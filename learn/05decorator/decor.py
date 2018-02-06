# decorator
# adding/editing func to different original funcs

def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print("wrapper executed this before {}.".format(original_func.__name__))
        return original_func(*args, **kwargs)
    return wrapper_func

@decorator_func
def display():
    print('display func ran')

@decorator_func
def display_info(name, age):
    print('display_info ran with args ({}, {})'.format(name, age))

display()
display_info('jack', 40)
