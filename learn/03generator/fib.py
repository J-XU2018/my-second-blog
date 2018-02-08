def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# itr = iter(fib())
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

for f in fib():
    if f > 50:
        break
    print(f)
