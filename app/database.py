# from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = 'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}'
Base = declarative_base()

class EngineConnection:

    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle=500)
        # self.engine = create_engine(DB_URL, connect_args={"check_same_thread": False})  # "connect_same_thread" option is used only SQLite

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connect()
        return conn

    # def declarative(self):
    #     Base = declarative_base()
    #     return Base

