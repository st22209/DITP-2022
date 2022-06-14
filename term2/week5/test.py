# make a person class that has 3 attributes: firstname, lastname, and age

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"Hey! My name is {self.firstname} {self.lastname} and I am {self.age} years old"

    def __add__(self, other_person):
        if isinstance(other_person, self.__class__):
            return self.age + other_person.age