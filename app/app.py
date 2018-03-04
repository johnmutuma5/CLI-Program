from app import User, Comment
from app import store
from datetime import datetime

session = {'user': None}

def main ():
    while not session['user']:
        user_input = render_homepage ()

        input_method = {
            '1': login,
            '2': sign_up
        }[user_input] # an elegant replacement for python's lack of switch case

        try:
            input_method ()
        except AssertionError as e:
            print (e)


    user = session['user']

    while True:
        input_action = render_indexViewFor (user)

        if input_action['type'] == 'post_comment':
            # post_comment params: string msg
            msg = input('Write your thoughts here: ')
            comm = getattr(user, input_action['method'])(msg)
            store.add_comment(comm)











def login ():
    username = input ("LOGIN: \n\tEnter your username: ")
    password = input ("\tEnter your password: ")

    user = store.users.get(username)
    if user and user.password == password:
        session['user'] = user
        user.isAuthenticated = True
        user.lastLoggedInAt = datetime.now ()
        print(user.lastLoggedInAt)
    else:
        assert 0, 'Invalid username or password'


def sign_up ():
    username = input ("SIGN UP: \n\tEnter your username: ")
    password = input ("\tEnter your password: ")

    user = User (username, password)
    store.add_user (user)
    print('Success, you can now login')





def render_homepage ():
    user_input = input (
        '''What would you like to do?
            1. Login
            2. Sign Up
            Reply with an option as above: ''')

    return user_input

def render_indexViewFor (user):
    input_action = user.__class__.indexView ()
    return input_action
