from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy import create_engine

from sqlalchemy.orm import relationship

from dbcore import Base

from user import User


class Message(Base):

    __tablename__ = 'Message'

    MessageID = Column(Integer, primary_key=True)

    Information = Column(String)

    user_id = Column(Integer, ForeignKey('User.UserID'))

    user = relationship(User, foreign_keys=[user_id])

    def __init__(self, information):


        self.information = information

    def __repr__(self):

        return "<Message ('%s')>" % self.Information


if __name__ == '__main__':

    engine = create_engine('sqlite:///DB/MesDB.db3')

    Base.metadata.create_all(engine)

