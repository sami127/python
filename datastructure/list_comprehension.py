
pow2 = [2**x for x in range(10)]
# print(pow2)
# pow2 = []
# for x in range(10):
#     pow2.append(2 ** x)
# pow2

r = [x+y for x in ['python', 'c'] for y in ['language','programming']]
#['pythonlanguage', 'pythonprogramming', 'clanguage', 'cprogramming']
print(r)
# res = []
# for x in ['python', 'c']:
#     for y in ['language','programming']:
#         res.append(x+y)

# OUtput:
# [python language, c programming]