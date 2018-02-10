def packer(**kwargs):
    print(kwargs)

packer(name="Jack", age=30, job="developper")

###########????
def packer(name=None, **kwargs):
    print(kwargs)

packer(name="Jack", age=30, job="developper")

##unpacker
def unpacker(welcom,first_name=None, last_name=None):
    if first_name and last_name:
        print("{0}, {1} {2}, {0}".format(welcom,first_name, last_name))
    else:
        print('Hi, no name!')

unpacker("hi",**{"first_name": "Jack", 'last_name': 'X'})
unpacker('Hi',"jack")
unpacker("Hi", 'jack', 'xu')
