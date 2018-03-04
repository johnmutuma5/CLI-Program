class Store ():
    '''
    class: store ---> a simulation of a database
    params: None
    fields:
        users
            a dict of users \{username: user_obj\}
        comments
            a dict of comments \{comment_id: comment_obj\}
    methods:
        add_user
            params: user_obj
            return: added user_obj

    '''

    users = {}
    comments = {}

    def __init__ (self):
        ...

    def add_user (self, user_obj):
        '''
            return: the user_obj added
        '''
        username = user_obj.username
        if self.__class__.users.get(username): assert 0, 'Username already exists'
        self.__class__.users[username] = user_obj
        print("User {} successfully added".format(username))
        return self.__class__.users[username]

    def add_comment (self, comment_obj):
        '''
            return: the comment_obj added
        '''
        comment_id = comment_obj.id
        self.__class__.comments[comment_id] = comment_obj
        print ('Comment {} successfully posted'.format(comment_id))
        return self.__class__.comments[comment_id]
