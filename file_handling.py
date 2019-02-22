# f = open('test.txt','w')
# r = open('test.txt', mode='r', encoding='UTF-8')
# print(r.read())

with open('new_write.txt','w',encoding='UTF-8') as f:
    f.write('my new write fil\n')
    f.write('THis is file')
    f.close()

r = open('new_write.txt', mode='r', encoding='UTF-8')
print(r.read())    

