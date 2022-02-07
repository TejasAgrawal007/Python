# import pandas as pd
# pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")


TejasApplication = RailwayForm()
TejasApplication.name = "Tejas"
TejasApplication.train = "Rajdhani Express"
TejasApplication.printData()