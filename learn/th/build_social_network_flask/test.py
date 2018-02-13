class User():
    email = None
user = User()
user.email = "test@gmail.com"

def hidden_email(user):
    """
    >>>

    """
    emil_sp = user.email.split('@')
    hide_name = emil_sp[0][0] + "*" * (len(emil_sp[0])-1)
    print(hide_name + '@' + emil_sp[1])

for i in "abcdef":
    print(i)
    print(loop.index)



hidden_email(user)
