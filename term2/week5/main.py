class Person:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def say_hi(self):
        print(f"{self.fullname} says never gonna give you up!")

person = Person("Rick", "Astley")

print(person.firstname)
print(person.fullname)

person.say_hi()


class CoolUsefulClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def add(self):
        return self.x + self.y


super_cool_variable = CoolUsefulClass(10, 20)
print(super_cool_variable.add())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hey! My name is {self.name} and I am {self.age} years old" 


person1 = Person("Rick Astley", 42)
print(person1)

del person1.age
print(person1.age)

class Employee:
    def __init__(self, firstname, lastname, salary, emp_id):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.emp_id = emp_id

    def __str__(self):
        return f"Employee Info:\n\nEmployee ID: {self.emp_id}\nFirstname: {self.firstname}\nLastname: {self.lastname}\nSalary: {self.salary}"

    def give_raise(self):
        old_salary = self.salary
        self.salary = old_salary * 1.15 # increase salary by 15% (give 15% raise)

        print(f"Employee's salary has been updated! from {old_salary} to {self.salary}")

    def __add__(self, other_employee):
        if isinstance(other_employee, self.__class__):
            return self.salary + other_employee.salary

employee1 = Employee("Person", "Lastname", 100_000, 1)
employee2 = Employee("Cool", "Person", 150_000, 3)

print(employee1+employee2)

employee1.__add__(employee1, employee2)

def add(x: int, y: int) -> int:
    """
    This function takes 2 numbers and returns the sum

    Parameters
    ----------
        x (int): the first number
        y (int): the second number
    
    Returns
    -------
        int: The sum of the 2 numbers 
    """
    return x + y


class Manager(Employee):
    def __init__(self, firstname, lastname, salary, emp_id):
        super().__init__(firstname, lastname, salary, emp_id)
        
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def remove_employee(self, employee):
        self.employee_list.remove(employee)

    # Overwrite the Employee classes str method with our own:
    def __str__(self):
        return f"Manager Info: Manager is cool"


manager1 = Manager("Person", "Lastname", 100_000, 1)       
manager1.add_employee(employee1)
manager1.add_employee(employee2)

print(manager1.employee_list)
print(manager1.employee_list[0].salary)

