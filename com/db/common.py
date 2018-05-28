import threading
import uuid

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


_LOCK = threading.Lock()
_SQL_ENGINE = None
SESSION = None


def get_engine():
    global _LOCK
    with _LOCK:
        global _SQL_ENGINE

        if not _SQL_ENGINE:
            _SQL_ENGINE = create_engine("mysql+pymysql://root:@localhost:3306/btcgraph", encoding="utf-8", echo=False)
        return  _SQL_ENGINE


def get_session():
    global SESSION
    if not SESSION:
        SESSION = sessionmaker(bind=get_engine())()
    return SESSION


def generate_uuid(dashed=True):
    """Create a random uuid string
    :param dashed:
    :return:
    """
    if dashed:
        return str(uuid.uuid4())
    return uuid.uuid4().hex


