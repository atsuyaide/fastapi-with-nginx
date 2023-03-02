# FastAPI サーバーに Nginx 経由で接続する

## 役割

- FastAPI: Web API サーバー
- Nginx: リバースプロキシ

## 構成

- FastAPI
  - `/users`: ユーザー ID のリストを返す
  - `/docs`: Swagger UI
  - `/redocs`: ReDoc UI
- Nginx
  - `/api/user-service/v1/users`: FastAPI サーバの`/users`にルーティング
  - `/api/user-service/v1/docs`: FastAPI サーバの`/docs`にルーティング
  - `/api/user-service/v1/redocs`: FastAPI サーバの`/redocs`にルーティング

## 起動方法

環境変数を設定

```shell
export $(cat ./webapp/.env)
```

Nginx と FastAPI サーバを起動

```shell
docker compose up -d
```

## 接続

ブラウザから Swagger UI に接続します.

### Nginx 経由でアクセス

`localhost:8080/api/user-service/v1/docs`にアクセス

### FastAPI サーバに直接アクセス

`localhost:8000/api/user-service/v1/docs`にアクセス
