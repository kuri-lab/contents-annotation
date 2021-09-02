# contents-annotation

画像の印象を付与するアノテーションツール

## docker

tsugaikeにすでにあるものを使用する。コンテナの作成(nameは自分で指定する。)
```
nvidia-docker run -it -v `pwd`:/workspace/sample --net=host --shm-size 8G --name annotation annotation:gpu
```

## How to start the server

```
python run.py
```
access to http://192.168.101.7:8000/top

## app/templates
app/templates/Image に表示する画像を入れているが、gitignoreしている。表示している画像は以下のデータセット。
* 手塚データセットは、[link](https://keio.app.box.com/s/s3pbq6na714vbbsh4hjuje267agrb74k). 
* DomainNetのSketchは、[link](http://ai.bu.edu/M3SDA/). 

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

