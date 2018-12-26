from sqlalchemy import Column, Integer, String

from sqlalchemy import create_engine

from dbcore import Base


class User(Base):

    __tablename__ = 'User'

    UserID = Column(Integer, primary_key=True)

    Login = Column(String)

    Information = Column(String)

    def __init__(self, login, information):

        self.Login = login

        self.Information = information

    def __repr__(self):

        return "<User ('{} {} {}')>".format(self.Login, self.Information, self.UserID)


if __name__ == '__main__':

    engine = create_engine('sqlite:///DB/MesDB.db3')

    Base.metadata.create_all(engine)
