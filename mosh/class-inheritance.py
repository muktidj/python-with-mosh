class Animal:
    def eat(self):
        print("it is like fish")

class Dog(Animal):
    def cute(self):
        print('The cute dog')

class Cat(Animal):
    def love(self, name):
        self.name = name
        print(f'it is name {name}, it is female')


Dog1 = Dog()
Dog1.cute()

Cat1 = Cat()
Cat1.love('Tanzi')