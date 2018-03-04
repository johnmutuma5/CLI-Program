from app import User, Comment
from app import store
from datetime import datetime

session = {'user': None}

def main ():
    render_homepage ()

    user = session['user']
    render_indexViewFor (user)












def login ():
    username = input ("LOGIN: \n\tEnter your username: ")
    password = input ("\tEnter your password: ")

    user = store.users.get(username)
    if user and user.password == password:
        session['user'] = user
        user.isAuthenticated = True
        user.lastLoggedInAt = datetime.now ()

        render_indexViewFor (user)
    else:
        assert 0, 'Invalid username or password'


def sign_up ():
    username = input ("SIGN UP: \n\tEnter your username: ")
    password = input ("\tEnter your password: ")

    user = User (username, password)
    store.add_user (user)
    print('Success, you can now login')


def render_homepage ():
    if session.get('user'):
        return

    user_input = input (
        '''What would you like to do?
            1. Login
            2. Sign Up
            Reply with an option as above: ''')

    input_method = {
        '1': login,
        '2': sign_up
    }[user_input] # an elegant replacement for python's lack of switch case

    try:
        input_method ()
    except AssertionError as e:
        print (e)

    return render_homepage ()



def render_indexViewFor (user):
    input_action = user.__class__.indexView ()

    if input_action['type'] == 'post_comment':
        # post_comment params: string msg
        msg = input('Write your thoughts here: ')
        comm = getattr(user, 'post_comment')(msg)
        store.add_comment(comm)

    elif input_action['type'] == 'view_comments':
        # view_comments params: store
        getattr(user, 'view_comments')()

    elif input_action['type'] == 'edit_comment':
        # edit_comment params: comment_id, new_msg
        comm_id = input('Enter targeted comment id: ')
        new_msg = input('Enter replacement message: ')
        getattr(user, 'edit_comment')(comm_id, new_msg)

    while not input_action['type'] == 'logout':
        render_indexViewFor (user)

    print('Goodbye {}'.format(user.username))
    session.pop('user')
    render_homepage ()
