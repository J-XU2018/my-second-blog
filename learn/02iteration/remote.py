class RemoteControl():

    def __init__(self):
        self.channels = ['HBO', 'cnn', 'cctv']
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        # if self.index == len(self.channels):
        #     raise StopIteration
        # return self.channels[self.index]
        try:
            return self.channels[self.index]
        except Exception as e:
            print("error")
        # finally:
            # print("finally this will run")


r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

print(next(itr))
