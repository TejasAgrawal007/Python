class progrmmmer:
    company = "Microsoft"


    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and product is {self.product}")


Tejas = progrmmmer("Tejas", "Github")
Siya = progrmmmer("Siya", "GitBasket")
Tejas.getInfo()
Siya.getInfo()