class Comment ():
    '''
    class: Comment
        params: msg, timestamp, author_id
    '''
    comments = 0

    @staticmethod
    def genCommentId ():
        '''generates an 8-character commnet id e.g. USR00001
        '''

        Comment.comments += 1
        return 'COM{:0>5}'.format(Comment.comments)

    def __init__ (self, msg, timestamp, author_id, author_name):
        self.id = self.__class__.genCommentId ()
        self.msg = msg
        self.timestamp = timestamp
        self.author_id = author_id
        self.author_name = author_name


    def __str__ (self):
        return '''
        {}
        {}: {}
        {}
        '''.format(self.author_name, self.id, self.msg, self.timestamp)
