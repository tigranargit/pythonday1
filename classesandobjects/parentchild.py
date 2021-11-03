#parent class

class Animal:
    counter = 0
    def __init__(self,legcount,canfly, species):
        self.legcount = legcount
        self.canfly = canfly
        self.species = species

    def reproduce(self):
        self.counter += 1

#polymorphism and overriding 

class Rabbits(Animal): #Rabbits class take from Animal class
    def reproduce(self):
        self.counter += 6 #we override the counter for rabbits 

horse1 = Animal("4", "False", "Horse")
horse1.reproduce()
horse1.reproduce()
horse1.reproduce()
print(horse1.counter)

bugs_bunny = Rabbits("4","False","Rabbit")
bugs_bunny.reproduce()
bugs_bunny.reproduce()
bugs_bunny.reproduce()
print(bugs_bunny.counter)


#child class

#class Fish:
 #   def __init__(self, legcount, canfly, species, fincount, colour):
  #      super().__init__(legcount, canfly, species)
   #     self.fincount = fincount
    #    self.colour = colour

    #def canSwim(self):
    #    return "I can swim"

#bird1 = Animal("2", "True", "Parrots")
#shark = Fish("0", "False", "Shark", "2", "Blue")