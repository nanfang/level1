import psycopg2
import psycopg2.extensions

from level1.conf import settings

_default_conn = None

IntegrityError = psycopg2.IntegrityError


def get_conn():
    global _default_conn
    if not _default_conn:
        db_settings = settings['DB']
        _default_conn = psycopg2.connect(database=db_settings['DATABASE'],
                                         user=db_settings['USER'],
                                         password=db_settings['PASSWORD'])
        _default_conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    return _default_conn


def get_cursor():
    return get_conn().cursor()
