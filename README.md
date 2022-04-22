# d-anime-mylist-backend

## 開発について

### 作業前に

.env を.env.sample をコピーしてルートディレクトリに作成してください。

```
$ cp .env.sample .env
```

### ポートの説明

`80` : API  
`3030` : phpMyAdmin

### API について

#### API の仕様

`/docs` : openapi(swagger)

#### フォーマット

```
$ docker exec -it d-anime-mylist-backend-web bash
コンテナ内 # black .
All done! ✨ 🍰 ✨
```

---

### データベース・テーブルについて

`server/app/models/mylist.py`に記載

`🔑`は主キー、複合主キーを示す。

#### `mylist` テーブル

| mylist_id🔑             | created_at             | updated_at             |
| ----------------------- | ---------------------- | ---------------------- |
| d-anime の mylist の id | カラムが作成された時間 | カラムが更新された時間 |

#### `mylistContents`テーブル

| mylist_id🔑             | anime_id🔑            |
| ----------------------- | --------------------- |
| d-anime の mylist の id | d-anime のアニメの id |

#### `animeInfo`テーブル

| anime_id🔑            | title            | image                        | url                               | first                 | stories      |
| --------------------- | ---------------- | ---------------------------- | --------------------------------- | --------------------- | ------------ |
| d-anime のアニメの id | アニメのタイトル | アニメのサムネイル画像の URL | アニメの詳細ページ(d-anime-store) | アニメ 1 話のタイトル | アニメの話数 |

#### データベースの作り方

```
$ docker exec -it d-anime-mylist-backend-web bash
コンテナ内 # python migrate.py
2022-03-22 09:10:13,777 INFO sqlalchemy.engine.Engine COMMIT
Create Table! ✨ 🍰 ✨
```

### テスト

テストの実行の方法

```
$ docker exec -it d-anime-mylist-backend-web bash
root@web-server:/app/api# cd ../test
root@web-server:/app/test# ./test.sh
```

**failed**の箇所は修正してください。

### 注意

**データベースのテーブルが上記の方法で作れない場合**や、**phpMyAdmin にエラーで入れない場合**は、db ディレクトリ直下の save_data を削除してください。

## ツール

[d-anime-mylist-scheduler](https://github.com/OHMORIYUSUKE/d-anime-mylist-scheduler)

DB の情報を更新するためのツールです。定期実行させることで、ユーザーが登録した d アニメストアのマイリストの状態を定期的に DB に更新させることができます。
