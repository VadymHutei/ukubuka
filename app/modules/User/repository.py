from config import DB_CREDENTIALS
from vendor.Ukubuka.repository import Repository


class UserRepository(Repository):

    def __init__(self):
        super().__init__()
        self._setCredentials(DB_CREDENTIALS)

    def getUserByEmail(self, email):
        query = '''
            SELECT
                id,
                email,
                first_name,
                last_name,
                is_confirmed
            FROM
                user
            WHERE
                email = %s
        '''
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (email,))
                result = cursor.fetchone()
        return result

    def addUser(self, data):
        query1 = '''
            INSERT INTO user (
                email,
                first_name,
                last_name,
                is_confirmed
            )
            VALUES (
                %s,
                NULL,
                NULL,
                1
            )
        '''
        query2 = '''
            INSERT INTO user_password (
                user_id,
                password_hash,
                salt
            )
            VALUES (
                LAST_INSERT_ID(),
                %s,
                %s
            )
        '''
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query1, (data['email'],))
                userID = cursor.lastrowid
                cursor.execute(query2, (data['passwordHash'], data['salt']))
            connection.commit()
        return userID

    def getUserPasswordByEmail(self, email):
        query = '''
            SELECT
                u.id,
                up.password_hash,
                up.salt
            FROM
                user u
            JOIN
                user_password up ON up.user_id = u.id
            WHERE
                u.email = %s
        '''
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, email)
                result = cursor.fetchone()
        return result

    def logoutBySessionID(self, sessionID):
        query = '''
            UPDATE
                session_user
            SET
                is_logged_in = 0
            WHERE
                session_id = %s
        '''
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (sessionID,))
            connection.commit()