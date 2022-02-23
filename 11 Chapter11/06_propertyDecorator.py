class Employee:
    company = "Google"
    salary = 5000
    slaryBonus = 500
    # totalSalary = 5500

    @property
    def totalSalary(self):
        return self.salary + self.slaryBonus

    @totalSalary.setter
    def totalSalary(self, value):
        self.salaryBonus = value - self.salary


# Creating an Object
e = Employee()
# print(e.totalSalary())
print(e.totalSalary)


e.totalSalary = 4000
print(e.salary)
print(e.salaryBonus)
