# Playbook для установки Clickhouse и Vector #

## Playbook содержит 2 сценария. ##  
Сценарий **Install Clickhouse** производит установку Clickhouse версии, указанной в переменной *clickhouse_version*.  
Установка происходит списком rpm-пакетов из переменной *clickhouse_packages*.  
Установка происходит на хосты из группы *clickhouse*.

Сценарий **Install Vector** производит установку Vector версии, указанной в переменной *vector_version*.  
Установка происходит через менеджер пакетов yum.  
Установка происходит на хосты из группы *clickhouse*.  

Тэг **08-ansible-02-playbook** установлен на результат выполнения домашнего задания № 8.2.

Репозиторий расположен по адресу:
https://github.com/netology-kononov/devops-netology-ansible-02/tree/08-ansible-02-playbook
