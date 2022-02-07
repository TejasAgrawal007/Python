class Employee:
    company = "Google"
    salary = 100

Tejas = Employee()
rajni = Employee()
Tejas.salary = 300
rajni.salary = 400

print(Tejas.company)
print(rajni.company)
Employee.company = "YouTube"
print(Tejas.company)
print(rajni.company)
print(Tejas.salary)
print(rajni.salary)