my_list = [4,7,0,3]
my_iter = iter(my_list)
# next(my_iter)

class PowTwo:

    def __init__(self, max=0):
        print("hi from init")
        self.max = max

    def __iter__(self):
        print("Hi from iter")
        self.n = 0
        return self

    def __next__(self):
        print("hi from next")
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

a = PowTwo(4)
# a.iter
i = iter(a)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))




