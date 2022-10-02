from flask import current_app as app
from redis import Redis


class RedisRepository:

    DATETIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'

    def _get_DB(self, db_type: str) -> Redis:
        return Redis(
            **app.config['REDIS_DB_CREDENTIALS'],
            db=app.config['REDIS_DBS'][db_type]
        )
