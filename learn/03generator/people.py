import sys
import random
import time

names = ['John', 'Katie', 'Adam', 'Jack', 'Laura']
majors = ['Math', 'Art', 'Finance', 'Science', 'Business']
print("memory (before): {}Mb".format(sys.getsizeof([])))

def people_list(num_people):
    result = []
    for i in range(num_people): #xrange
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

# t1 = time.time()
# people = people_list(1000000)
# t2 = time.time()
# print(people)

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()
# print(people)
# print(next(people))

print("Memory(after): {}Mb".format(sys.getsizeof([])))
print("Took {} seconds".format(t2 - t1))
