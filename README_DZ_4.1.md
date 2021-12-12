**1. Какие значения переменным c,d,e будут присвоены? Почему?**  
| Переменная  | Значение | Обоснование |  
| --- | --- | --- |  
| `c` | a+b | Переменная определяется как строка последовательностью символов a+b |  
| `d` | 1+2 | Тип переменных a и b определяется как строковый, переменная c получается конкатенацией значений переменных a, b и символа "+" |  
| `e` | 3 | Bash интерпретирует выражение  $((expression)) как арифметическое. Arithmetic expansion allows the evaluation of an arithmetic expression and the substitution of the result.  The format for arithmetic expansion is: $((expression)) |  

**2.1 Что необходимо сделать, чтобы его исправить?**  
> Нудно в первой строке установить вторую закрывающую скобку:  
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