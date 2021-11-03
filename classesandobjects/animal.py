#class Animal:
 #   species = "Dog"

    #def isPet(self):
     #   print("True")
    
    #eyes = "Blue"
    #colour = "Brown"
    #teeth = "15"

#benji_sausage = Animal()
#meow = Animal()
#meow.species = "Cat"
#print(meow.species)

#print(benji_sausage.species)
#benji_sausage.isPet()
#print(benji_sausage.teeth)

class Animal:
    def __init__(self, species, isPet, eyes, colour, teeth):
        self.species = species
        self.isPet = isPet
        self.eyes = eyes
        self.colour = colour
        self.teeth = teeth

benji_sausage = Animal("Dog", "True","Blue", "Brown", 15)
fluffy = Animal("Cat", "True", "Green", "White", 20)

print ("This is Benji:  ",benji_sausage.species)
print ("This is Fluffy:  ",fluffy.species)

