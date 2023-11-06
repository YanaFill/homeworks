def StudentInit(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

def StudentGreet(self):
    print(f"Hi, I'm {self.name}.")

def StudentDescription(self):
    print(f"I'm a {self.gender} student, {self.age} years old.")

attrs = {
    'team': "Python31",
    '__init__': StudentInit,
    'greet': StudentGreet,
    'description': StudentDescription
}

Student = type('Student', (), attrs)

student = Student("Jon", 21, "Male")
student.greet()
student.description()
