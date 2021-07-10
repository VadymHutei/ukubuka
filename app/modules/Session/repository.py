from vendor.Ukubuka.repository import Repository
from config import DB_CREDENTIALS


class SessionMySQLRepository(Repository):

    def __init__(self):
        super().__init__()
        self._setCredentials(DB_CREDENTIALS)

    def addSession(self, sessionID, created, expired):
        query = '''
            INSERT INTO session (
                id,
                created_datetime,
                expired_datetime
            )
            VALUES (
                %s,
                %s,
                %s
            )
        '''

        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (sessionID, created, expired))
            connection.commit()

    def getUserIDBySessionID(self, sessionID):
        query = '''
            SELECT
                user_id
            FROM
                session_user
            WHERE
                session_id = %s
        '''

        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query, sessionID)
                result = cursor.fetchone()
        return result

    def getUserBySessionID(self, sessionID):
        query = '''
            SELECT
                u.id,
                u.email,
                u.first_name,
                u.last_name,
                u.is_confirmed,
                su.is_logged_in
            FROM
                session_user AS su
            JOIN
                user AS u ON u.id = su.user_id
            WHERE
                su.session_id = %s
        '''

        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query, sessionID)
                result = cursor.fetchone()
        return result

    def setLoginStatus(self, sessionID, userID, isLogin):
        query = '''
            INSERT INTO
                session_user (
                    session_id,
                    user_id,
                    is_logged_in
                )
            VALUES
                (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
                user_id = %s,
                is_logged_in = %s
        '''

        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (sessionID, userID, isLogin, userID, isLogin))
            connection.commit()

    def setSessionData(self, sessionID, key, value):
        query = '''
            INSERT INTO
                session_data (
                    session_id,
                    data
                )
            VALUES
                (
                    %s,
                    JSON_OBJECT(%s, %s)
                )
            ON DUPLICATE KEY UPDATE
                data = JSON_SET(data, CONCAT('$.', %s), %s)
        '''

        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (sessionID, key, value, key, value))
            connection.commit()

    def getSessionData(self, sessionID, key):
        query = '''
            SELECT
                JSON_EXTRACT(data, CONCAT('$.', %s)) AS value
            FROM
                session_data
            WHERE
                session_id = %s
        '''

        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (key, sessionID))
                result = cursor.fetchone()
        return result