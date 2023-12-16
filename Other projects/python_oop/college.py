class Course():
    def __init__(self, name:str, sks:int) -> None:
        self.name = name
        self.sks = sks

    def __repr__(self):
        return self.name

class Person():
    def __init__(self, name:str, surname:str) -> None:
        self.name = name
        self.surname = surname

    def editInfo(self, name:str, surname:str):
        self.name = name
        self.surname = surname

class Student(Person):
    def __init__(self, name: str, surname: str) -> None:
        super().__init__(name, surname)
        self.courses = []

    def addCourse(self, course):
        self.courses.append(course)

class Teacher(Person):
    def __init__(self, name: str, surname: str, courses:list[Course], salary_info:int=0) -> None:
        super().__init__(name, surname)
        self.teaching_in_courses = courses
        self.salary_info = salary_info

    def addCourse(self, course):
        self.teaching_in_courses.append(course)

    def teach(self):
        [print(course) for course in self.teaching_in_courses]

ddp1 = Course("DDP1", 4)
matdis1 = Course("MatDis1", 3)
calculus = Course("Calculus", 2)
psd = Course("PSD", 4)

my_teacher = Teacher("Bob", "Manson", [psd, matdis1])
my_student = Student("Clement", "Tine")

my_student.addCourse(matdis1)
print(my_student.courses)

my_teacher.teach()