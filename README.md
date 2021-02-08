# Ukubuka

## Comand hints

```
mkdir app
cd app
python3.9 -m venv env
source env/bin/activate
```

```
pip install -U pip
pip install -r requirements.txt
```

```
export FLASK_APP=main.py
export FLASK_ENV=development
flask run --port=5000
```

```
docker run --name ukubuka_db -d --restart always -v C:\Users\hutei\dev\ukubuka\db\data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 mysql:5
```