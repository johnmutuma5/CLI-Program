from storage import Store

store = Store()
session = {'user': None}

from app.user import User, Moderator, Admin, Comment
