from typing import Optional

from modules.Base.repositories.MySQLRepository import MySQLRepository
from modules.User.entities.UserEntity import UserEntity
from modules.User.entities.UserNameEntity import UserNameEntity


class UserRepository(MySQLRepository):

    @staticmethod
    def create_user_entity(row: dict) -> UserEntity:
        return UserEntity(
            ID=int(row['id']),
            email=row['email'],
            name=UserNameEntity(
                first_name=row['first_name'],
                last_name=row['last_name'],
            ),
            is_blocked=bool(row['is_blocked']),
            registered_datetime=row['registered_datetime'],
        )

    def get_user_by_ID(self, user_ID: int) -> Optional[UserEntity]:
        query = '''
            SELECT
                id,
                email,
                first_name,
                last_name,
                is_blocked,
                registered_datetime
            FROM
                user
            WHERE
                id = %s
        '''

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (user_ID,))

        return UserRepository.create_user_entity(cursor.fetchone())

    def get_user_by_email(self, email: str) -> Optional[UserEntity]:
        query = '''
            SELECT
                id,
                email,
                first_name,
                last_name,
                is_blocked,
                registered_datetime
            FROM
                user
            WHERE
                email = %s
        '''

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (email,))
                user_data = cursor.fetchone()
        
        return UserRepository.create_user_entity(user_data) if user_data else None

    def get_user_by_session_ID(self, session_ID: str) -> Optional[UserEntity]:
        query = '''
            SELECT
                user.id,
                user.email,
                user.first_name,
                user.last_name,
                user.is_blocked,
                user.registered_datetime
            FROM
                user
            JOIN
                session_user ON session_user.user_id = user.id
            WHERE
                session_user.session_id = %s
        '''

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (session_ID,))
                try:
                    return UserRepository.create_user_entity(cursor.fetchone())
                except:
                    return None

    def add_user(self, data: dict) -> int:
        query1 = '''
            INSERT INTO user (
                email,
                first_name,
                last_name,
                is_blocked,
                registered_datetime
            )
            VALUES (
                %s,
                NULL,
                NULL,
                1,
                %s
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

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query1, (data['email'], data['registered']))
                user_ID = cursor.lastrowid
                cursor.execute(query2, (data['passwordHash'], data['salt']))
            connection.commit()

        return user_ID

    def get_user_password_by_email(self, email: str) -> Optional[tuple]:
        query = '''
            SELECT
                u.id,
                up.password_hash,
                up.salt
            FROM
                user u
            JOIN
                user_password up
                ON up.user_id = u.id
            WHERE
                u.email = %s
        '''

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, email)

                return cursor.fetchone()

    def logout_by_session_ID(self, session_ID: str):
        query = '''
            UPDATE
                session_user
            SET
                is_logged_in = 0
            WHERE
                session_id = %s
        '''

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (session_ID,))
            connection.commit()

    def get_users(self) -> list[UserEntity]:
        query = '''
            SELECT
                id,
                email,
                first_name,
                last_name,
                is_blocked,
                registered_datetime
            FROM
                user
        '''

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)

                return [UserRepository.create_user_entity(row) for row in cursor.fetchall()]

    def block_user(self, user_ID: int):
        query = '''
            UPDATE
                user
            SET
                is_blocked = 1
            WHERE
                id = %s
        '''

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (user_ID,))
            connection.commit()

    def unblock_user(self, user_ID):
        query = '''
            UPDATE
                user
            SET
                is_blocked = 0
            WHERE
                id = %s
        '''

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (user_ID,))
            connection.commit()
