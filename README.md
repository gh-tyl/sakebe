# api

# YOTOBackend

## 環境構築
### 初回手順(親ディレクトリで作業)
1. 環境ファイルのコピー
```
cp .env.example .env
```
2. .envのXXXXを任意の値に変更
3. localのdbを使用する場合
```
sh sh/reset_db.sh
```
4. コンテナのビルド
```
docker-compose up -d --build
```
5. コンテナの起動
```
docker-compose up -d
```
6. 起動コンテナの確認 (STATUSがUpとなっていたら起動済み)
```
docker ps
```
7. 
```
docker stop [CONTAINER ID or NAMES]
```

### 手順(通常時)
- docker-composeでコンテナを起動
```
docker-compose up -d
```
### 手順(Case by case)
- db更新時
```
sh sh/reset_db.sh
```

### dockerコマンド一覧
- コンテナの起動
```
docker-compose up -d
```
- 起動コンテナの確認(STATUSがUpとなっていたら起動済み)
```
docker ps
```
- ログの確認
```
docker logs -f [CONTAINER ID or NANES]
```

### Flask関連のコマンド
```zsh
# 追記予定
```

### mysqlコマンド一覧
```zsh
# 追記予定
```

### 3-1. ブランチのルール
- 本番環境: main
- 開発環境: develop
- 新機能開発: feature

### Curlコマンド
API