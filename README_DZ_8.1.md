#Репозитарий расположен:  
https://github.com/netology-kononov/devops-netology-ansible-01

#Ответы на вопросы:  
**1. Где расположен файл с some_fact из второго пункта задания?**  
> https://github.com/netology-kononov/devops-netology-ansible-01/blob/master/group_vars/all/examp.yml

**2. Какая команда нужна для запуска вашего playbook на окружении test.yml?**  
> ansible-playbook site.yml -i inventory/test.yml

**3. Какой командой можно зашифровать файл?**  
> ansible-vault encrypt FILE_NAME

**4. Какой командой можно расшифровать файл?**  
> ansible-vault decrypt FILE_NAME

**5. Можно ли посмотреть содержимое зашифрованного файла без команды расшифровки файла? Если можно, то как?**  
> можно,
> ansible-vault view FILE_NAME

**6. Как выглядит команда запуска playbook, если переменные зашифрованы?**  
> ansible-playbook site.yml -i inventory/prod.yml --ask-vault-password

**7. Как называется модуль подключения к host на windows?**  
> winrm - Run tasks over Microsoft's WinRM  
> psrp - Run tasks over Microsoft PowerShell Remoting Protocol

**8. Приведите полный текст команды для поиска информации в документации ansible для модуля подключений ssh**  
> ansible-doc -t connection ssh

**9. Какой параметр из модуля подключения ssh необходим для того, чтобы определить пользователя, под которым необходимо совершать подключение?**  
```yaml
- remote_user
        User name with which to login to the remote server, normally set by the remote_user keyword.
        If no user is supplied, Ansible will let the SSH client binary choose the user as it normally.
        [Default: (null)]
        set_via:
          cli:
          - name: user
            option: --user
          env:
          - name: ANSIBLE_REMOTE_USER
          ini:
          - key: remote_user
            section: defaults
          vars:
          - name: ansible_user
          - name: ansible_ssh_user
```