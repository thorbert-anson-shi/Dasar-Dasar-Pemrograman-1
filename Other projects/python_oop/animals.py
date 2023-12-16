class Animal():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, "is eating...")

class Snake(Animal):
    def crawl(self):
        print(self.name, "is crawling...")

my_snake = Snake("bob", "13")
my_snake.eat()
my_snake.crawl()