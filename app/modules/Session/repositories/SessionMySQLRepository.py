from modules.Base.repositories.MySQLRepository import MySQLRepository
from modules.Session.entities.SessionEntity import SessionEntity


class SessionMySQLRepository(MySQLRepository):

    @staticmethod
    def create_session_entity(row: dict) -> SessionEntity:
        return SessionEntity(
            ID=row['id'],
            created_datetime=row['created_datetime'],
            expired_datetime=row['expired_datetime'],
            user_agent=row['user_agent'],
        )

    def get_session(self, session_ID: str) -> SessionEntity | None:
        query = '''
            SELECT
                id,
                created_datetime,
                expired_datetime,
                user_agent
            FROM
                session
            WHERE
                id = %s
        '''

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (session_ID,))
                try:
                    return SessionMySQLRepository.create_session_entity(cursor.fetchone())
                except:
                    return None

    def add_session(self, session: SessionEntity):
        query = '''
            INSERT INTO session (
                id,
                created_datetime,
                expired_datetime,
                user_agent
            )
            VALUES (
                %s,
                %s,
                %s,
                %s
            )
        '''
        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                data = (
                    session.ID,
                    session.created_datetime,
                    session.expired_datetime,
                    session.user_agent
                )
                cursor.execute(query, data)
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
        with self.get_connection() as connection:
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
                u.is_blocked,
                u.registered_datetime,
                su.is_logged_in
            FROM
                session_user AS su
            JOIN
                user AS u
                ON u.id = su.user_id
            WHERE
                su.session_id = %s
        '''
        with self.get_connection() as connection:
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
        with self.get_connection() as connection:
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
        with self.get_connection() as connection:
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
        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (key, sessionID))
                result = cursor.fetchone()
        return result
