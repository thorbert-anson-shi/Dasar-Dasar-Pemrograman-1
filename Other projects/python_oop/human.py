class Human():
    def __init__(self, name:str, gender:bool, age:int) -> None:
        """True for male and False for female"""
        self.name = name
        self.gender = "Male" if gender else "Female"
        self.age = age        

    def get_name(self):
        print(self.name)
        return self.name
    
    def get_gender(self):
        print(self.gender)
        return self.gender

    def get_age(self):
        print(self.age)
        return self.age

    def celebrate_birthday(self):
        self.age += 1

    def change_name(self, new_name:str):
        self.name = new_name

human1 = Human("Thorbert", True, 18)
human1.get_name()
human1.get_gender()
