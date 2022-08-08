# Altair

### Rode esse comando para ativar o mongodb local para testes
```
docker-compose up -d
```
Para verificar se os containers estão rodando

```
docker container ls
```

Algo parecido com isso deve ser mostrado com a execução do comando acima

    CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS          PORTS                                 NAMES
    e5b27f080061   mongo-express   "tini -- /docker-ent…"   58 minutes ago   Up 58 minutes   0.0.0.0:8081->8081/tcp                mongo-express-altair
    f0a10df1e920   mongo           "docker-entrypoint.s…"   58 minutes ago   Up 58 minutes   0.0.0.0:27017->27017/tcp, 27018/tcp   altair_bd

### Depois para iniciar o servidor Django utilize o comando abaixo
```
python3 manage.py runserver
```
