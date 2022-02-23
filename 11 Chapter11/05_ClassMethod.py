class Employee:
    company = "Airbnb"
    salary = 100
    location = "Delhi"

    # def changeSalary(self, sal):
        # self.__class__.salary = sal  # Dunder Method

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal


e = Employee()
print(e.salary)
e.changeSalary(786)
print(e.salary)