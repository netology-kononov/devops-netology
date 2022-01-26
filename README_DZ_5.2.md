**1.1 Опишите своими словами основные преимущества применения на практике IaaC паттернов.**  
> Паттерны IaaC позволяют упростить, автоматизировать и повысить эффективность процесс разработки: внесение изменений в 
> код, проверка его работоспособности и соответствия бизнес-задачам, а также запуск кода в производственной среде. 
> Этот подход позволяет оперативно и часто вносить изменения для исправления ошибок и добавления нового функционала. 
> Представление инфраструктуры в форме кода позволяет быстрее масштабировать инфраструктуру и мигрировать инфраструктуру 
> на другие площадки, разворачивать тестовые среды. Позволяет обеспечить стабильность среды и конфигураций между средами 
> разработки, тестирования и производственной среде.  

**1.2 Какой из принципов IaaC является основополагающим?**  
> Основополагающим принципом является идемпотентность выполняемого кода.  

**2.1 Чем Ansible выгодно отличается от других систем управление конфигурациями?**  
> 1. Использование Ansible не требует внедрения PKI-окружения на управляемых объектах, используется имеющаяся SSH инфраструктура, что позволяет увеличить скорость внедрения решения.
> 2. Возможность использования декларативного метода описания конфигураций даёт простоту применения инструмента.
> 3. Ansible позволяет использовать внешние модули и роли, что обеспечивает расширение возможностей применения иструмента.  

**2.2 Какой, на ваш взгляд, метод работы систем конфигурации более надёжный push или pull?**  
> Более комфортным способом управления кофигурацией является push метод, он позволяет запустиь задачу и сразу увидеть 
> результат её выполнения. С другой стороны, метод pull позволяет передавать конфигурацию на систему, прямой доступ на 
> которую невозможен из соображений безопасности или технических ограничений. С моей точки зрения, надёжность определяется 
> не методом доставки изменений, а алгоритмом проверки целостности и корректности изменений и механизмом мониторинга 
> результатов применения изменений.  

**3. Установить на личный компьютер: VirtualBox, Vagrant, Ansible.**  
```commandline
echo "deb http://download.virtualbox.org/virtualbox/debian $(lsb_release -sc) contrib" | sudo tee -a /etc/apt/sources.list
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
sudo apt-get update
sudo apt-get install dkms
sudo apt-get install virtualbox-6.1
sudo usermod -a -G vboxusers `whoami`

vagrant@hv-temp:~$ vboxmanage --version
6.1.32r149290

curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install vagrant

vagrant@hv-temp:~$ vagrant -v
Vagrant 2.2.19

sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible

vagrant@hv-temp:~$ ansible --version
ansible [core 2.12.1]
```

**4. Воспроизвести практическую часть лекции самостоятельно.**  
> Простым способом решения задачи было установка связки VirtualBox + Vagrant + Ansible на хост с ОС Linux, для этого использовались 
> конфигурационные файлы из папки src домашнего задания с минимумом правок:
```commandline
vagrant@hv-temp:~/download/vagrant$ vagrant up

PLAY RECAP *********************************************************************
server1.netology           : ok=7    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

vagrant@hv-temp:~/download/vagrant$ vagrant ssh

vagrant@server1:~$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
> Для запуска связки VirtualBox + Vagrant + Ansible на хост с ОС Windows существует проблема запуска Ansible, работа которого на 
> ОС Windows не поддерживается. В связи с чем, я посчитал возможным использование другого метода применения Ansible в Vagrant - 
> установка Ansible на гостевую ОС. Такое решение несколько медленнее оригинального, однако лишено зависимости от ОС хоста. 
> В ряд конфигурационных файлов были внесены изменения:  
```commandline
inventory :
server2.netology ansible_connection=local ansible_user=vagrant

provision.yml :
shell: cd ~/ && curl -fsSL get.docker.com -o get-docker.sh && chmod +x get-docker.sh && ./get-docker.sh

Vagrantfile :
:hostname => HOST_PREFIX + "2" + DOMAIN,
node.vm.provision "ansible_local" do |setup|
```
```commandline
>vagrant up

PLAY RECAP *********************************************************************
server2.netology           : ok=7    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

>vagrant ssh

vagrant@server2:~$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```