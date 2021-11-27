**1. Какой системный вызов делает команда cd?**  
>strace /bin/bash -c 'cd /tmp' 2>&1 | grep tmp  
stat("/tmp", {st_mode=S_IFDIR|S_ISVTX|0777, st_size=4096, ...}) = 0  
chdir("/tmp") = 0  

**2. Используя strace выясните, где находится база данных file на основании которой она делает свои догадки.**  
>strace -e openat file /bin/bash  
>strace -e openat file /dev/tty  
>strace -e openat file /dev/sda  
Имеют общие открываемые файлы (за исключением файлов библиотек):  
>openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3  
>openat(AT_FDCWD, "/etc/magic.mgc", O_RDONLY) = -1 ENOENT (No such file or directory)  
>openat(AT_FDCWD, "/etc/magic", O_RDONLY) = 3  
>openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3  
Файл /etc/magic.mgc не существует, файл /etc/magic пустой,  
/etc/ld.so.cache - динамический линкер,  
/usr/share/misc/magic.mgc - видимо, искомая база.  

**3. Предложите способ обнуления открытого удаленного файла.**  
>Нужно передать приложению сигнал USR1 для переоткрытия файла логов.  
>kill -USR1 $pid  

**4. Занимают ли зомби-процессы какие-то ресурсы в ОС (CPU, RAM, IO)?**  
>Нет.  

**5. На какие файлы вы увидели вызовы группы open за первую секунду работы утилиты?**  
>Открываются файлы в виртуальной файловой системе /proc  
>PID    COMM               FD ERR PATH  
1040   vmstats             5   0 /proc/meminfo  
1040   vmstats             5   0 /proc/stat  
591    irqbalance          6   0 /proc/interrupts  
591    irqbalance          6   0 /proc/stat  
591    irqbalance          6   0 /proc/irq/20/smp_affinity  
591    irqbalance          6   0 /proc/irq/0/smp_affinity  
591    irqbalance          6   0 /proc/irq/1/smp_affinity  
591    irqbalance          6   0 /proc/irq/8/smp_affinity  
591    irqbalance          6   0 /proc/irq/12/smp_affinity  
591    irqbalance          6   0 /proc/irq/14/smp_affinity  
591    irqbalance          6   0 /proc/irq/15/smp_affinity  
1      systemd            12   0 /proc/383/cgroup  

**6. Какой системный вызов использует uname -a? Приведите цитату из man по этому системному вызову, где описывается альтернативное местоположение в /proc, где можно узнать версию ядра и релиз ОС.**  
>Системный вызов:  
uname({sysname="Linux", nodename="vagrant", ...}) = 0  
>Цитата из man:  
Part of the utsname information is also accessible via /proc/sys/kernel/{ostype, hostname, osrelease, version, domainname}.  

**7. Чем отличается последовательность команд через ; и через && в bash?  
Есть ли смысл использовать в bash &&, если применить set -e?**  
>Разделитель команд && эквивалентен условному выполнению последующей команды, если предыдущая завершилась успешно
>Разделитель ; используется для безусловного выполнения последовательности команд.  
> 
>Параметр set -e определяет поведение оболочки при любом завершении команды в пайплайне, списке или составной команде, 
>иногда удобнее использовать разное поведение в последовательностях команд. Использовать && имеет смысл.  

**8. Из каких опций состоит режим bash set -euxo pipefail и почему его хорошо было бы использовать в сценариях?**  
>-e Завершает сценарий, если команда вернула ненулевой код.  
>-u Останавливает сценарий, если в нём присутствуют неопределённые переменные или параметры отличные от "@" и "*".  
>-x Отображает выполняемую команду, раскрывая имеющиеся преобразования.  
>-o pipefail Возвращает ненулевой значение самой правой команды в пайплайне, если оно есть.  
>Этот режим позволяет более безопасно выполнять сценарии и удобнее выявлять ошибки в них.  

**9. Определите, какой наиболее часто встречающийся статус у процессов в системе.**  
>ps -axo stat | grep S | wc -l  
61  
ps -axo stat | grep I | wc -l  
47  
ps -axo stat | grep R | wc -l  
1  
статус S - процесс в состоянии ожидания (sleeping).  
