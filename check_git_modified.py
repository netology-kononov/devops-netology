#!/usr/bin/env python3
# Скрипт принимает аргумент с полным именем папки репозитария git, если параметр не указан, предполагается,
# что репозитарий расположен в текущей папке.
# Для простоты реализации принят ряд допущений:
# Проверка, что указанный в аргументе путь коректный не производится.
# Проверка, что в указанной папке существует репозитарий не производится.

import os
import sys

git_dir = os.getcwd()
if sys.argv[1:]:
    bash_command2 = "realpath " + sys.argv[1]
    git_dir = os.popen(bash_command2).read().strip()
bash_command = "git -C " + git_dir + " status"
result_os = os.popen(bash_command).read()
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(git_dir + "/" + prepare_result)