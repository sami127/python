class Parrot:

    def __init__(self):
        self.__price = 2000 
    
    def print_price(self):
        print('Sell price : ', self.__price)

    def change_price(self, price):
        self.__price = price


     


    def fly(self):
        print('Parrot can fly')
    def swim(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("Penguin can'n fly")
    def swim(self):
        print("Penguin can swim") 

#common interface
def flying_test(bird):
    bird.fly()        

p = Parrot()
p.__price = 3000
p.change_price(p.__price)
p.print_price()





pen = Penguin()

flying_test(p)
flying_test(pen)

