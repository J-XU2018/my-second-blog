# decorator
# adding/editing func to different original funcs

def my_time(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in: {}sec".format(orig_func.__name__, t2))
        return result
    return wrapper

import time
@my_time
def display():
    time.sleep(2)
    print('display run')

display()
