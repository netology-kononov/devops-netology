**1. Создайте самостоятельно простой unit-файл для node_exporter**  
> wget https://github.com/prometheus/node_exporter/releases/download/v1.3.0/node_exporter-1.3.0.linux-amd64.tar.gz  
> tar xvfz node_exporter-1.3.0.linux-amd64.tar.gz  
> cd node_exporter-1.3.0.linux-amd64  
> vi node-exporter.service  
```
[Unit]
Description=Node Exporter

[Service]
EnvironmentFile=/home/vagrant/node_exporter-1.3.0.linux-amd64/node_exporter.conf
ExecStart=/home/vagrant/node_exporter-1.3.0.linux-amd64/node_exporter $NE_ARG

[Install]
WantedBy=default.target
```
> sudo ln node-exporter.service /etc/systemd/system/node-exporter.service  
> sudo systemctl daemon-reload  

**1.1 поместите его в автозагрузку,**  
> sudo systemctl enable node-exporter.service  

**1.2 предусмотрите возможность добавления опций к запускаемому процессу через внешний файл,**  
> vi /home/vagrant/node_exporter-1.3.0.linux-amd64/node_exporter.conf
```
NE_ARG=--help
```
> передал сервису параметр --help через конфигурационный файл  

**1.3 удостоверьтесь, что с помощью systemctl процесс корректно стартует, завершается, а после перезагрузки автоматически поднимается.**  
> sudo systemctl start node-exporter.service | journalctl -u node-exporter.service  
> sudo systemctl stop node-exporter.service | journalctl -u node-exporter.service  
> sudo reboot  
> systemctl status node-exporter.service  

**2. Приведите несколько опций, которые вы бы выбрали для базового мониторинга хоста по CPU, памяти, диску и сети.**  
> node_cpu_guest_seconds_total Seconds the CPUs spent in guests (VMs) for each mode.  
> node_cpu_seconds_total Seconds the CPUs spent in each mode.  
> curl http://localhost:9100/metrics 2> /dev/null | grep ^node_cpu  

> node_memory_Active_anon_bytes Memory information field Active_anon_bytes.  
> node_memory_Active_bytes Memory information field Active_bytes.  
> node_memory_Active_file_bytes Memory information field Active_file_bytes.  
> node_memory_AnonHugePages_bytes Memory information field AnonHugePages_bytes.  
> node_memory_AnonPages_bytes Memory information field AnonPages_bytes.  
> node_memory_Bounce_bytes Memory information field Bounce_bytes.  
> node_memory_Buffers_bytes Memory information field Buffers_bytes.  
> node_memory_Cached_bytes Memory information field Cached_bytes.  
> node_memory_CmaFree_bytes Memory information field CmaFree_bytes.  
> node_memory_CmaTotal_bytes Memory information field CmaTotal_bytes.  
> node_memory_CommitLimit_bytes Memory information field CommitLimit_bytes.  
> node_memory_Committed_AS_bytes Memory information field Committed_AS_bytes.  
> node_memory_DirectMap2M_bytes Memory information field DirectMap2M_bytes.  
> node_memory_DirectMap4k_bytes Memory information field DirectMap4k_bytes.  
> node_memory_Dirty_bytes Memory information field Dirty_bytes.  
> node_memory_FileHugePages_bytes Memory information field FileHugePages_bytes.  
> node_memory_FilePmdMapped_bytes Memory information field FilePmdMapped_bytes.  
> node_memory_HardwareCorrupted_bytes Memory information field HardwareCorrupted_bytes.  
> node_memory_HugePages_Free Memory information field HugePages_Free.  
> node_memory_HugePages_Rsvd Memory information field HugePages_Rsvd.  
> node_memory_HugePages_Surp Memory information field HugePages_Surp.  
> node_memory_HugePages_Total Memory information field HugePages_Total.  
> node_memory_Hugepagesize_bytes Memory information field Hugepagesize_bytes.  
> node_memory_Hugetlb_bytes Memory information field Hugetlb_bytes.  
> node_memory_Inactive_anon_bytes Memory information field Inactive_anon_bytes.  
> node_memory_Inactive_bytes Memory information field Inactive_bytes.  
> node_memory_Inactive_file_bytes Memory information field Inactive_file_bytes.  
> node_memory_KReclaimable_bytes Memory information field KReclaimable_bytes.  
> node_memory_KernelStack_bytes Memory information field KernelStack_bytes.  
> node_memory_Mapped_bytes Memory information field Mapped_bytes.  
> node_memory_MemAvailable_bytes Memory information field MemAvailable_bytes.  
> node_memory_MemFree_bytes Memory information field MemFree_bytes.  
> node_memory_MemTotal_bytes Memory information field MemTotal_bytes.  
> node_memory_Mlocked_bytes Memory information field Mlocked_bytes.  
> node_memory_NFS_Unstable_bytes Memory information field NFS_Unstable_bytes.  
> node_memory_PageTables_bytes Memory information field PageTables_bytes.  
> node_memory_Percpu_bytes Memory information field Percpu_bytes.  
> node_memory_SReclaimable_bytes Memory information field SReclaimable_bytes.  
> node_memory_SUnreclaim_bytes Memory information field SUnreclaim_bytes.  
> node_memory_ShmemHugePages_bytes Memory information field ShmemHugePages_bytes.  
> node_memory_ShmemPmdMapped_bytes Memory information field ShmemPmdMapped_bytes.  
> node_memory_Shmem_bytes Memory information field Shmem_bytes.  
> node_memory_Slab_bytes Memory information field Slab_bytes.  
> node_memory_SwapCached_bytes Memory information field SwapCached_bytes.  
> node_memory_SwapFree_bytes Memory information field SwapFree_bytes.  
> node_memory_SwapTotal_bytes Memory information field SwapTotal_bytes.  
> node_memory_Unevictable_bytes Memory information field Unevictable_bytes.  
> node_memory_VmallocChunk_bytes Memory information field VmallocChunk_bytes.  
> node_memory_VmallocTotal_bytes Memory information field VmallocTotal_bytes.  
> node_memory_VmallocUsed_bytes Memory information field VmallocUsed_bytes.  
> node_memory_WritebackTmp_bytes Memory information field WritebackTmp_bytes.  
> node_memory_Writeback_bytes Memory information field Writeback_bytes.  
> curl http://localhost:9100/metrics 2> /dev/null | grep ^go_memstats  
> 
> node_disk_discard_time_seconds_total This is the total number of seconds spent by all discards.  
> node_disk_discarded_sectors_total The total number of sectors discarded successfully.  
> node_disk_discards_completed_total The total number of discards completed successfully.  
> node_disk_discards_merged_total The total number of discards merged.  
> node_disk_info Info of /sys/block/<block_device>.  
> node_disk_io_now The number of I/Os currently in progress.  
> node_disk_io_time_seconds_total Total seconds spent doing I/Os.  
> node_disk_io_time_weighted_seconds_total The weighted # of seconds spent doing I/Os.  
> node_disk_read_bytes_total The total number of bytes read successfully.  
> node_disk_read_time_seconds_total The total number of seconds spent by all reads.  
> node_disk_reads_completed_total The total number of reads completed successfully.  
> node_disk_reads_merged_total The total number of reads merged.  
> node_disk_write_time_seconds_total This is the total number of seconds spent by all writes.  
> node_disk_writes_completed_total The total number of writes completed successfully.  
> node_disk_writes_merged_total The number of writes merged.  
> node_disk_written_bytes_total The total number of bytes written successfully.  
> curl http://localhost:9100/metrics 2> /dev/null | grep ^node_disk  
> 
> node_network_address_assign_type address_assign_type value of /sys/class/net/<iface>.  
> node_network_carrier carrier value of /sys/class/net/<iface>.  
> node_network_carrier_changes_total carrier_changes_total value of /sys/class/net/<iface>.  
> node_network_carrier_down_changes_total carrier_down_changes_total value of /sys/class/net/<iface>.  
> node_network_carrier_up_changes_total carrier_up_changes_total value of /sys/class/net/<iface>.  
> node_network_device_id device_id value of /sys/class/net/<iface>.  
> node_network_dormant dormant value of /sys/class/net/<iface>.  
> node_network_flags flags value of /sys/class/net/<iface>.  
> node_network_iface_id iface_id value of /sys/class/net/<iface>.  
> node_network_iface_link iface_link value of /sys/class/net/<iface>.  
> node_network_iface_link_mode iface_link_mode value of /sys/class/net/<iface>.  
> node_network_info Non-numeric data from /sys/class/net/<iface>, value is always 1.  
> node_network_mtu_bytes mtu_bytes value of /sys/class/net/<iface>.  
> node_network_net_dev_group net_dev_group value of /sys/class/net/<iface>.  
> node_network_protocol_type protocol_type value of /sys/class/net/<iface>.  
> node_network_receive_bytes_total Network device statistic receive_bytes.  
> node_network_receive_compressed_total Network device statistic receive_compressed.  
> node_network_receive_drop_total Network device statistic receive_drop.  
> node_network_receive_errs_total Network device statistic receive_errs.  
> node_network_receive_fifo_total Network device statistic receive_fifo.  
> node_network_receive_frame_total Network device statistic receive_frame.  
> node_network_receive_multicast_total Network device statistic receive_multicast.  
> node_network_receive_packets_total Network device statistic receive_packets.  
> node_network_speed_bytes speed_bytes value of /sys/class/net/<iface>.  
> node_network_transmit_bytes_total Network device statistic transmit_bytes.  
> node_network_transmit_carrier_total Network device statistic transmit_carrier.  
> node_network_transmit_colls_total Network device statistic transmit_colls.  
> node_network_transmit_compressed_total Network device statistic transmit_compressed.  
> node_network_transmit_drop_total Network device statistic transmit_drop.  
> node_network_transmit_errs_total Network device statistic transmit_errs.  
> node_network_transmit_fifo_total Network device statistic transmit_fifo.  
> node_network_transmit_packets_total Network device statistic transmit_packets.  
> node_network_transmit_queue_length transmit_queue_length value of /sys/class/net/<iface>.  
> node_network_up Value is 1 if operstate is 'up', 0 otherwise.  
> curl http://localhost:9100/metrics 2> /dev/null | grep ^node_network  

**3. Ознакомьтесь с метриками, которые по умолчанию собираются Netdata и с комментариями, которые даны к этим метрикам.**  
> Every second, Netdata collects 1 301 metrics on vagrant, presents them in 227 charts and monitors them with 101 alarms.  
> netdata v1.19.0  

**4. Можно ли по выводу dmesg понять, осознает ли ОС, что загружена не на настоящем оборудовании, а на системе виртуализации?**  
> Согласно http://manpages.ubuntu.com/manpages/focal/man1/systemd-detect-virt.1.html  
> systemd умеет распознавать запуск в вируальной среде:  
> systemd-detect-virt  
> oracle  
> Если система загружена недавно, соответствующая запись есть в dmesg  
> dmesg | grep oracle  
> [   11.779740] systemd[1]: Detected virtualization oracle.  

**5. Как настроен sysctl fs.nr_open на системе по-умолчанию? Узнайте, что означает этот параметр.  
Какой другой существующий лимит не позволит достичь такого числа?**  
> sysctl -a 2> /dev/null | grep fs.nr_open  
> fs.nr_open = 1048576  
> Согласно https://www.kernel.org/doc/Documentation/sysctl/fs.txt  
> Этот параметр определяет системное ограничение на количество открытых дескрипторов.  
> Ограничения для ресурсов, доступных для оболочки и порождённых её процессов показывает:  
> ulimit --help | grep 'open file'  
> -n        the maximum number of open file descriptors  
> ulimit -n  
> 1024  

**6. Покажите, что ваш процесс работает под PID 1 через nsenter.**  
> screen  
> unshare -f --pid --mount-proc /bin/sleep 1h  
> ps aux | grep sleep  
> root        2667  0.0  0.0   8080   592 pts/3    S+   14:53   0:00 unshare -f --pid --mount-proc /bin/sleep 1h  
> root        2668  0.0  0.0   8076   592 pts/3    S+   14:53   0:00 /bin/sleep 1h  
> root        2670  0.0  0.0   8900   736 pts/0    S+   14:54   0:00 grep --color=auto sleep  
> nsenter --target 2668 --pid --mount  
> root@vagrant:/# ps aux  
> USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND  
> root           1  0.0  0.0   8076   592 pts/3    S+   14:53   0:00 /bin/sleep 1h  
> root           2  0.0  0.4   9836  4088 pts/0    S    14:54   0:00 -bash  
> root          11  0.0  0.3  11492  3320 pts/0    R+   14:54   0:00 ps aux  

**7. Найдите информацию о том, что такое :(){ :|:& };:.  
Какой механизм помог автоматической стабилизации.  
Как настроен этот механизм по-умолчанию, и как изменить число процессов, которое можно создать в сессии?**  
> Это однострочная запись функции, вызывающей саму себя в нескольки экземлярах. Форк-бомба.  
> dmesg -C  
> dmesg  
> cgroup: fork rejected by pids controller in /user.slice/user-1000.slice/session-14.scope  

> Существует механизм, ограничивающий кол-во одновременно запущенных процессов.  
> Увидеть ограничение на количество процессов для пользовательского слоя можно командой:   
> systemctl status user-1000.slice  
> Tasks: 7 (limit: 2356)  
> Эту величину можно изменить в файле /usr/lib/systemd/system/user-.slice.d/10-defaults.conf в поле TasksMax  
> Также ограничением на поличество процессов можно управлять с помощью утилиты ulimit  
> ulimit -u  
> 3571  
> с правами пользователя можно только уменьшить количество процессов для текущей сессии:  
> ulimit -u 3500  
> с правами суперпользователя можно увеличить эту величину для текущей сессии:  
> limit -u 3600  
> для всех пользователей (или какого-то конкретного) постоянное ограничение можно установить в файле /etc/security/limits.conf  
```
*               soft    nproc           3600
*               hard    nproc           3600
```