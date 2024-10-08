MYSQL_DB_CREDENTIALS = {
    'host': 'localhost',
    'port': 3306,
    'user': 'user',
    'password': 'password',
    'database': 'database',
}

REDIS_DB_CREDENTIALS = {
    'host': 'localhost',
    'port': 6379,
}

REDIS_DBS = {
    'test': 0,
    'session': 1,
    'cache': 2,
    'notification': 3,
}

SESSION_COOKIE_NAME = 'usid'
SESSION_ID_LENGTH = 32
SESSION_LIFETIME_DAYS = 7

PASSWORD_ABC = '1234567890abcdefghijklmnopqrstuvwxyz'
PASSWORD_ABC_SAFE = '23456789abcdefghjkmnpqrstuvwxyz'
PASSWORD_ABC_UPPER = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PASSWORD_ABC_UPPER_SAFE = '23456789ABCDEFGHJKMNPQRSTUVWXYZ'
PASSWORD_ABC_FULL = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
PASSWORD_ABC_FULL_SAFE = '23456789abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ'
PASSWORD_LENGTH = 12
PASSWORD_LENGTH_MIN = 1
PASSWORD_LENGTH_MAX = 128
PASSWORD_SALT_LENGTH = 12
PASSWORD_SALT = 'PasswordSalt'

USE_ENTITY_STORE = True
