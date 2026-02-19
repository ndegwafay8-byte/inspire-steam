#Name : Faith Nyambura
# Date : 19/02/2026
# 



def cook_egg():
    oil = "20ml"
    pan = True
    moto = True
    eggs = 2

    print(f"the pan is {pan},and the fire is {moto}, add{oil}amount of oil and cook {eggs} eggs")

print("here is statement 1")

print("here is statement 2")
    
cook_egg()

print("here is statement 3")

# Bus fare creating function

def create_fare(route, distance, rush_hour):
    fare = distance * 10
    if rush_hour == True:
        fare = fare * 1.5
    print(f"the fare on route{route}, is {fare}")

rush_hour = True
create_fare("Juja_allsopes", 7, rush_hour)

# passing a list as a parameter
def write_all_interests(interest):
    for interest in interest:
        print(f"i am interested in {interest}")

all_interest = ["bike ridding","painting","poetry"]

write_all_interests(all_interest)
