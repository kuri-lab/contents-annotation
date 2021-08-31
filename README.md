# contents-annotation

画像の印象を付与するアノテーションツール

## docker


```nvidia-docker run -it -v `pwd`:/workspace/sample --net=host --shm-size 8G --name annotation annotation:gpu'''


## Initialize databases　データベースの初期化

```
% python
>>> from models.database import init_db
>>> init_db()
>>> exit()
```

## How to start the server

```
% python run.py
```

access to http://localhost:8000/task/hypara_test


## check the database

```
% sqlite3 models/impression.db
sqlite> Select * from impressioncontents;
```
