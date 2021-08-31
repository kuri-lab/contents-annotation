# contents-annotation

画像の印象を付与するアノテーションツール

## docker

tsugaikeにすでにあるものを使用する。コンテナの作成(nameは自分で指定する。)
```
nvidia-docker run -it -v `pwd`:/workspace/sample --net=host --shm-size 8G --name annotation annotation:gpu
```

## How to start the server

```
% python run.py
```
access to http://192.168.101.7/:8000/top


## others
### jupyterlabの起動
```
cd /workspace/sample/
jupyter lab --allow-root --ip=* --no-browser
```


#### check the database
```
% sqlite3 models/impression.db
sqlite> Select * from impressioncontents;
```

#### Initialize databases　
```
% python
>>> from models.database import init_db
>>> init_db()
>>> exit()
```

