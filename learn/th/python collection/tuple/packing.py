def multiply(*args):
    product = 1;
    print(args)
    # ar = tuple(args)
    for i in args:
        product *= i
    return product

print(multiply(1,2,3,4))


for index, letter in enumerate("abc"):
    print("{} {}".format(index+1,letter))

def stringcases(string):
    return string.upper(), string.lower(),string.title(), "".join(list(string)[::-1])

# print("".join([a,b,c]))
print(stringcases("abc"))
