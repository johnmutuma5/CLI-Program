from datetime import datetime
from app.user.comment import Comment

class User ():
    '''
    class User:
        params: username, password
        Methods:
            post_comment:
                params: msg
                return: comment
    '''
    users = 0

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
        comment = Comment (msg, timestamp, self.id)
        return comment

    def view_comments (self, store):
        

    def indexView ():
        user_input = input (
            '''
            What would you like to do?
                1. Post a comment
                2. Edit a comment
                3. View comments
                Reply with an option as above: ''')

        input_action = {
            '1': {'type': 'post_comment', 'method': 'post_comment'},
            '2': 'edit_comment(com_id)',
            '3': 'view_comments'
        }[user_input]

        return input_action
