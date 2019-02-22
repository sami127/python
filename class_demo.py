
class Bird:
    type_of_bird = 'Parrot'

    def __init__(self):
        print('I am in init')
    
    def function(self):
        print('This msg is coming from function')

b_obj = Bird()
c_obj = Bird()
print(b_obj.type_of_bird)
print(b_obj.function())
