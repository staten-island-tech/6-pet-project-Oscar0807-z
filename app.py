
class Hero:
    def __init__(self, name, happiness, saturation):
        self.name = name
        self.happiness = happiness
        self.saturation = saturation
    def check_status(self): 
        print(self.happiness)
Food = ["Apple", "Bread", "Sandwich", "Burger"]

options = ["Play","Feed","Check status"]
a = input("What would you like to do with your pet")
if a == "Feed":
    print (Food)
    x = input("What would you like to feed your pet?")
def feed():
    for i in Food:
        if x == "Apple":
            saturation += 10
        elif x == "Bread":
            saturation += 15
        elif x == "Sandwich":
            saturation += 20
        elif x == "Burger":
            saturation += 25
    print (saturation)
def play():
    saturation -= 20
    happiness += 15
def check_status():
    print (saturation)
    print (happiness)
def stats():
    if saturation <= 50:
        print ("Your pet is hungry")
    if happiness <= 50:
        print ("Your pet is unhappy")
