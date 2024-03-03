from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from starlette.config import Config


class engineconn:
    def __init__(self):
        config = Config(".env")
        self.engine = create_engine(config('DATABASE_URL'), pool_recycle = 500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connect()
        return conn
