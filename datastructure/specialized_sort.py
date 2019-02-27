a = [5,1,2,3,4]
# print(sorted(a))

strs = ['aa','BB','zz','CC']
# print(sorted(strs))
# print(sorted(strs, reverse=True))


str_len = ['ccc','aaaa','d', 'bb']
# print(sorted(str_len,key=len ))


str_fun = ['xc','zb','yd','wa']

def Myfn(s):
    return s[-1]

print(sorted(str_fun, key=Myfn))