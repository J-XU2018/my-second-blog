# generator not holding all the values and memory, so
# it's performance is better, faster and less memory use

def square_num(nums):
    for num in nums:
        yield (num*num)

my_nums = square_num([1, 2, 3, 4])
# my_nums2 = [m * m for m in [1, 2, 3, 4]] #comprehensive
my_nums3 = (m * m for m in [1, 2, 3, 4]) #generator
print(my_nums)
print(next(my_nums))
print("next:")
for num in my_nums:
    print(num)
print(my_nums3)
# print(list(my_nums3))
print(next(my_nums3))
