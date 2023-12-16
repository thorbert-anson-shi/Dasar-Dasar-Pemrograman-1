# A python class describes a set of objects with its own set of functions, methods, and properties
class Animal():
    def __init__(self, name:str, weight:int):
        self.name = name
        self.weight = weight

    def get_name(self):
        return self.name

# Entering the class name as a constructor argument means the subclass inherits properties of the superclass
class Cat(Animal):
    def sound(self):
        print("meow")

class Dog(Animal):
    def sound(self):
        print("bork")

my_cat = Cat("Allison", 54)
print(my_cat.get_name())
my_dog = Dog("Babushka", 50)

print(my_cat.__dict__)
print(my_dog.__dict__)
print("get woofed") if my_dog.weight > my_cat.weight else print("get meowed")