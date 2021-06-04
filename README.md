Python & MySQL & MongoDB 環境をDockerで構築
====

<br />

# 環境構築

```
# dockerコンテナを起動
# scraipingを行うメインのコンテナ以外にmysqlとmondoDB合わせて3つのコンテナが起動する
# ローカルホスト直下にmondoディレクトリとmysqlディレクトリが生成される
# このレポジトリ直下はdockerコンテナにマウントされる
$ docker compose up -d


# python コンテナ内部へ入る
$ docker exec -it python /bin/bash

# mongo コンテナ内部へ入る
$ docker exec -it mongo_db /bin/bash

# mysql コンテナ内部へ入る
$ docker exec -it mysql_db /bin/bash
```

<br />

# python -> MySQL 接続

```
# mysql コンテナ内部へ入る
$ docker exec -it mysql_db /bin/bash

# root user でログイン
$ mysql -u root -p

# sample db を作成
mysql> CREATE DATABASE sample DEFAULT CHARACTER SET utf8mb4;

# db 作成を確認
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sample             |
| sys                |
+--------------------+

# python コンテナへ
$ docker exec -it python /bin/bash

# サンプルファイル実行、接続を確認
$ python src/mysql.py
('タンパベイ・レイズ', 'ア・東地区', 1)
('ニューヨーク・ヤンキース', 'ア・東地区', 2)
('ミネソタ・ツインズ', 'ア・中地区', 1)
('シカゴ・ホワイトソックス', 'ア・中地区', 2)
('オークランド・アスレチックス', 'ア・西地区', 1)
('ヒューストン・アストロズ', 'ア・西地区', 2)
```

<br />

# python -> mongoDB 接続

```
# python コンテナへ
$ docker exec -it python /bin/bash

# サンプルファイル実行、接続を確認
$ python src/mongo.py
{'_id': ObjectId('********'), 'name': 'アトランタ・ブレーブス', 'district': 'ナ・東地区', 'ranking_2020': 1}
{'_id': ObjectId('********'), 'name': 'フロリダ・マーリンズ', 'district': 'ナ・東地区', 'ranking_2020': 2}
{'_id': ObjectId('********'), 'name': 'シカゴ・カブス', 'district': 'ナ・中地区', 'ranking_2020': 1}
{'_id': ObjectId('********'), 'name': 'セントルイス・カージナルス', 'district': 'ナ・中地区', 'ranking_2020': 2}
{'_id': ObjectId('********'), 'name': 'ロサンゼルス・ドジャース', 'district': 'ナ・西地区', 'ranking_2020': 1}
{'_id': ObjectId('********'), 'name': 'サンディエゴ・パドレス', 'district': 'ナ・西地区', 'ranking_2020': 2}
```

<br />

# 補足
ホストのディレクトがマウントされているので、例えば下記のようにdockerコンテナ内に入ってコードを編集したり、DBを書き換えたりした場合、ホスト内のファイルも同様に変更される。
