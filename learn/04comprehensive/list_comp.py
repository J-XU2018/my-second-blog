nums = [1, 2, 3, 4, 5, 6]

# i want n for each n in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)
my_list = [n for n in nums]
print(my_list)

#i want n*n for each n in my_nums
my_list2 = []
for n in nums:
    my_list2.append(n * n)
print(my_list2)
my_list2 = [n*n for n in nums]
print(my_list2)

#using a map + lambda
my_list3 = map(lambda n: n*n, nums)
print(my_list3)

# i want n for each n in nums if n is even
my_list4 = [n for n in nums if n%2 == 0]
print(my_list4)

# using filter + lambda
my_list5 = filter(lambda n: n%2 ==0, nums)
print(my_list5)

# i want a (letter, num) pair for each letter in 'abcd' and each number in '0213'
my_list6 = []
for letter in 'abcd':
    for num in range(4):
        my_list6.append((letter, num))
print(my_list6)
my_list6 = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list6)

# dectionary comprehensive
names = ['John', 'Katie', 'Adam', 'Jack', 'Laura']
majors = ['Math', 'Art', 'Finance', 'Science', 'Business']
# print(zip(names, majors)) #not work, its generator
# print(list(zip(names,majors)))
# for zip in zip(names, majors):
    # print(zip)


# i want a dict{'name': 'majors'} for each name, mafor in zip(names, majors)
my_dict = {}
for name, major in list(zip(names, majors)):
    my_dict[name] = major
print(my_dict)

my_dict2 = {name: major for name, major in list(zip(names, majors))}
print(my_dict2)

# if name not equal to John
my_dict3 = {name: major for name, major in list(zip(names, majors)) if name != 'John'}
print(my_dict3)

# set comprehensive
nums = [1, 1, 2, 3, 4, 4,]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)
my_set2 = {n for n in nums}
print(my_set2)

# generator expression
# i want to yield 'n*n' for each n in nums
def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)
for i in my_gen:
    print(i)

my_gen2 = (n*n for n in nums)
for i in my_gen2:
    print(i)
