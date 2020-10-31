## https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=2
class Employee:
    'Common base class for all employees'
    empCount = 0
    raise_amount = 1.04

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        Employee.empCount += 1

    @property
    def email(self):
        return('{}.{}@mycompany.com'.format(self.first, self.last))

    @property
    def fullname(self):
        return('{} {}'.format(self.first, self.last))

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = first
        self.last = last

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, salary = emp_str.split('-')
        return cls(first,last,salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return('{} {} {}'.format(self.first, self.last, self.salary))

    def __str__(self):
        return('{} - {}'.format(self.fullname, self.email))

    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.fullname())

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--> ', emp.fullname())

##    def displayCount(self):
##        #print ("Total Employee d%" % Employee.empCount )
##        print ("Total Employee ", Employee.empCount )
##
##    def displayEmployee(self):
##        print ("Name : ", self.name, ", Salary: ", self.salary)
##

emp1 = Employee('John', 'Smith', 20000)
emp2 = Employee("Manni", "Mukasa", 5000)

emp1.fullname = 'Mary Kola'

print(emp1.first)
print(emp1.email)
print(emp1.fullname)


##print(emp1.fullname())
##print(len(emp1))
##print(emp1.__repr__())
##print(emp1.__str__())

##dev1 = Developer('Joey', 'Smith', 20000, 'Python')
##dev2 = Developer("Mannie", "Mutabi", 5000, 'Java')
##
##mgr1 = Manager('David', 'Skype', 90000, [dev1])
##
##print(issubclass(Developer, Manager))

##print(isinstance(mgr1, Manager))

##mgr1.add_emp(dev2)
##mgr1.remove_emp(dev1)
##
##print(mgr1.email)
##mgr1.print_emps()

##print(help(Developer))

##print(dev1.email)
##print(dev1.prog_lang)

##import datetime
##my_date = datetime.date(2020, 10, 15)
##print (Employee.is_workday(my_date))



##emp_str_1 = 'John-Doe-70000'
####first, last, salary = emp_str_1.split('-')
##
##new_emp_1 = Employee.from_string(emp_str_1)
##
##print(new_emp_1.email)
##print(new_emp_1.salary)
##Employee.set_raise_amt(1.05)
##print (Employee.raise_amount)
##print (emp1.raise_amount)
##print (emp2.raise_amount)

##emp1.raise_amount = 1.05
##print (emp1.__dict__)
##print (Employee.raise_amount)
##print (emp1.raise_amount)
##print (emp2.raise_amount)
##print (emp1.email)
##print ('{} {}'.format(emp1.first, emp1.last))
##print (emp2.fullname())

##print (emp1.name)
###print (Employee.displayEmployee(emp_01))
##print (emp1.salary)
##
##
##emp1.displayEmployee()
##emp2.displayEmployee()
##print ("Total Employee %d" % Employee.empCount)
##emp1.age = 7
##print (emp1.age)
##hasattr(emp2, 'age')
##print ("Employee.__doc__:", Employee.__doc__ )
##print ("Employee.__name__:", Employee.__name__)
##print ("Employee.__module__:", Employee.__module__)
##print ("Employee.__bases__:", Employee.__bases__)
##print ("Employee.__dict__:", Employee.__dict__)
##print ("Total Employee %d" % Employee.empCount)