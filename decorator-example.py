def user_auth(func):
    def wrapper():
        user = input('User name: ')
        if user in users_list:
            func()
        else:
            print('Unknown user!')
    return wrapper

@user_auth
def get_data_from_database():
    print("Super secure data from database")
  
users_list = ['admin', 'ivan', 'ivan_ivan']

get_data_from_database()
