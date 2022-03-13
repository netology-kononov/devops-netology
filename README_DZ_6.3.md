**1.1 Используя docker поднимите инстанс MySQL (версию 8). Данные БД сохраните в volume.**  
```yaml
version: '3.1'

volumes:
    db-data-mysql:
    
services:
    mydb:
        image: mysql:8.0.28
        restart: always
        command: --default-authentication-plugin=mysql_native_password
        volumes:
            - db-data-mysql:/var/lib/mysql
        ports: 
            - "3306:3306"
        environment:
            - MYSQL_ROOT_PASSWORD=mysecretpassword
```
**1.2 Изучите бэкап БД и восстановитесь из него.**  
> Создана соответствующая база в СУБД:  
```text
CREATE DATABASE test_db;
```
> Дамп базы был модифицирован, добавлена команда:  
```text
USE test_db;
```
```commandline
mysql -uroot -p -h 127.0.0.1 < test_dump_modified.sql
```
**1.3 Найдите команду для выдачи статуса БД и приведите в ответе из ее вывода версию сервера БД.**  
```text
mysql> \s
--------------
mysql  Ver 8.0.28-0ubuntu0.20.04.3 for Linux on x86_64 ((Ubuntu))

Connection id:          18
Current database:       test_db
Current user:           root@172.18.0.1
SSL:                    Cipher in use is TLS_AES_256_GCM_SHA384
Current pager:          stdout
Using outfile:          ''
Using delimiter:        ;
Server version:         8.0.28 MySQL Community Server - GPL
Protocol version:       10
Connection:             127.0.0.1 via TCP/IP
Server characterset:    utf8mb4
Db     characterset:    utf8mb4
Client characterset:    utf8mb4
Conn.  characterset:    utf8mb4
TCP port:               3306
Binary data as:         Hexadecimal
Uptime:                 30 min 33 sec

Threads: 2  Questions: 92  Slow queries: 0  Opens: 179  Flush tables: 3  Open tables: 97  Queries per second avg: 0.050
--------------
```
**1.4 Приведите в ответе количество записей с price > 300.**  
```text
mysql> SELECT count(*) FROM orders WHERE price > 300;
+----------+
| count(*) |
+----------+
|        1 |
+----------+
```
**2.1 Создайте пользователя test в БД c паролем test-pass.**  
```text
mysql> CREATE USER 'test'@'localhost' IDENTIFIED WITH mysql_native_password BY 'test-pass'
    -> WITH MAX_QUERIES_PER_HOUR 100
    -> PASSWORD EXPIRE INTERVAL 180 DAY
    -> FAILED_LOGIN_ATTEMPTS 3
    -> ATTRIBUTE '{"fname": "James", "lname": "Pretty"}';
Query OK, 0 rows affected (0.01 sec)
```
**2.2 Предоставьте привелегии пользователю test на операции SELECT базы test_db.**  
```text
mysql> GRANT SELECT ON test_db.* TO 'test'@'localhost';
Query OK, 0 rows affected, 1 warning (0.01 sec)
```
**2.3 Используя таблицу INFORMATION_SCHEMA.USER_ATTRIBUTES получите данные по пользователю test.**  
```text
mysql> SELECT * FROM USER_ATTRIBUTES WHERE USER = 'test';
+------+-----------+---------------------------------------+
| USER | HOST      | ATTRIBUTE                             |
+------+-----------+---------------------------------------+
| test | localhost | {"fname": "James", "lname": "Pretty"} |
+------+-----------+---------------------------------------+
```
**3.1 Исследуйте, какой engine используется в таблице БД test_db.**  
```text
mysql> SELECT table_name, table_schema, engine FROM information_schema.tables WHERE table_schema = 'test_db';
+------------+--------------+--------+
| TABLE_NAME | TABLE_SCHEMA | ENGINE |
+------------+--------------+--------+
| orders     | test_db      | InnoDB |
+------------+--------------+--------+
```
**3.2 Измените engine и приведите время выполнения и запрос на изменения из профайлера.**  
```text
mysql> SHOW PROFILES;
+----------+------------+-------------------------------------------------------------------------------------------------------+
| Query_ID | Duration   | Query                                                                                                 |
+----------+------------+-------------------------------------------------------------------------------------------------------+
|       14 | 0.06005375 | ALTER TABLE orders ENGINE = MyISAM                                                                    |
|       15 | 0.06362325 | ALTER TABLE orders ENGINE = InnoDB                                                                    |
+----------+------------+-------------------------------------------------------------------------------------------------------+
```
**4. Приведите в ответе измененный файл my.cnf.**  
```text
[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
secure-file-priv= NULL

innodb_flush_log_at_trx_commit = 2
innodb_file_per_table = 1
innodb_log_buffer_size = 1M
innodb_buffer_pool_size = 30
innodb_log_file_size = 100M

# Custom config should go here
!includedir /etc/mysql/conf.d/
```