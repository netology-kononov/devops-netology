**1. Проверьте список доступных сетевых интерфейсов на вашем компьютере. Какие команды есть для этого в Linux и в Windows?**  
```
vagrant@vagrant:~$ ip -br link show
lo               UNKNOWN        00:00:00:00:00:00 <LOOPBACK,UP,LOWER_UP>
eth0             UP             08:00:27:73:60:cf <BROADCAST,MULTICAST,UP,LOWER_UP>


C:\Users\user> Get-NetAdapter

Name                      InterfaceDescription                    ifIndex Status       MacAddress             LinkSpeed
----                      --------------------                    ------- ------       ----------             ---------
vEthernet (WSL)           Hyper-V Virtual Ethernet Adapter             36 Up           00-15-5D-C1-85-42        10 Gbps
Ethernet                  Qualcomm Atheros AR8151 PCI-E Gigabi...      17 Up           14-DA-E9-EE-0E-5E         1 Gbps
VirtualBox Host-Only N... VirtualBox Host-Only Ethernet Adapter         9 Up           0A-00-27-00-00-09         1 Gbps
```

**2. Какой протокол используется для распознавания соседа по сетевому интерфейсу? Какой пакет и команды есть в Linux для этого?**  
> Существует много протоколов для этой задачи: CDP, LLTD, MNDP.  
> Вендоро-независимым является Link Layer Discovery Protocol (LLDP).  
> В Ubuntu есть пакет lldpd для работы с этим протоколом.  
> Команда lldpcli вызывает консоль для работы с десоном, список команд доступен по man lldpcli, например:  
> [lldpcli] $ show neighbors  

**3. Какая технология используется для разделения L2 коммутатора на несколько виртуальных сетей? 
Какой пакет и команды есть в Linux для этого? Приведите пример конфига.**  
> Для создания виртуальных сетей используется технология VLAN.  
> В Ubuntu существует пакет vlan и модуль ядра 8021q  
> Конфигурация для netplan:
```
vagrant@vagrant:~$ cat /etc/netplan/01-netcfg.yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: true
  vlans:
    vlan10:
      id: 10
      link: eth0
      addresses: [ "10.10.10.10/24" ]
```
> Результат применения конфигурации:
```
vagrant@vagrant:~$ ip -br link show
lo               UNKNOWN        00:00:00:00:00:00 <LOOPBACK,UP,LOWER_UP>
eth0             UP             08:00:27:73:60:cf <BROADCAST,MULTICAST,UP,LOWER_UP>
vlan10@eth0      UP             08:00:27:73:60:cf <BROADCAST,MULTICAST,UP,LOWER_UP>
```

**4. Какие типы агрегации интерфейсов есть в Linux? Какие опции есть для балансировки нагрузки? Приведите пример конфига.**  
> Существует 7 типов агрегации в Linux:  
> mode=0 – Round-Robin - используются все интерфейсы по очереди;  
> mode=1 - Active-Backup - Используется один интерфейс, второй остаётся в качестве резервного;  
> mode=2 - Balance XOR - Балансировка исходя из MAC адресов отправителя и получателя;  
> mode=3 - Broadcast - Исходящий трафик передаётся во все интерфейсы;  
> mode=4 - 802.3ad - В этом режиме возможны как простая агрегация (LAG), так и управляемая (LACP);  
> mode=5 - Balance TLB - Передаваемый трафик балансируется исходя из загруженности инерфейсов;  
> mode=6 - Balance ALB - Входящий и исходящий трафик балансируеся исходя из загруженности интерфейсов.  
> Балансировка нагрузки может происходить по MAC-адресам, IP-адресам или портам (L2,L3,L4-based).  
> Пример конфигурации агрегированных интерфейсов в netplan (режим: active-backup):
```
vagrant@vagrant:~$ cat /etc/netplan/50-vagrant.yaml
---
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: no
    eth1:
      dhcp4: no
  bonds:
    bond0:
      dhcp4: yes
      interfaces:
        - eth0
        - eth1
      parameters:
        mode: active-backup
        primary: eth0
vagrant@vagrant:~$
```
> Список интерфейсов после применения конфигурации:
```
vagrant@vagrant:~$ ip -br link show
lo               UNKNOWN        00:00:00:00:00:00 <LOOPBACK,UP,LOWER_UP>
eth0             UP             e6:b6:ef:2e:29:11 <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP>
eth1             UP             e6:b6:ef:2e:29:11 <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP>
bond0            UP             e6:b6:ef:2e:29:11 <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP>
```

**5. Сколько IP адресов в сети с маской /29 ? Сколько /29 подсетей можно получить из сети с маской /24. 
Приведите несколько примеров /29 подсетей внутри сети 10.10.10.0/24.**  
> 8 IP-адресов: 6 хостов, адрес сети и широковещательный адрес.  
> 32 подсети /29 в сети /24.  
> 10.10.10.0/29, 10.10.10.8/29, 10.10.10.16/29.  

**6. Задача: вас попросили организовать стык между 2-мя организациями. 
Диапазоны 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 уже заняты. 
Из какой подсети допустимо взять частные IP адреса? Маску выберите из расчета максимум 40-50 хостов внутри подсети.**  
> Существует диапазон 100.64.0.0 — 100.127.255.255 Carrier-Grade NAT, который можно использовать для этой задачи.  
> Так как необходимо, чтобы в сети существовало не менее 50 хостов, минимальный размер сети - 64 адреса (62 хоста),  
> например: 100.64.0.0/26.  

**7.1 Как проверить ARP таблицу в Linux, Windows?**  
> Linux: ip neigh show  
> Windows: arp -a

**7.2 Как очистить ARP кеш полностью?**  
> Linux: ip neigh flush all  
> Windows: arp -d *  

**7.3 Как из ARP таблицы удалить только один нужный IP?**  
> Linux: ip neigh del inet_addr  
> Windows: arp -d inet_addr