**2. Могут ли файлы, являющиеся жесткой ссылкой на один объект, иметь разные права доступа и владельца? Почему?**  
> Не могут. Атрибуты безопасности (права, владелец) являются свойствами inode,  
> а этот объект один для всех файлов, являющихся жесткой ссылкой на один объект.  

**4. Используя fdisk, разбейте первый диск на 2 раздела: 2 Гб, оставшееся пространство.**  
> fdisk -l  
> Disk /dev/sda: 64 GiB, 68719476736 bytes, 134217728 sectors  
>> /dev/sda1  *       2048   1050623   1048576  512M  b W95 FAT32  
>> /dev/sda2       1052670 134215679 133163010 63.5G  5 Extended  
>> /dev/sda5       1052672 134215679 133163008 63.5G 8e Linux LVM
> 
> Disk /dev/sdb: 2.51 GiB, 2684354560 bytes, 5242880 sectors  
> Disk /dev/sdc: 2.51 GiB, 2684354560 bytes, 5242880 sectors  
> 
> fdisk /dev/sdb  
> n  
> p  
> 1  
> 2048  
> +2G  
> n  
> p  
> 2  
> 4196352  
> 5242879  
> w  
> 
> fdisk -l  
> Disk /dev/sda: 64 GiB, 68719476736 bytes, 134217728 sectors  
>> /dev/sda1  *       2048   1050623   1048576  512M  b W95 FAT32  
>> /dev/sda2       1052670 134215679 133163010 63.5G  5 Extended  
>> /dev/sda5       1052672 134215679 133163008 63.5G 8e Linux LVM  
> 
> Disk /dev/sdb: 2.51 GiB, 2684354560 bytes, 5242880 sectors  
>> /dev/sdb1          2048 4196351 4194304    2G 83 Linux  
>> /dev/sdb2       4196352 5242879 1046528  511M 83 Linux
> 
> Disk /dev/sdc: 2.51 GiB, 2684354560 bytes, 5242880 sectors  

**5. Используя sfdisk, перенесите данную таблицу разделов на второй диск.**  
> sfdisk -d /dev/sdb > disk_save.txt  
> sfdisk /dev/sdc < disk_save.txt  
> sfdisk -l  
> Disk /dev/sda: 64 GiB, 68719476736 bytes, 134217728 sectors  
>> /dev/sda1  *       2048   1050623   1048576  512M  b W95 FAT32  
>> /dev/sda2       1052670 134215679 133163010 63.5G  5 Extended  
>> /dev/sda5       1052672 134215679 133163008 63.5G 8e Linux LVM  
> 
> Disk /dev/sdb: 2.51 GiB, 2684354560 bytes, 5242880 sectors  
>> /dev/sdb1          2048 4196351 4194304    2G 83 Linux  
>> /dev/sdb2       4196352 5242879 1046528  511M 83 Linux  
> 
> Disk /dev/sdc: 2.51 GiB, 2684354560 bytes, 5242880 sectors  
>> /dev/sdc1          2048 4196351 4194304    2G 83 Linux  
>> /dev/sdc2       4196352 5242879 1046528  511M 83 Linux  

**6. Соберите mdadm RAID1 на паре разделов 2 Гб.**  
> mdadm -Cv /dev/md0 --level=1 --raid-devices=2 /dev/sdb1 /dev/sdc1  

**7. Соберите mdadm RAID0 на второй паре маленьких разделов.**  
> mdadm -Cv /dev/md1 --level=0 --raid-devices=2 /dev/sdb2 /dev/sdc2  

**8. Создайте 2 независимых PV на получившихся md-устройствах.**  
> pvcreate /dev/md0 /dev/md1  

**9. Создайте общую volume-group на этих двух PV.**  
> vgcreate LVM_Netology /dev/md0 /dev/md1  

**10. Создайте LV размером 100 Мб, указав его расположение на PV с RAID0.**  
> lvcreate -L 100m LVM_Netology /dev/md1  

**11. Создайте mkfs.ext4 ФС на получившемся LV.**  
> mkfs.ext4 /dev/LVM_Netology/lvol0  

**12. Смонтируйте этот раздел в любую директорию, например, /tmp/new.**  
> mkdir /tmp/new  
> mount /dev/LVM_Netology/lvol0 /tmp/new  

**13. Поместите туда тестовый файл, например wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz.**  
```
root@vagrant:~# ls -l /tmp/new/  
total 21992  
drwx------ 2 root root    16384 Nov 28 17:11 lost+found  
-rw-r--r-- 1 root root 22500661 Nov 28 15:54 test.gz  
```
**14. Прикрепите вывод lsblk.**  
```
root@vagrant:~# lsblk
NAME                     MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sda                        8:0    0   64G  0 disk
├─sda1                     8:1    0  512M  0 part  /boot/efi
├─sda2                     8:2    0    1K  0 part
└─sda5                     8:5    0 63.5G  0 part
  ├─vgvagrant-root       253:0    0 62.6G  0 lvm   /
  └─vgvagrant-swap_1     253:1    0  980M  0 lvm   [SWAP]
sdb                        8:16   0  2.5G  0 disk
├─sdb1                     8:17   0    2G  0 part
│ └─md0                    9:0    0    2G  0 raid1
└─sdb2                     8:18   0  511M  0 part
  └─md1                    9:1    0 1018M  0 raid0
    └─LVM_Netology-lvol0 253:2    0  100M  0 lvm   /tmp/new
sdc                        8:32   0  2.5G  0 disk
├─sdc1                     8:33   0    2G  0 part
│ └─md0                    9:0    0    2G  0 raid1
└─sdc2                     8:34   0  511M  0 part
  └─md1                    9:1    0 1018M  0 raid0
    └─LVM_Netology-lvol0 253:2    0  100M  0 lvm   /tmp/new
```
**15. Протестируйте целостность файла:**  
```
root@vagrant:~# gzip -t /tmp/new/test.gz
root@vagrant:~# echo $?
0
```
**16. Используя pvmove, переместите содержимое PV с RAID0 на RAID1.**  
> pvmove -i5 /dev/md1 /dev/md0  

**17. Сделайте --fail на устройство в вашем RAID1 md.**  
> mdadm /dev/md0 -f /dev/sdc1  
> mdadm --detail /dev/md0  
```commandline
/dev/md0:
    Number   Major   Minor   RaidDevice State
       0       8       17        0      active sync   /dev/sdb1
       -       0        0        1      removed

       1       8       33        -      faulty   /dev/sdc1
```
**18. Подтвердите выводом dmesg, что RAID1 работает в деградированном состоянии.**  
> [14510.893542] md/raid1:md0: Disk failure on sdc1, disabling device.  
> md/raid1:md0: Operation continuing on 1 devices.  

**19. Протестируйте целостность файла, несмотря на "сбойный" диск он должен продолжать быть доступен:**  
```
root@vagrant:~# gzip -t /tmp/new/test.gz
root@vagrant:~# echo $?
0
```