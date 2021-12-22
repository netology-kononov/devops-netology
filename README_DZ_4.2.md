**Задача 1**  
| Вопрос  | Ответ |  
| --- | --- |
| Какое значение будет присвоено переменной `c`?  | is not defined  |  
| Как получить для переменной `c` значение 12?  | c = str(a) + b  |  
| Как получить для переменной `c` значение 3?  | c = a + int(b)  |  

**Задача 2**  
> Cкрипт:
```python
#!/usr/bin/env python3

import os

git_dir = "/home/ubun/netology/sysadm-homeworks"
bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(git_dir + "/" + prepare_result)
```
> Вывод скрипта при запуске при тестировании:
```
$ ./check_git_modified.py
/home/ubun/netology/sysadm-homeworks/README_DZ_4.2.md
/home/ubun/netology/sysadm-homeworks/branching/rebase.sh
/home/ubun/netology/sysadm-homeworks/check_git_modified.py
```

**Задача 3**
> Скрипт:  
```python
#!/usr/bin/env python3
# Скрипт принимает аргумент с именем папки репозитария git, если параметр не указан, предполагается, что репозитарий 
# расположен в текущей папке.
# Для простоты реализации принят ряд допущений:
# Не производится проверка, что указанный в аргументе путь коректный.
# Не производится проверка, что в указанной папке существует репозитарий.

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
```
> Вывод скрипта при запуске при тестировании:
```
$ ./check_git_modified.py /home/ubun/netology/sysadm-homeworks
/home/ubun/netology/sysadm-homeworks/README_DZ_4.2.md
/home/ubun/netology/sysadm-homeworks/branching/rebase.sh
/home/ubun/netology/sysadm-homeworks/check_git_modified.py
```

**Задача 4**  
> Скрипт:  
```python
#!/usr/bin/env python3

import socket
import time

ip_addr = {}
ip_addr_prev = {}
dict_init = True
url_list = ("drive.google.com", "mail.google.com", "google.com")
while True:
    for url in url_list:
        ip_addr[url] = socket.gethostbyname(url)
        print(url + " - " + ip_addr[url])
        if (dict_init):
            ip_addr_prev[url] = ip_addr[url]
        if (ip_addr[url] != ip_addr_prev[url]):
            print("[ERROR] " + url + " IP mismatch: " + ip_addr_prev[url] + " " + ip_addr[url])
        ip_addr_prev[url] = ip_addr[url]
    time.sleep(10)
    dict_init = False
```

> Вывод скрипта при запуске при тестировании:  
```
mail.google.com - 64.233.161.83
google.com - 142.250.150.138
drive.google.com - 64.233.162.194
mail.google.com - 64.233.161.83
google.com - 142.250.150.101
[ERROR] google.com IP mismatch: 142.250.150.138 142.250.150.101
drive.google.com - 64.233.162.194
mail.google.com - 64.233.161.83
google.com - 142.250.150.101
```

**Дополнительное задание**  
> Скрипт:  
```python
#!/usr/bin/env python3
#Используется авторизация в GitHub по токену, которая имеет следующее ограичение:
#При использовании push в публичный репозитарий, токен отзывается.
#https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/token-expiration-and-revocation
#Скрипт работает только с приватными репозитариями.

import os
import sys
import git
from github import Github

config_file = "config.cfg"
local_repo_dir = "~/netology/rebase-merge"
commit_message = "Commit Message"
github_token = "ghp_ggL*************************cZ0n3OKrBx"
github_repo = "netology-kononov/rebase-merge"
branch_name = "dev"
pullrequest_body = "Request Body"

if sys.argv[1:]:
    pullrequest_title = sys.argv[1]
else:
    print("No Arguments (pull request title) found")
    sys.exit()

bash_unzip = "gunzip -f " + config_file + ".gz"
os.popen(bash_unzip)

local_repo = git.Repo(local_repo_dir)
local_repo.git.add(config_file)
local_repo.git.commit(m=commit_message)
local_repo.git.push()

gh = Github(github_token)
gh_repo = gh.get_repo(github_repo)
pr = gh_repo.create_pull(title=pullrequest_title, body=pullrequest_body, head=branch_name, base="main")
pr
```
> Вывод скрипта при запуске при тестировании:  
```
~/netology/rebase-merge$ ./github_auto.py
No Arguments (pull request title) found
~/netology/rebase-merge$
~/netology/rebase-merge$
~/netology/rebase-merge$ ./github_auto.py "New config"
Enter passphrase for key '/home/ubun/.ssh/id_rsa':
~/netology/rebase-merge$
```