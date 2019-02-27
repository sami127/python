

def my_gen():
    n=1
    print("This is first")
    yield n

    n += 1
    print("This is second")
    yield n

    n+=1
    print("This is third")
    yield n


# for i in my_gen():
#     print(i)

my_list = [1,3,6,10]
gen = (x ** 2 for x in my_list)

print(list(gen))