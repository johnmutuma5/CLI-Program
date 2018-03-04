

def wrap_output (func):

    def wrapper (*args, **kwargs):
        print('{:*<32} BEGIN {:*<32}'.format('', ''))
        res = func (*args, **kwargs)
        print('{:*<32} END {:*<32}'.format('', ''))
        return res

    wrapper.__doc__ = func.__doc__
    wrapper.__name__ = func.__name__
    return wrapper
