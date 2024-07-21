# Ukubuka

## Hints

### Virtual environment
```
python3 -m venv env
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

### MySQL DB
```
docker run --name mysql8 -d --restart always -v /path/to/mysql/data/dir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 mysql:8
```

### Redis
```
docker run --name redis7 -d --restart always -v /path/to/redis/data/dir:/data -p 6379:6379 redis:7
```

### Running app
```
flask --app=app/main.py --debug run --port=5000
```
