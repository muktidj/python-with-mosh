class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        speak = 'Everynight i always think of you bibeh'
        introduce = f"Hai gaiz, mi chiamo {self.name}, come ti chiama ?"
        print(introduce)


Mukti = Person('Mukti DJ')
Ayu = Person('Ayu Mukti')
Mukti.talk()
Ayu.talk()

# Person1 = Person('Mukti,')
# print(Person1.name)
# Person1.talk()
