# d-anime-mylist

## 開発について

### 作業前に

.env を.env.sample をコピーしてルートディレクトリに作成してください。

```
$ cp .env.sample .env
```

### ポートの説明

`8000` : API  
`3031` : phpMyAdmin

### API について

#### API の仕様

`/docs` : openapi(swagger)

#### フォーマット

```
$ docker exec -it d-anime-mylist-web-1 bash
コンテナ内 # pip install black
コンテナ内 # black .
All done! ✨ 🍰 ✨
```

---

### データベース・テーブルについて

`server/app/models/mylist.py`に記載

#### `mylist` テーブル

| id                      | created_at             | updated_at             |
| ----------------------- | ---------------------- | ---------------------- |
| d-anime の mylist の id | カラムが作成された時間 | カラムが更新された時間 |

#### `mylistContents`テーブル

| id                      | title                     | image                                 | url                                                   |
| ----------------------- | ------------------------- | ------------------------------------- | ----------------------------------------------------- |
| d-anime の mylist の id | mylist のアニメのタイトル | mylist のアニメのサムネイル画像のパス | mylist のアニメの詳細ページ（d-anime ストアのページ） |

#### データベースの作り方

```
$ docker exec -it d-anime-mylist-web-1 bash
コンテナ内 # python migrate.py
2022-03-22 09:10:13,777 INFO sqlalchemy.engine.Engine COMMIT
Create Table! ✨ 🍰 ✨
```
