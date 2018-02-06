# Closures closes free variables

def outer_func():
    msg = "hi"

    def inner_func():
        print(msg)

    return inner_func()

outer_func()


# sample2
def outer_func(msg):

    def inner_func():
        print(msg)

    return inner_func
hi_func = outer_func("hi,there")
bye_func = outer_func('bye')
print(hi_func.__name__)

hi_func()
bye_func()

# sample3
def outer_func(msg):

    def inner_func(inner_msg):
        print(inner_msg)
        print(msg)

    return inner_func
hi_func = outer_func("hi,there")
bye_func = outer_func('bye')
# print(hi_func.__name__)

hi_func("inner_HIHI")
bye_func("inner Byebye")
