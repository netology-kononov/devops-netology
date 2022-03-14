**1. Найдите и приведите управляющие команды.**  

| Задача                            | Команда         | 
|-----------------------------------|-----------------|
| Вывод списка БД                   | \l[+] [PATTERN] |
| Подключение к БД                  | \c[onnect]      |
| Вывод списка таблиц               | \d[S+] \dt[S+]  |
| Вывод описания содержимого таблиц | \d[S+] NAME     |
| Выход из psql                     | \q              |

**2. Используя таблицу pg_stats, найдите столбец таблицы orders с наибольшим средним значением размера элементов в байтах.
Приведите в ответе команду, которую вы использовали для вычисления и полученный результат.**  
```text
test_database=# SELECT attname, avg_width FROM pg_stats WHERE tablename = 'orders';
 attname | avg_width
---------+-----------
 id      |         4
 title   |        16
 price   |         4
(3 rows)
```
**3. Предложите SQL-транзакцию для проведения разбиения таблицы на 2 (шардировать на orders_1 - price>499 и orders_2 - price<=499). 
Можно ли было изначально исключить "ручное" разбиение при проектировании таблицы orders?**  
```text
CREATE TABLE orders_tmp as SELECT * FROM orders;
CREATE TABLE orders_1 (CHECK ( price > 499 )) INHERITS (orders);
CREATE TABLE orders_2 (CHECK ( price <= 499 )) INHERITS (orders);
DELETE FROM orders;
INSERT INTO orders_1 select * FROM orders_tmp where price > 499;
INSERT INTO orders_2 select * FROM orders_tmp where price <= 499;
DROP TABLE orders_tmp;
```
> Да, можно было создать таблицу orders как секционированную с соответствующими правилами или триггерными функциями для работы с секциями.  

**4. Как бы вы доработали бэкап-файл, чтобы добавить уникальность значения столбца title для таблиц test_database?**  
> В SQL сценарий нужно добавить директиву:
```text
UNIQUE(title)
```
> в каждую из таблиц, где существует поле 'title'. К сожалению, ограничение уникальности на наследуемых таблицах не наследуется.
> И более того, если указать уникальность поля для каждой шарды, указанное поле будет уникально только в пределах одной шарды, 
> а не для таблицы в целом. Это ограничение СУБД, согласно документации: 
> https://postgrespro.ru/docs/postgresql/13/ddl-inherit#DDL-INHERIT-CAVEATS
> 