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

**2. 