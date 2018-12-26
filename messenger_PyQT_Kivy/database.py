from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

import settings


Base = declarative_base()


class DatabaseManager(metaclass=ConfigMetaclass):

    def __init__(self):

        self._engine = create_engine(settings.CONNECTION_STRING)

        self._session_class = sessionmaker(bind=self._engine)

    def init_database(self):

        Base.metadata.create_all(self._engine)

    def create_session(self):

        return self._session_class()
