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
    time.sleep(20)
