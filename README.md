# contents-annotation

画像の印象を付与するアノテーションツール

## docker

tsugaikeにすでにあるものを使用する。以下のコードを実行することでコンテナを作成することができる。(nameは自分で指定する。)
```
nvidia-docker run -it -v `pwd`:/workspace/sample --net=host --shm-size 8G --name annotation annotation:gpu
'''
その後、以下のコードでjupyterlabを起動できる。
```
cd /workspace/sample/
jupyter lab --allow-root --ip=* --no-browser
```

## How to start the server

```
% python run.py
```
access to http://192.168.101.7/:8000/task/hypara_test


# check the database
```
% sqlite3 models/impression.db
sqlite> Select * from impressioncontents;
```

# Initialize databases　データベースの初期化
```
% python
>>> from models.database import init_db
>>> init_db()
>>> exit()
```

