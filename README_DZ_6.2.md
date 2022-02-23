**1. Приведите получившуюся команду или docker-compose манифест.**  
```yaml
version: '3.1'

volumes:
    db-data:
    db-backup:
    
services:
    mydb:
        image: postgres:12.10-alpine
        restart: always
        volumes:
            - db-data:/var/lib/postgresql/data
            - db-backup:/var/lib/postgresql/backup
        ports: 
            - "5432:5432"
        environment:
            - POSTGRES_PASSWORD=mysecretpassword
```

**2.1 Приведите итоговый список БД**  
```commandline
test_db=# \l
                                     List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |       Access privileges
-----------+----------+----------+------------+------------+--------------------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres                   +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres                   +
           |          |          |            |            | postgres=CTc/postgres
 test_db   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =Tc/postgres                  +
           |          |          |            |            | postgres=CTc/postgres         +
           |          |          |            |            | "test-admin-user"=CTc/postgres
(4 rows)
```
**2.2 Приведите описание таблиц (describe)**  
```commandline
test_db=# \dt+
                      List of relations
 Schema |  Name   | Type  |  Owner   |  Size   | Description
--------+---------+-------+----------+---------+-------------
 public | clients | table | postgres | 0 bytes |
 public | orders  | table | postgres | 0 bytes |
(2 rows)

test_db=# \d+ clients
                                                             Table "public.clients"
      Column       |         Type          | Collation | Nullable |               Default               | Storage  | Stats target | Description
-------------------+-----------------------+-----------+----------+-------------------------------------+----------+--------------+-------------
 id                | integer               |           | not null | nextval('clients_id_seq'::regclass) | plain    |              |
 фамилия           | character varying(40) |           |          |                                     | extended |              |
 страна проживания | character varying(40) |           |          |                                     | extended |              |
 заказ             | integer               |           |          |                                     | plain    |              |
Indexes:
    "clients_pkey" PRIMARY KEY, btree (id)
    "i_country" btree ("страна проживания")
Foreign-key constraints:
    "заказ" FOREIGN KEY (id) REFERENCES orders(id)
Access method: heap

test_db=# \d+ orders
                                                          Table "public.orders"
    Column    |         Type          | Collation | Nullable |              Default               | Storage  | Stats target | Description
--------------+-----------------------+-----------+----------+------------------------------------+----------+--------------+-------------
 id           | integer               |           | not null | nextval('orders_id_seq'::regclass) | plain    |              |
 наименование | character varying(40) |           |          |                                    | extended |              |
 цена         | integer               |           |          |                                    | plain    |              |
Indexes:
    "orders_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "clients" CONSTRAINT "заказ" FOREIGN KEY (id) REFERENCES orders(id)
Access method: heap
```
**2.3 Приведите SQL-запрос для выдачи списка пользователей с правами над таблицами test_db**  
> SELECT * FROM information_schema.role_table_grants WHERE table_catalog='test_db' AND table_schema='public';  

**2.4 Приведите список пользователей с правами над таблицами test_db**  
```commandline
 grantor  |     grantee      | table_catalog | table_schema | table_name | privilege_type | is_grantable | with_hierarchy
----------+------------------+---------------+--------------+------------+----------------+--------------+----------------
 postgres | postgres         | test_db       | public       | clients    | INSERT         | YES          | NO
 postgres | postgres         | test_db       | public       | clients    | SELECT         | YES          | YES
 postgres | postgres         | test_db       | public       | clients    | UPDATE         | YES          | NO
 postgres | postgres         | test_db       | public       | clients    | DELETE         | YES          | NO
 postgres | postgres         | test_db       | public       | clients    | TRUNCATE       | YES          | NO
 postgres | postgres         | test_db       | public       | clients    | REFERENCES     | YES          | NO
 postgres | postgres         | test_db       | public       | clients    | TRIGGER        | YES          | NO
 postgres | test-admin-user  | test_db       | public       | clients    | INSERT         | NO           | NO
 postgres | test-admin-user  | test_db       | public       | clients    | SELECT         | NO           | YES
 postgres | test-admin-user  | test_db       | public       | clients    | UPDATE         | NO           | NO
 postgres | test-admin-user  | test_db       | public       | clients    | DELETE         | NO           | NO
 postgres | test-admin-user  | test_db       | public       | clients    | TRUNCATE       | NO           | NO
 postgres | test-admin-user  | test_db       | public       | clients    | REFERENCES     | NO           | NO
 postgres | test-admin-user  | test_db       | public       | clients    | TRIGGER        | NO           | NO
 postgres | test-simple-user | test_db       | public       | clients    | INSERT         | NO           | NO
 postgres | test-simple-user | test_db       | public       | clients    | SELECT         | NO           | YES
 postgres | test-simple-user | test_db       | public       | clients    | UPDATE         | NO           | NO
 postgres | test-simple-user | test_db       | public       | clients    | DELETE         | NO           | NO
 postgres | postgres         | test_db       | public       | orders     | INSERT         | YES          | NO
 postgres | postgres         | test_db       | public       | orders     | SELECT         | YES          | YES
 postgres | postgres         | test_db       | public       | orders     | UPDATE         | YES          | NO
 postgres | postgres         | test_db       | public       | orders     | DELETE         | YES          | NO
 postgres | postgres         | test_db       | public       | orders     | TRUNCATE       | YES          | NO
 postgres | postgres         | test_db       | public       | orders     | REFERENCES     | YES          | NO
 postgres | postgres         | test_db       | public       | orders     | TRIGGER        | YES          | NO
 postgres | test-admin-user  | test_db       | public       | orders     | INSERT         | NO           | NO
 postgres | test-admin-user  | test_db       | public       | orders     | SELECT         | NO           | YES
 postgres | test-admin-user  | test_db       | public       | orders     | UPDATE         | NO           | NO
 postgres | test-admin-user  | test_db       | public       | orders     | DELETE         | NO           | NO
 postgres | test-admin-user  | test_db       | public       | orders     | TRUNCATE       | NO           | NO
 postgres | test-admin-user  | test_db       | public       | orders     | REFERENCES     | NO           | NO
 postgres | test-admin-user  | test_db       | public       | orders     | TRIGGER        | NO           | NO
 postgres | test-simple-user | test_db       | public       | orders     | INSERT         | NO           | NO
 postgres | test-simple-user | test_db       | public       | orders     | SELECT         | NO           | YES
 postgres | test-simple-user | test_db       | public       | orders     | UPDATE         | NO           | NO
 postgres | test-simple-user | test_db       | public       | orders     | DELETE         | NO           | NO
(36 rows)
```
**3. Вычислите количество записей для каждой таблицы. Приведите в ответе: запросы, результаты их выполнения.**  
```commandline
test_db=# SELECT count(*) FROM clients;
 count
-------
     5
(1 row)

test_db=# SELECT count(*) FROM orders;
 count
-------
     5
(1 row)
```
**4.1 Используя foreign keys свяжите записи из таблиц. Приведите SQL-запросы для выполнения данных операций**  
> UPDATE clients SET "заказ" = (SELECT ID FROM orders WHERE "наименование"='Книга') WHERE "фамилия"='Иванов Иван Иванович';  
> UPDATE clients SET "заказ" = (SELECT ID FROM orders WHERE "наименование"='Монитор') WHERE "фамилия"='Петров Петр Петрович';  
> UPDATE clients SET "заказ" = (SELECT ID FROM orders WHERE "наименование"='Гитара') WHERE "фамилия"='Иоганн Себастьян Бах';  

**4.2 Приведите SQL-запрос для выдачи всех пользователей, которые совершили заказ, а также вывод данного запроса**  
```commandline
test_db=# SELECT "фамилия" FROM clients INNER JOIN orders ON clients."заказ" = orders.ID;
       фамилия
----------------------
 Иванов Иван Иванович
 Петров Петр Петрович
 Иоганн Себастьян Бах
(3 rows)
```
**5. Приведите получившийся результат и объясните что значат полученные значения**  
```commandline
test_db=# EXPLAIN SELECT "фамилия" FROM clients INNER JOIN orders ON clients."заказ" = orders.ID;
                             QUERY PLAN
---------------------------------------------------------------------
 Hash Join  (cost=23.50..37.93 rows=350 width=98)
   Hash Cond: (clients."заказ" = orders.id)
   ->  Seq Scan on clients  (cost=0.00..13.50 rows=350 width=102)
   ->  Hash  (cost=16.00..16.00 rows=600 width=4)
         ->  Seq Scan on orders  (cost=0.00..16.00 rows=600 width=4)
(5 rows)
```
> "Hash Join" означает, что планировщик выбирает соединение по хешу, при котором строки одной таблицы записываются в хеш-таблицу 
> в памяти, после чего сканируется другая таблица и для каждой её строки проверяется соответствие по хеш-таблице.  
> "Seq Scan" означает, что выбран план простого последовательного сканирования.  
> "Hash" означает операцию конструирования хеш-таблицы.  
> Значения в скобках после "cost" означают:  
> Приблизительная стоимость запуска. Это время, которое проходит, прежде чем начнётся этап вывода данных.  
> Приблизительная общая стоимость. Она вычисляется в предположении, что узел плана выполняется до конца, то есть возвращает все доступные строки.  
> Ожидаемое число строк, которое должен вывести этот узел плана. При этом так же предполагается, что узел выполняется до конца.  
> Ожидаемый средний размер строк, выводимых этим узлом плана (в байтах).  
 
**6. Приведите список операций, который вы применяли для бэкапа данных и восстановления**  
```commandline
# pg_dump -U postgres -F t test_db > /var/lib/postgresql/backup/test_db.tar
# createdb -U postgres test_db
# pg_restore -U postgres --dbname=test_db --verbose /var/lib/postgresql/backup/test_db.tar
```
