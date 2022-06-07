**1.1 Текст Dockerfile манифеста**  
```text
FROM centos:7.9.2009

RUN yum install wget perl-Digest-SHA -y
RUN mkdir /usr/share/elasticsearch
WORKDIR /usr/share/elasticsearch
RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.2.2-linux-x86_64.tar.gz && \
    wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.2.2-linux-x86_64.tar.gz.sha512 && \
    shasum -a 512 -c elasticsearch-8.2.2-linux-x86_64.tar.gz.sha512 && \
    tar -xzf elasticsearch-8.2.2-linux-x86_64.tar.gz --strip-components=1 && \
    rm elasticsearch-8.2.2-linux-x86_64.tar.gz && \
    rm elasticsearch-8.2.2-linux-x86_64.tar.gz.sha512
COPY config/elasticsearch.yml config/
RUN useradd elasticsearch && \
    chown -R elasticsearch: /var/lib && \
    chown -R elasticsearch: /usr/share/elasticsearch
EXPOSE 9200 9300

CMD [ "./bin/elasticsearch" ]
USER elasticsearch
```
config/elasticsearch.yml
```yaml
node.name: netology_test
path.data: /var/lib
network.host: 0.0.0.0
xpack.security.enabled: false
discovery.type: single-node
```
**1.2 Ссылка на образ в репозитории dockerhub**  
> https://hub.docker.com/r/hintmy/netology-es  

**1.3 Ответ elasticsearch на запрос пути / в json виде**
```yaml
root@hv-temp:/netology/db_es# curl http://localhost:9200
{
  "name" : "netology_test",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "ZaWPFdulSS2Nla2DBTa0Kw",
  "version" : {
    "number" : "8.2.2",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "9876968ef3c745186b94fdabd4483e01499224ef",
    "build_date" : "2022-05-25T15:47:06.259735307Z",
    "build_snapshot" : false,
    "lucene_version" : "9.1.0",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

**2.1 Получите список индексов и их статусов, используя API и приведите в ответе на задание.**
```commandline
root@hv-temp:/netology/db_es/docker# curl -X GET "localhost:9200/_cat/indices?v"
health status index uuid                   pri rep docs.count docs.deleted store.size pri.store.size
yellow open   ind-3 KfEmkxMDSpOw34X_PR0KpA   4   2          0            0       900b           900b
yellow open   ind-2 3qekxifuSw2Vm4R-2vprVQ   2   1          0            0       450b           450b
green  open   ind-1 BhYCO_oHQrCWpDq3gF3cRw   1   0          0            0       225b           225b
```
**2.2 Получите состояние кластера elasticsearch, используя API. Как вы думаете, почему часть индексов и кластер находится в состоянии yellow?**
```json
root@hv-temp:/netology/db_es/docker# curl -X GET "localhost:9200/_cluster/health/" | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   403  100   403    0     0  33583      0 --:--:-- --:--:-- --:--:-- 33583
{
  "cluster_name": "elasticsearch",
  "status": "yellow",
  "timed_out": false,
  "number_of_nodes": 1,
  "number_of_data_nodes": 1,
  "active_primary_shards": 8,
  "active_shards": 8,
  "relocating_shards": 0,
  "initializing_shards": 0,
  "unassigned_shards": 10,
  "delayed_unassigned_shards": 0,
  "number_of_pending_tasks": 0,
  "number_of_in_flight_fetch": 0,
  "task_max_waiting_in_queue_millis": 0,
  "active_shards_percent_as_number": 44.44444444444444
}
```
> Полагаю, что состояние yellow связано с тем, что все реплики расположены на одной ноде, т.к. в кластере только одна нода.

**3.1 Приведите в ответе запрос API и результат вызова API для создания репозитория.**  
```commandline
root@hv-temp:/netology/db_es/docker# curl -X PUT "localhost:9200/_snapshot/netology_backup?pretty" -H 'Content-Type: application/json' -d'
> {
>   "type": "fs",
>   "settings": {
>     "location": "/usr/share/elasticsearch/snapshots"
>   }
> }
> '
{
  "acknowledged" : true
}
```

**3.2 Приведите в ответе список индексов.**
```commandline
root@hv-temp:/netology/db_es/docker# curl -X GET "localhost:9200/_cat/indices?v"
health status index uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test  d9qqFoJyTF6-5Jw2hbs1EA   1   0          0            0       225b           225b
```

**3.3 Приведите в ответе список файлов в директории со snapshotами.**
```commandline
[elasticsearch@7a2b61cac82e elasticsearch]$ ls -la snapshots/
total 48
drwxr-xr-x 3 elasticsearch elasticsearch  4096 Jun  7 21:17 .
drwxr-xr-x 1 elasticsearch elasticsearch  4096 Jun  7 20:59 ..
-rw-r--r-- 1 elasticsearch elasticsearch   846 Jun  7 21:17 index-0
-rw-r--r-- 1 elasticsearch elasticsearch     8 Jun  7 21:17 index.latest
drwxr-xr-x 4 elasticsearch elasticsearch  4096 Jun  7 21:17 indices
-rw-r--r-- 1 elasticsearch elasticsearch 18282 Jun  7 21:17 meta-e9RDxw3DSKCjfgohJxO5UQ.dat
-rw-r--r-- 1 elasticsearch elasticsearch   350 Jun  7 21:17 snap-e9RDxw3DSKCjfgohJxO5UQ.dat
```

**3.4 Приведите в ответе список индексов.**
```commandline
root@hv-temp:/netology/db_es/docker# curl -X GET "localhost:9200/_cat/indices?v"
health status index  uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test-2 aIreBh-tQSqUIAoZQM8vXA   1   0          0            0       225b           225b
```

**3.5 Приведите в ответе запрос к API восстановления и итоговый список индексов.**
```commandline
root@hv-temp:/netology/db_es/docker# curl -X POST "localhost:9200/_snapshot/netology_backup/test_snapshot/_restore?pretty" -H 'Content-Type: application/json' -d'
> {
>   "indices": "test"
> }
> '
{
  "accepted" : true
}
root@hv-temp:/netology/db_es/docker# curl -X GET "localhost:9200/_cat/indices?v"
health status index  uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test-2 aIreBh-tQSqUIAoZQM8vXA   1   0          0            0       225b           225b
green  open   test   hED3CP_ZSESPE_r5vJT0wA   1   0          0            0       225b           225b
```