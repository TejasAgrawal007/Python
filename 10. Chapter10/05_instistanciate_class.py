class Employee:
    company = "Google"
    salary = 100

Tejas = Employee()
Akash = Employee()

# Creating instance attribute salary for both the objects
# Tejas.salary = 300
# Akash.salary = 400
Tejas.salary = 45
print(Tejas.salary)
print(Akash.salary)

# Below line throws an error as address is not present in instance/class 
# print(Akash.address) 