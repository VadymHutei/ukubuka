# Ukubuka

## Comand hints

```
mkdir app
cd app
python3.9 -m venv env
source env/bin/activate
```

### Requirements

```
pip install -U pip

pip install Flask
pip install PyMySQL

# or

pip install -r ../requirements.txt
```

```
export FLASK_APP=main.py
export FLASK_ENV=development
flask run --port=5000
```

```
docker run --name ukubuka_db -d --restart always -v C:\Users\hutei\dev\ukubuka\db\data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 mysql:5
```

## Routing

### Shop

URL | Redirect
|
**Catalog**
```/shop```
```/shop/:categoryID``` | ```/shop/:categoryAlias```
```/shop/:categoryAlias```
```/shop/:subcategoryID``` | ```/shop/:subcategoryAlias```
```/shop/:subcategoryAlias```
```/shop/:categoryID/:subcategoryID``` | ```/shop/:subcategoryAlias```
```/shop/:categoryID/:subcategoryAlias``` | ```/shop/:subcategoryAlias```
```/shop/:categoryAlias/:subcategoryID``` | ```/shop/:subcategoryAlias```
```/shop/:categoryAlias/:subcategoryAlias``` | ```/shop/:subcategoryAlias```
```/shop/:catalogID``` | ```/shop/:catalogAlias```
```/shop/:catalogAlias```
**Product**
```/shop/:category/:product_id```
```/shop/:category/:subcategory/:product_id```
```/shop/:category/:subcategory/:subcategory/:product_id```
```/shop/:category/:product_alias```
```/shop/:category/:subcategory/:product_alias```
```/shop/:category/:subcategory/:subcategory/:product_alias```
```/shop/:product_id```
```/shop/:product_alias```
**SKU**
```/shop/:category/:sku_id```
```/shop/:category/:subcategory/:sku_id```
```/shop/:category/:subcategory/:subcategory/:sku_id```
```/shop/:category/:sku_alias```
```/shop/:category/:subcategory/:sku_alias```
```/shop/:category/:subcategory/:subcategory/:sku_alias```
```/shop/:sku_id```
```/shop/:sku_alias```