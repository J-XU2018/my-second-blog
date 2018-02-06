def square(x):
    return x * x

f = square
print(f(4))

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

square = my_map(square, [1, 2, 3, 4])

print(square)

def cube(x):
    return x * x * x

print(my_map(cube, [1 ,2, 3, 4]))
