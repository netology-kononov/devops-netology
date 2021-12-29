**Задача 1**  
> Строка 6, пропущена запятая между элементами списка  
> Строка 9, пропущена кавычка в  имени ключа  
> Строки 5 и 9, не ясно какой тип данных должен быть значением ключа "ip". Если как в примере, то тип данных должен быть строка и заключен в кавычки.  

**Задача 2**  
```python
#!/usr/bin/env python3
# Для реализации задачи записи YAML И JSON файлов в указанном формате пришлось изменить формат хранения данных.
# Вместо словаря {URL: IP-адрес} в данном случае удобнее использовать список словарей [{URL: IP-адрес}],
# в каждом из которых существует по одной записи.
# Такой подход позволяет получить дамп YAML-файла без дополнительных манипуляций.
# Дамп этой структуры в JSON-файл также мне кажется более удобочитаемым (см. export.json),
# поэтому я оставил его в качестве дополнительного решения.
# Для выполнения задания буквально и получения формата указанного в задаче (см. export_format.json),
# пришлось производить преобразования вывода дампа списка словарей как преобразование строки.
# Такой формат файла не соответствует стандарту JSON.
# При необходимости формат вывода можно произвольно изменять с помощью преобразований через переменную format_json.

import json
import socket
import time
import yaml

ip_addr = {}
url_list = ("drive.google.com", "mail.google.com", "google.com")
dict_list = [None] * len(url_list)
while True:
    for url in url_list:
        i = url_list.index(url)
        ip_addr[url] = socket.gethostbyname(url)
        print(url + " - " + ip_addr[url])
        if dict_list[i] is not None:
            if ip_addr[url] != dict_list[i].get(url):
                print("[ERROR] " + url + " IP mismatch: " + dict_list[i].get(url) + " " + ip_addr[url])
        ip_addr_copy = ip_addr.copy()
        dict_list[i] = ip_addr_copy
        ip_addr.clear()
    with open('export.yml', 'w') as yaml_file:
        yaml_file.write(yaml.dump(dict_list, indent=4))
    with open('export.json', 'w') as json_file:
        json_file.write(json.dumps(dict_list, indent=0))
    format_json = json.dumps(dict_list)
    format_json = format_json.replace(', ', '\n')
    format_json = format_json.replace('[', '')
    format_json = format_json.replace(']', '\n')
    with open('export_format.json', 'w') as json_file_format:
        json_file_format.write(format_json)
    time.sleep(10)
```

> Вывод скрипта при запуске при тестировании:  
```
drive.google.com - 64.233.165.194
mail.google.com - 74.125.131.18
google.com - 142.250.150.102
drive.google.com - 64.233.165.194
mail.google.com - 74.125.131.83
[ERROR] mail.google.com IP mismatch: 74.125.131.18 74.125.131.83
google.com - 142.250.150.102
drive.google.com - 64.233.165.194
mail.google.com - 74.125.131.83
google.com - 142.250.150.102
```

> yml-файл, который записал скрипт:
```yaml
-   drive.google.com: 64.233.165.194
-   mail.google.com: 74.125.131.83
-   google.com: 142.250.150.102
```

> json-файл, который записал скрипт (export.json):
```json
[
{
"drive.google.com": "64.233.165.194"
},
{
"mail.google.com": "74.125.131.83"
},
{
"google.com": "142.250.150.102"
}
]
```

> json-файл, который записал скрипт (export_format.json):
```json
{"drive.google.com": "64.233.165.194"}
{"mail.google.com": "74.125.131.83"}
{"google.com": "142.250.150.102"}
```

**Дополнительное задание**  
> Скрипт:  
```python
#!/usr/bin/env python3

import json
import sys
import yaml
import linecache

# Проверка наличия параметра
if sys.argv[1:]:
    filename = sys.argv[1]
else:
    print("No file to convert was found")
    sys.exit()
# Если не поддерживаемое расширение файла
if not filename.lower().endswith('.yml') and not filename.lower().endswith('.json'):
    print("No correct file extension was found")
    sys.exit()
# Попытка прочитать файл как YAML
yaml_filename = filename
with open(yaml_filename, 'r') as yaml_file:
    error_yaml_file = False
    try:
        load_yaml_file = yaml.safe_load(yaml_file)
    except yaml.YAMLError as load_error:
        error_yaml_message = load_error.problem
        error_yaml_mark = load_error.problem_mark
        error_yaml_line_number = error_yaml_mark.line
        error_yaml_file = True
# Попытка прочитать файл как JSON
json_filename = filename
with open(json_filename, 'r') as json_file:
    error_json_file = False
    try:
        load_json_file = json.load(json_file)
    except json.JSONDecodeError as load_error:
        error_json_message = load_error.msg
        error_json_line_number = load_error.lineno
        error_json_file = True
# Если некорректный формат файла с расширением YAML предполагаем, что у него формат YAML
if filename.lower().endswith('.yml') and error_yaml_file and error_json_file:
    print('Error while parsing YAML file: ' + str(error_yaml_message))
    print("At line [" + str(error_yaml_line_number) + "]: " + linecache.getline(yaml_filename, error_yaml_line_number))
    sys.exit()
# Если некорректный формат файла с расширением JSON предполагаем, что у него формат JSON
if filename.lower().endswith('.json') and error_yaml_file and error_json_file:
    print('Error while parsing JSON file: ' + str(error_json_message))
    print("At line [" + str(error_json_line_number) + "]: " + linecache.getline(json_filename, error_json_line_number))
    sys.exit()
# Если корректный YAML формат файла
if not error_yaml_file:
    if filename.lower().endswith('.yml'):
        new_filename = filename[:-3] + 'json'
    elif error_json_file:
        new_filename = filename
    else:
        new_filename = False
    if new_filename:
        with open(new_filename, 'w') as json_file:
            json_file.write(json.dumps(load_yaml_file, indent=4))
        print("Converted into: " + str(new_filename))
        sys.exit()
# Если корректный JSON формат файла
if not error_json_file:
    if filename.lower().endswith('.json'):
        new_filename = filename[:-4] + 'yml'
    elif error_yaml_file:
        new_filename = filename
    else:
        new_filename = False
    if new_filename:
        with open(new_filename, 'w') as yaml_file:
            yaml_file.write(yaml.dump(load_json_file, indent=4))
        print("Converted into: " + str(new_filename))
        sys.exit()
print("Incorrect script completion.")
```
> Вывод скрипта при запуске при тестировании:  
```
$ ./convert_json_yml.py convert_from_yml.yml
Converted into: convert_from_yml.json

$ ./convert_json_yml.py convert_from_json.json
Converted into: convert_from_json.yml

$ ./convert_json_yml.py error_from_yml.yml
Error while parsing YAML file: expected <block end>, but found '?'
At line [1]: -   drive.google.com: 64.233.165.194

$ ./convert_json_yml.py error_from_json.json
Error while parsing JSON file: Expecting ',' delimiter
At line [5]:     {

```