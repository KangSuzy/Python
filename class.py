class Lion:
    color:""
    area:""
    def crying(self):
        print("으르렁")
    def eat(self):
        print("냠냐미")

dsLion = Lion()

dsLion.color = "orange"
dsLion.area = "seoul"

print(dsLion.color)
print(dsLion.area)

dsLion.crying()
dsLion.eat()

class animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def say(self):
        print("Hi!", self.name)
class Dog(animal):
    pass
class Cat(animal):
    pass

dog = Dog('댕댕', '갈색')
cat = Cat('냥냥', '검은색')

dog.say()
cat.say()

class animals:
    def __init__(self, name, color):
        self.name = name
        self.color =color

class Dogs(animals):
    def say(self):
        print("멍멍!")

class Cats(animals):
    def say(self):
        print("냐옹~")
        
dog = Dogs("댕댕이","누런색")
cat = Cats("냥냥이", "껌정색")

dog.say()
cat.say()
