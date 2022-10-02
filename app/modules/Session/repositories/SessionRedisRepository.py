from datetime import datetime

from modules.Base.repositories.RedisRepository import RedisRepository
from modules.Session.entities.SessionEntity import SessionEntity


class SessionRedisRepository(RedisRepository):

    SESSION_PREFIX: str = 'session'
    SESSION_DATA_PREFIX: str = 'session_data'

    @staticmethod
    def create_session_entity(session_data: dict) -> SessionEntity:
        data = {
            'ID': session_data[b'id'].decode('utf-8'),
            'created_datetime': datetime.strptime(
                session_data[b'created_datetime'].decode('utf-8'),
                RedisRepository.DATETIME_FORMAT
            ),
            'expired_datetime': datetime.strptime(
                session_data[b'expired_datetime'].decode('utf-8'),
                RedisRepository.DATETIME_FORMAT
            ),
            'user_agent': session_data[b'user_agent'].decode('utf-8'),
        }

        return SessionEntity(**data)

    def __init__(self):
        self._db = self._get_DB('session')

    def _get_session_key(self, session_ID: str) -> str:
        return f'{self.SESSION_PREFIX}:{session_ID}'

    def add_session(self, session: SessionEntity):
        key = self._get_session_key(session.ID)
        session_TTL = int((session.expired_datetime - session.created_datetime).total_seconds())

        self._db.hmset(
            key,
            {
                'id': session.ID,
                'created_datetime': session.created_datetime.strftime(RedisRepository.DATETIME_FORMAT),
                'expired_datetime': session.expired_datetime.strftime(RedisRepository.DATETIME_FORMAT),
                'user_agent': session.user_agent,
            }
        )

        self._db.expire(key, session_TTL)

    def get_session(self, session_ID: str):
        key = self._get_session_key(session_ID)
        session_data = self._db.hgetall(key)

        return SessionRedisRepository.create_session_entity(session_data) if session_data else None
