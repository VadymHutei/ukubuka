from pymysql.cursors import DictCursor


DB_CREDENTIALS = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'ukubuka',
    'cursorclass': DictCursor
}