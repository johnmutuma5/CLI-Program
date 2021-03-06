from datetime import datetime
from app.user.comment import Comment
from app import store
from helpers.decorators import wrap_output

class User ():
    '''
    class User:
        params: username, password
        Methods:
            post_comment:
                params: msg
                return: comment
            view_comments:
                params: None
                return: None / prints comments
            edit_comment:
                params: comm_id, new_msg
                return: new_msg / replaces comment's msg with new_msg
    '''
    users = 0

    @classmethod
    def indexView (cls):
        user_input = input (
            '''
            What would you like to do?
                1. Post a comment
                2. Edit a comment
                3. View comments
                4. Logout
                Reply with an option as above: ''')

        input_action = {
            '1': {'type': 'post_comment'},
            '2': {'type': 'edit_comment'},
            '3': {'type': 'view_comments'},
            '4': {'type': 'logout'}
        }.get(user_input)

        return input_action

    @staticmethod
    def genUserId ():
        '''generates an eight-character user id e.g. USR00001
        '''
        User.users += 1
        return 'USR{:0>5}'.format(User.users)

    def __init__ (self, username, password):
        self.username = username
        self.password = password
        self.id = self.__class__.genUserId ()
        self.isAuthenticated = False
        self.lastLoggedInAt = None

    def post_comment (self, msg):
        '''
            creates a Comment object
            params: string msg
            return: comment
        '''
        timestamp = datetime.now()
        comment = Comment (msg, timestamp, self.id, self.username)
        return comment

    @wrap_output
    def view_comments (self):
        comments = store.comments

        for comment in sorted(comments.values(), key = lambda comment: comment.id):
            print(comment)

    def edit_comment (self, comm_id, new_msg):
        comments = store.comments
        target = comments.get(comm_id)

        if not target:
            print('\nUNSUCCESSFUL Comment id NOT found')
            return None

        if target.author_id == self.id or self.__class__.__name__ == 'Admin':
            target.msg = new_msg
            print('\nComment edited successfully\n')
            return target.msg

        print('Comment NOT edited. You can only edit your own comments')
        return None


class Moderator (User):
    moderators = 0
    @classmethod
    def indexView (cls):
        user_input = input (
            '''
            What would you like to do?
                1. Post a comment
                2. Edit a comment
                3. View comments
                4. Delete a comment
                5. Logout
                Reply with an option as above: ''')

        input_action = {
            '1': {'type': 'post_comment'},
            '2': {'type': 'edit_comment'},
            '3': {'type': 'view_comments'},
            '4': {'type': 'delete_comment'},
            '5': {'type': 'logout'}
        }.get(user_input)

        return input_action

    @staticmethod
    def genUserId ():
        '''generates an eight-character user id e.g. MOD00001
        '''
        Moderator.moderators += 1
        return 'MOD{:0>5}'.format(Moderator.moderators)

    def delete_comment (self, comm_id):
        comments = store.comments
        try:
            comments.pop(comm_id)
            print('\nComment DELETED successfully')
        except KeyError:
            print('\nUNSUCCESSFUL: could not find a comment with that id')


class Admin (Moderator, User):
    ...
