**1. В ответе укажите полученный HTTP код, что он означает?**  
> HTTP/1.1 301 Moved Permanently  
> Код 301 означает, что запрошенный ресурс был на постоянной основе перемещён в новое месторасположение, и указывающий на то, что текущие ссылки, использующие данный URL, должны быть обновлены.  

**2.1 Найдите первый ответ HTTP сервера, откройте вкладку Headers. Укажите в ответе полученный HTTP код.**  
```
scheme: http
host: stackoverflow.com
filename: /
Адрес: 151.101.1.69:80
Состояние: 301 Moved Permanently
Версия: HTTP/1.1
Передано: 51,70 КБ (размер 172,83 КБ)
```
**2.2 Проверьте время загрузки страницы, какой запрос обрабатывался дольше всего?**  
```
scheme: https
host: stackoverflow.com
filename: /
Адрес: 151.101.129.69:443
Состояние: 200 OK
Версия: HTTP/2
Передано: 51,74 КБ (размер 172,83 КБ)
```
```
В очереди: 358 мс Начато: 358 мс Загружено: 592 мс
Тайминг запроса
Заблокировано: 0 мс
Поиск DNS: 1 мс
Соединение: 35 мс
Установка TLS: 65 мс
Отправка: 0 мс
Ожидание: 132 мс
Получение: 0 мс
```
**2.3 Приложите скриншот консоли браузера в ответ.**  
![stackoverflow](img/stackoverflow.png)  

**3. Какой IP адрес у вас в интернете?**  
> Нам разрешили не сообщать реальный IP адрес, поэтому только 1й и 2й октет. Использовался сайт: https://whoer.net/ru  
> 93.123.000.000  

**4. Какому провайдеру принадлежит ваш IP адрес? Какой автономной системе AS?**  
> route:          93.123.224.0/21  
> descr:          INFFIN-NET  
> origin:         AS35539  

**5. Через какие сети проходит пакет, отправленный с вашего компьютера на адрес 8.8.8.8? Через какие AS?**  
> traceroute -nAI 8.8.8.8  
```
 1  10.0.2.2 [*]  0.318 ms  0.248 ms  0.191 ms
 2  192.168.3.1 [AS65190]  1.386 ms  1.764 ms  1.709 ms
 3  93.123.*.* [AS35539]  3.003 ms  4.054 ms  3.999 ms
 4  93.123.*.* [AS35539]  3.942 ms  3.888 ms  3.556 ms
 5  93.123.*.* [AS35539]  5.197 ms  5.143 ms  5.077 ms
 6  93.123.*.* [AS35539]  5.021 ms  4.462 ms  4.326 ms
 7  93.123.*.* [AS35539]  4.199 ms  6.388 ms  6.276 ms
 8  72.14.197.189 [AS15169]  6.886 ms  6.588 ms  6.477 ms
 9  * * 108.170.250.33 [AS15169]  7.886 ms
10  108.170.250.34 [AS15169]  6.578 ms  6.495 ms  6.415 ms
11  172.253.66.116 [AS15169]  40.971 ms  40.248 ms  21.948 ms
12  72.14.235.69 [AS15169]  21.741 ms  21.652 ms  22.668 ms
13  216.239.42.23 [AS15169]  23.153 ms  23.025 ms  24.088 ms
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * * *
21  * * *
22  * * *
23  8.8.8.8 [AS15169]  20.387 ms  22.316 ms  22.145 ms
```
> Пакет идёт через AS35539 (мой провайдер) и AS15169 (Google)  
> AS65190 - приватная система.

**6. Повторите задание 5 в утилите mtr. На каком участке наибольшая задержка - delay?**  
> mtr -n 8.8.8.8
```
Keys:  Help   Display mode   Restart statistics   Order of fields   quit
                                     Packets               Pings
 Host                              Loss%   Snt   Last   Avg  Best  Wrst StDev
 1. 10.0.2.2                        0.0%    64    1.2   1.1   0.4   2.5   0.4
 2. 192.168.3.1                     0.0%    63    4.7   3.0   1.7   8.4   1.3
 3. 93.123.*.*                      0.0%    63    8.7  12.7   2.1 116.5  16.6
 4. 93.123.*.*                      0.0%    63    3.3   5.0   2.1  22.7   4.2
 5. 93.123.*.*                      0.0%    63    4.0   6.1   2.9  22.8   4.3
 6. 93.123.*.*                      0.0%    63    3.7   5.9   3.4  24.3   3.9
 7. 93.123.*.*                      0.0%    63    3.3   8.5   3.1  45.5   9.9
 8. 72.14.197.189                   0.0%    63    4.6   6.0   3.9  23.4   3.6
 9. 108.170.250.33                 59.7%    63    5.9   7.0   4.5  24.3   4.8
10. 108.170.250.34                  0.0%    63    4.5   5.9   4.1  26.1   3.3
11. 172.253.66.116                  0.0%    63   21.0  22.2  19.3  44.0   5.2
12. 72.14.235.69                    0.0%    63   23.2  23.8  21.3  44.8   4.8
13. 216.239.42.23                   0.0%    63   25.0  24.7  21.5  49.1   5.2
14. (waiting for reply)
15. (waiting for reply)
16. (waiting for reply)
17. (waiting for reply)
18. (waiting for reply)
19. (waiting for reply)
20. (waiting for reply)
21. (waiting for reply)
22. (waiting for reply)
23. 8.8.8.8                        12.7%    63   22.9  22.1  18.1  39.8   5.0
```
> Среднее время ответа на Ping (Avg) больше всех у хоста 216.239.42.23  

**7. Какие DNS сервера отвечают за доменное имя dns.google? Какие A записи?**  
```commandline
vagrant@vagrant:~$ dig NS +short dns.google
ns2.zdns.google.
ns1.zdns.google.
ns3.zdns.google.
ns4.zdns.google.
vagrant@vagrant:~$ dig A +short dns.google
8.8.4.4
8.8.8.8
vagrant@vagrant:~$ dig A +short ns1.zdns.google
216.239.32.114
vagrant@vagrant:~$ dig A +short ns2.zdns.google
216.239.34.114
vagrant@vagrant:~$ dig A +short ns3.zdns.google
216.239.36.114
vagrant@vagrant:~$ dig A +short ns4.zdns.google
216.239.38.114
```
**8. Проверьте PTR записи для IP адресов из задания 7. Какое доменное имя привязано к IP?**  
```
vagrant@vagrant:~$ dig -x 8.8.4.4 +short
dns.google.
vagrant@vagrant:~$ dig -x 8.8.8.8 +short
dns.google.
vagrant@vagrant:~$ dig -x 216.239.32.114 +short
ns1.zdns.google.
vagrant@vagrant:~$ dig -x 216.239.34.114 +short
ns2.zdns.google.
vagrant@vagrant:~$ dig -x 216.239.36.114 +short
ns3.zdns.google.
vagrant@vagrant:~$ dig -x 216.239.38.114 +short
ns4.zdns.google.
```