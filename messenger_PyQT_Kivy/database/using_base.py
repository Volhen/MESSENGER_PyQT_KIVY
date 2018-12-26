from sqlalchemy import create_engine

from sqlalchemy import Table, Column, Integer, Numeric, String, MetaData, ForeignKey

from sqlalchemy.orm import sessionmaker

from dbcore import Base

import message

import user


class UsingBase():

    def __init__(self):

        self.engine = create_engine('sqlite:///database/DB/MesDB.db3')

        session = sessionmaker(bind=self.engine)

        self._session = session()

        Base.metadata.create_all(self.engine)

        message.Base.metadata.create_all(self.engine)

        user.Base.metadata.create_all(self.engine)


    def show_message(self):

        # for mes in self._session.query(user):

        #     print('"{}"'.format(mes.User.lo))
        # print(str(user.User.__repr__))

        q_artists = self._session.query(user.User).all()
        print(q_artists)
            

    def create_message(self):

        us = user.User('Volhen', '555')

        # mes = message.Message('Text')

        self._session.add(us)

        self._session.commit()


if __name__ == '__main__':

	use = UsingBase()

	use.create_message()

	use.show_message()
