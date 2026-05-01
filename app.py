
class Hero:
    def __init__(self, name, happiness, saturation):
        self.name = name
        self.happiness = happiness
        self.saturation = saturation
    def check_status(self): 
        print(self.happiness)
    def play(self):
        self.saturation -= 20
        self.happiness += 15  
        print (self.saturation)
        print (self.happiness)
    def feed(self):
            x = input("What would you like to feed your pet?")
            for i in Food:
                if x == "Apple":
                    self.saturation += 10
                elif x == "Bread":
                    self.saturation += 15
                elif x == "Sandwich":
                    self.saturation += 20
                elif x == "Burger":
                   self.saturation += 25
            print (self.saturation)
Food = ["Apple", "Bread", "Sandwich", "Burger"]
Daniel = Hero("Daniel",100,70)
b = input("Would you like to do something")
while b == "Yes":
    a = input("What would you like to do with your pet")
if a == "Feed":
    print (Food)
    Daniel.feed()
if a == "Check Status":
    Daniel.check_status()
if a == "Play":
    Daniel.play()
