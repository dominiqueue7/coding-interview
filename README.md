# coding-interview

- Categoryモデルの読み取り・作成・更新・削除が出来るAPI
  ※ views/category.py, serializers/category.py に実装するイメージ
- APIのテストの実装
  ※ test_views.pyに実装するイメージ

# start up postgresql with docker

```shell
docker compose up -d
```

# request with postman 

## GET

```url
localhost:8000/api/categories/
```

## POST

```url
localhost:8000/api/categories/
```

body

```json
{
    "company": "76334870-ea84-4c6d-a1da-37a1920a0ed6",
    "name": "gpu"
}
```

## PATCH

```url
localhost:8000/api/categories/76334870-ea84-4c6d-a1da-37a1920a0ed6/
```

body

```json
{
    "name": "graphics"
}
```

## DELETE

```url
localhost:8000/api/categories/76334870-ea84-4c6d-a1da-37a1920a0ed6/
```
