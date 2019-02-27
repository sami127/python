import re
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern,test_string)
# if result:
#     print('success')
# else:
#     print('not matched')

#re.findall()
string = "hello 12 hi 89, Howdy 34"
pattern = '\d+' #[1315646468]
result = re.findall(pattern, string)
# print(result)


#re.split()
string_1 = "Twelve:12 Eighty nine:89 ."
pattern = '\d+'
result_1 = re.split(pattern, string_1) 
# print(result_1)

#re.search()
string_2 = "Python is good"
pattern = '\APython'   #---\APython 
r = re.search(pattern,string_2)
# if r:
#     print('matched')
# else:
#     print('not matched')


string_3 = "19524 256, 4567 1234"
pattern = '(\d{3}) (\d{2})' 
m = re.search(pattern, string_3)
if m:
    print(m.group())
else:
    print('not matched')  
