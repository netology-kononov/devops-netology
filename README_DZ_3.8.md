**1. Подключитесь к публичному маршрутизатору в интернет. Найдите маршрут к вашему публичному IP.**  
```commandline
route-views>show ip route 93.123.224.0 255.255.224.0
Routing entry for 93.123.224.0/19
  Known via "bgp 6447", distance 20, metric 0
  Tag 6939, type external
  Last update from 64.71.137.241 5w3d ago
  Routing Descriptor Blocks:
  * 64.71.137.241, from 64.71.137.241, 5w3d ago
      Route metric is 0, traffic share count is 1
      AS Hops 2
      Route tag 6939
      MPLS label: none

route-views>show bgp 93.123.224.0 255.255.224.0
BGP routing table entry for 93.123.224.0/19, version 1220386377
Paths: (5 available, best #5, table default)
  Not advertised to any peer
  Refresh Epoch 3
  3303 6939 35539
    217.192.89.50 from 217.192.89.50 (138.187.128.158)
      Origin IGP, localpref 100, valid, external
      Community: 3303:1006 3303:1021 3303:1030 3303:3067 6939:7154 6939:8233 6939:9002
      path 7FE01CD4D6F8 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  1351 6939 35539
    132.198.255.253 from 132.198.255.253 (132.198.255.253)
      Origin IGP, localpref 100, valid, external
      path 7FE108F88FF0 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3267 35539
    194.85.40.15 from 194.85.40.15 (185.141.126.1)
      Origin IGP, metric 0, localpref 100, valid, external
      path 7FE101C554F0 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  20130 6939 35539
    140.192.8.16 from 140.192.8.16 (140.192.8.16)
      Origin IGP, localpref 100, valid, external
      path 7FE188050908 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  6939 35539
    64.71.137.241 from 64.71.137.241 (216.218.252.164)
      Origin IGP, localpref 100, valid, external, best
      unknown transitive attribute: flag 0xE0 type 0x20 length 0xC
        value 0000 21B7 0000 0777 0000 21B7
      path 7FE0CE96A290 RPKI State not found
      rx pathid: 0, tx pathid: 0x0
```

**2. Создайте dummy0 интерфейс в Ubuntu. Добавьте несколько статических маршрутов. Проверьте таблицу маршрутизации.**  
> Поскольку в Ububntu менеджер сети не поддерживает устройства типа dummy, 
> устройство типа dummy было создано с помощью конфигурационного файла^ /etc/network/interfaces.d/dummy0  
```
auto dummy0
iface dummy0 inet static
address 100.64.0.1
netmask 255.192.0.0
iface dummy0 inet static
address 172.16.0.1
netmask 255.255.0.0
```
> Результат применения конфигурации:  
```
vagrant@vagrant:~$ ip r
default via 10.0.2.2 dev eth0 proto dhcp src 10.0.2.15 metric 100
10.0.2.0/24 dev eth0 proto kernel scope link src 10.0.2.15
10.0.2.2 dev eth0 proto dhcp scope link src 10.0.2.15 metric 100
10.10.10.0/24 dev vlan10 proto kernel scope link src 10.10.10.10
100.64.0.0/10 dev dummy0 proto kernel scope link src 100.64.0.1
172.16.0.0/16 dev dummy0 proto kernel scope link src 172.16.0.1
```

**3. Проверьте открытые TCP порты в Ubuntu, какие протоколы и приложения используют эти порты? 
Приведите несколько примеров.**  
> Протоколы можно определить по столбцу Local Address:Port исходя из стандартных портов ими используемых:  
> 22 - ssh;  
> 53 - dns. (можно было их отобразить в выводе команды, если не использовать параметр -n)  
> Приложения использующие порты указаны в столбце Process:  
> sshd, systemd-resolve, netdata, node_exporter, rpcbind.
```
vagrant@vagrant:~$ sudo ss -tapn
State             Recv-Q             Send-Q                         Local Address:Port                          Peer Address:Port             Process
LISTEN            0                  4096                                 0.0.0.0:19999                              0.0.0.0:*                 users:(("netdata",pid=668,fd=4))
LISTEN            0                  4096                                 0.0.0.0:111                                0.0.0.0:*                 users:(("rpcbind",pid=569,fd=4),("systemd",pid=1,fd=35))
LISTEN            0                  4096                           127.0.0.53%lo:53                                 0.0.0.0:*                 users:(("systemd-resolve",pid=571,fd=13))
LISTEN            0                  128                                  0.0.0.0:22                                 0.0.0.0:*                 users:(("sshd",pid=690,fd=3))
LISTEN            0                  4096                               127.0.0.1:8125                               0.0.0.0:*                 users:(("netdata",pid=668,fd=42))
ESTAB             0                  0                                  10.0.2.15:22                                10.0.2.2:62581             users:(("sshd",pid=1242,fd=4),("sshd",pid=1194,fd=4))
LISTEN            0                  4096                                       *:9100                                     *:*                 users:(("node_exporter",pid=618,fd=3))
LISTEN            0                  4096                                    [::]:111                                   [::]:*                 users:(("rpcbind",pid=569,fd=6),("systemd",pid=1,fd=37))
LISTEN            0                  128                                     [::]:22                                    [::]:*                 users:(("sshd",pid=690,fd=4))
LISTEN            0                  4096                                   [::1]:8125                                  [::]:*                 users:(("netdata",pid=668,fd=41))
```

**4. Проверьте используемые UDP сокеты в Ubuntu, какие протоколы и приложения используют эти порты?**  
> Протоколы можно определить по столбцу Local Address:Port исходя из стандартных портов ими используемых:  
> 53 - dns;  
> 68 - dhcp.  
> Приложения использующие порты указаны в столбце Process:  
> systemd-resolve, systemd-network, netdata, rpcbind.
```
vagrant@vagrant:~$ sudo ss -uapn
State              Recv-Q             Send-Q                          Local Address:Port                         Peer Address:Port            Process
UNCONN             0                  0                                   127.0.0.1:8125                              0.0.0.0:*                users:(("netdata",pid=668,fd=38))
UNCONN             0                  0                               127.0.0.53%lo:53                                0.0.0.0:*                users:(("systemd-resolve",pid=571,fd=12))
UNCONN             0                  0                              10.0.2.15%eth0:68                                0.0.0.0:*                users:(("systemd-network",pid=384,fd=15))
UNCONN             0                  0                                     0.0.0.0:111                               0.0.0.0:*                users:(("rpcbind",pid=569,fd=5),("systemd",pid=1,fd=36))
UNCONN             0                  0                                       [::1]:8125                                 [::]:*                users:(("netdata",pid=668,fd=37))
UNCONN             0                  0                                        [::]:111                                  [::]:*                users:(("rpcbind",pid=569,fd=7),("systemd",pid=1,fd=38))
```

**5. Используя diagrams.net, создайте L3 диаграмму вашей домашней сети или любой другой сети, с которой вы работали.**  
> https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Test%20Diagram.drawio#R7ZrPb6M4FMf%2FmhyLbPwD%2BzjtdGcOu9qReljtXkYMuAGV4Mg4TTJ%2F%2FZpgCJhUYZiEUik9pPAwBr7v4%2BfnBwv0sNp9UeE6%2BUvGIlv4IN4t0OeF70OKgPlXWvbWArG1LFUaW9vR8JT%2BFNZYN9uksSg6DbWUmU7XXWMk81xEumMLlZLbbrNnmXWvug6Xomd4isKsb%2F0njXVSWZkfHO1fRbpM6itDyqsjq7BubJ%2BkSMJYblsm9LhAD0pKXW2tdg8iK9WrdanO%2B%2BONo82NKZHrISf8y%2B6WQZEk2%2F%2BwIF%2F%2FfvkZFXd3vr3b1zDb2Ce2d6v3tQSmG6O22bnfJqkWT%2BswKo9sjceNLdGrzOxBs6mkDnUqc7PLgdnv36G96VehtNi1TPaOvwi5ElrtTRN7FCFanWL5wcAKvz06oyYqafvB2kLr%2FmXT81Ehs2FF%2BhXB8LwFwwDMTDD%2FOoLd4QspRjjsKEYI8RB6Z9HAdUS71KgMiCMZeHfJIL2OZJfCDDLfc1TD%2BP1VOy%2BambfW5eZqtyzneC9Ki0h6Sm60UIX9byQqXoSOEstYS8q1THPT4vHVSFdYWxwWiYht2%2Bc0yx5kJtXhcgggynhQdqiVfBGtI8%2BHv%2BZIPR0bze9LN6Rm0v4z%2FCGyb7JIrfN%2BSK3lqtXgU5YuywNalh4P7V4k8uohzMNkaW4uWicTV3M%2B5KDn%2BYD1PU%2FQtULMWM8X29Q4WhReFu6F%2Bo6%2BV4YbAmcmZtSdmBHrA0BxH4DadnEABiQyZwDYSvWyNAFgfUNgWBRwcjNCSQ8BCOCJIHCt8E9uDEzMAMLBzBgYkDfdGLgoA3R2cSC4JQOTEuCzmSUD7DwAIo8%2FlQU1s5fLXLgLpk0eNy58U6FCblQkzoOoQ7UU%2BnzyIuJO9a6vd0tPcmJdVduUyMx677Vb8zslsr3CtxLiVlDnXXc2A7zuonpue1a7Rud0dK6fSpdePweXN089noIhxcApKCADKQhmRUHgRPWxEEDfKeG5Yf%2FKFMAhxacpMKAfEgPqLPQC132DOXA6wmxiDgYUhybhAA%2FkwJ8VB8EbU%2FzvhgOEJsZgQKVoVrPCvDCgziAOxmIAnY78iTFAM8Fg6KwwLwzc2g%2BmYzkgTkfuu4FrczDkBehwDuplpVlmvUyycpgZFudyvcFYONMNnnjpgEa%2FSSpEtFGp3nvPqRLbsLzsrXhwEsnm7Wv3m4hmimkhW3%2FX0SkeBG%2FT%2BVvFA3QiQzAPy1n5e%2F95YdzEDpZ7ctgGtb2xnAghzavampook5v4%2FKvbCwhMnEEJT1RnmoHbVthN8S6n8FxW5vUw%2F2BrMpN9e5wyAgkHEFAAukV4SJy62uCoC7jHOQ0YxsSMOcq6I7OX8185CNefDnwcTOY1GyPXfz7xEGMEEYAgwwEciQnCyIOcIWg2qc8ox93L8IkxmcuKbjAmcFaYYNj9lgP5gUcQxCbAHH7pOEpMCPEoP3JCu0FqckrmsuCr04uPRgkAHjVhwySgFAUBJ11o%2FLGFgLJfxgml3OcQmZDlZIPA%2BWJoNCZm9%2Fh1ctX8%2BJE3evwf