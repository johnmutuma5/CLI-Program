from app import User, Moderator, Admin, Comment
from app import store, session
from helpers.key_funcs import render_homepage, render_indexViewFor


def main ():

    mod = Moderator ('mod', 'math')
    admin = Admin ('admin', 'math')

    # add default users admin and moderator
    store.add_user (mod)
    store.add_user (admin)

    render_homepage ()

    user = session['user']
    render_indexViewFor (user)
