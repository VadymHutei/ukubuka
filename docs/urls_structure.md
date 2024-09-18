# URLs

## Base pattern

```
https://<domain>/<language>/<keyword>/<unique_name>
```

## Examples

```
https://<domain>/ua/catalogs/black_friday_sale
https://<domain>/ua/categories/furniture
https://<domain>/ua/products/sony_xperia_1_V
https://<domain>/ua/pages/contacts
```

Префікс: https://<domain>/ua

## Структура

### Головна
```
/
```
### Розділ клієнта (редірект)
```
/customer
```
### Реєстрація клієнта
```
/customer/registration
```
### Автентифікація клієнта
```
/customer/authentication
```
### Кабінет клієнта
```
/customer/account
```
### Каталог
```
/catalog
```
### Категорія
```
/catalog/<category_code>
/catalog/<category_id> - редірект на код
```
### Товар
```
/product/<product_code>
/product/<product_id>
```
### Кошик
```
/cart
```
### Оформлення замовлення
```
/authentication
```
### Автентифікація
```
/authentication
```