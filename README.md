# Ukubuka

```
# virtual environment
python3.9 -m venv env
source env/bin/activate

# requirements
pip install -U pip

pip install Flask
pip install PyMySQL

# or

pip install -r ../requirements.txt

# MySQL DB
docker run --name ukubuka_db -d --restart always -v C:\Users\hutei\dev\ukubuka\db\data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 mysql:5

# run app
flask --app=app/main.py --debug run --port=5000
```