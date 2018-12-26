import pymongo as pm 

class UseDatabase():

    def __init__(self, db_name='messenger'):

        connect = pm.MongoClient('localhost', 27017)

        self._user = connect.messenger.user

    # ********** add_user **********

    def add_user(self, name, login, password='123', email='no mail', sex=True):

        self._name = name

        self.login = login

        self._password = password

        self._email = email

        self._sex = sex

        self._user.insert_one(
            {'name': self._name, 'login':self.login, 'email': self._email, 'password': self._password, 'sex': self._sex})

    # ********** edit_user_name **********
    def edit_user_name(self, find_name, edit_name):

        self._user.update_one({'name': find_name}, {
                              '$set': {'name': edit_name}})

    # ********** edit_user_password **********

    def edit_user_password(self, find_name, edit_password):

        self._user.update_one({'name': find_name}, {
                              '$set': {'password': edit_password}})

    # ********** edit_user_email **********

    def edit_user_email(self, find_name, edit_email):

        self._user.update_one({'name': find_name}, {
                              '$set': {'email': edit_email}})

    # ********** edit_user_sex **********

    def edit_user_sex(self, find_name, edit_sex):

        self._user.update_one({'name': find_name}, {'$set': {'sex': edit_sex}})

    # ********** remove_user **********

    def remove_user(self, find_name):

        self._user.delete_one({'name': find_name})

    # ********** return list_name **********

    def return_list_name(self):

        # list(self._user.find(projection={'name': True, '_id': False})))
        list_users_name = list()

        for itm in self._user.find():

            list_users_name.append(itm.get('name'))
        
        return list_users_name

      




if __name__ == '__main__':

    user = UseDatabase()

    # user.add_user('test','logtst','qwe@mail.ru')
    # user.remove_user('zxc')
    print(user.return_list_name())
