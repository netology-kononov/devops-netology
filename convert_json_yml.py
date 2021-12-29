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
# Если ошибочный файл с расширением YAML предполагаем, что у него формат YAML
if filename.lower().endswith('.yml') and error_yaml_file and error_json_file:
    print('Error while parsing YAML file: ' + str(error_yaml_message))
    print("At line [" + str(error_yaml_line_number) + "]: " + linecache.getline(yaml_filename, error_yaml_line_number))
    sys.exit()
# Если ошибочный файл с расширением JSON предполагаем, что у него формат JSON
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