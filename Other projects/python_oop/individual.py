class Individual():
    def counter(self):
        print(self)

    def __init__(self, character_name) -> None:
        self.character_name = character_name
        self.happy = True
    
    def get_character_name(self):
        return self.character_name

    def is_happy(self):
        return self.happy

    def switch_mood(self):
        self.happy = not self.happy

    def speak(self):
        if self.happy == True:
            print(f"Hello, my name is {self.character_name}")
        else:
            print("Go away!")

individual1 = Individual("Buster")
individual2 = Individual("Tobias")
individual3 = Individual("Lucille")

individual1.counter()
