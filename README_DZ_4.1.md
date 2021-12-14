**1. Какие значения переменным c,d,e будут присвоены? Почему?**  
| Переменная  | Значение | Обоснование |  
| --- | --- | --- |  
| `c` | a+b | Переменная определяется как строка последовательностью символов a+b |  
| `d` | 1+2 | Тип переменных a и b определяется как строковый, переменная c получается конкатенацией значений переменных a, b и символа "+" |  
| `e` | 3 | Bash интерпретирует выражение  $((expression)) как арифметическое. Цитата из man bash: Arithmetic expansion allows the evaluation of an arithmetic expression and the substitution of the result.  The format for arithmetic expansion is: $((expression)) |  

**2.1 Что необходимо сделать, чтобы его исправить?**  
> Нужно в первой строке установить вторую закрывающую скобку:  
> while ((1==1))  

**2.2 Необходимо написать скрипт.**  
```
#!/usr/bin/env bash
logfile=log
hosts=" 192.168.0.1 173.194.222.113 87.250.250.242 "
for i in {1..5}
do
        for host in $hosts
        do
                nc -v -w 1 $host 80 2>> $logfile
        done
done
```

**3. Необходимо дописать скрипт.**  
```
#!/usr/bin/env bash
logfile=log
errorfile=error
hosts=" 192.168.0.1 173.194.222.113 87.250.250.242 "
for i in {1..5}
do
        for host in $hosts
        do
                if ! nc -v -w 1 $host 80 2>> $logfile
                then
                        echo $host > $errorfile
                        break 2
                fi
        done
done
```

**4. Нужно написать локальный хук для git, который будет проверять, что сообщение в коммите содержит код текущего задания в квадратных скобках и количество символов в сообщении не превышает 30.**  
> vi .git/hooks/commit-msg  
> с синтаксисом bash:
```
#!/usr/bin/env bash

msg=$(cat $1)
if ! [[ "${msg}" =~ .*\[.+\].* ]]
then
        echo Incorrect format. Square brackets required. ${msg}
        exit 1
fi
if (( ${#msg} >= 30 ))
then
        echo Incorrect size. Less then 30 required. ${#msg}
        exit 2
fi
```
> с синтексисом POSIX:
```
#!/bin/sh

msg=$(cat $1)
if ! echo "${msg}" | grep -qP "\[.+\]"
then
        echo Incorrect format. Square brackets required. ${msg}
        exit 1
fi
if [ ${#msg} -ge 30 ]
then
        echo Incorrect size. Less then 30 required. ${#msg}
        exit 2
fi
```
> chmod +x commit-msg