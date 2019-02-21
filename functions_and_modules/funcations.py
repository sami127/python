def greet(msg,name):
    print(msg,name)

# greet('hello','sami')

def mul_greet(*name):
    print(name)
    for n in name:
        print (n)
# mul_greet('hello','sami','kavitha','harry')

def greek(name, msg='Hello'):
    print(msg,name)

# greek('samiulla',msg='Welcome')

def greek_new(full_name,**kwargs):
    print('full_name : %s' %(full_name))
    
    for k,v in kwargs.items():
        print(k,v)

# greek_new('samiulla jamadar',first='samiula',last='jamadar')

# lamda argumetns : express

double = lambda x: x*2
# print(double(5))

# filter()
my_list = [1,5,4,6,8,11,3,12]
new_list = list(filter(lambda x:(x%2==0),my_list))
print(new_list)


# map()
new_list = list(map(lambda x: x*2, my_list))
print(new_list)




