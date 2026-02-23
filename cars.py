#Name : Faith Nyambura
# Date : 23/02/2026
# program to show classes in python

class Car():
    # attribute of the car
    def __init__(self,model,make,color,year):    
        self.model = model
        self.make = make
        self.color = color
        self.year = year

# print car details
    def print_details(self,model,make,color,year):
        print(f"{make} {model} of color {color} was manufactured in {year}")



    #instantiate a class object


my_car = Car("Atenza","Mazda","Red",2022)
dads_car = Car("landcruiser","toyota","black",2024)

my_car.print_details("atenza","mazda","red",2022)
    

