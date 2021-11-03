from abc import ABC, abstractmethod 

class Animal(ABC):
   
    counter = 0
    @abstractmethod
    def reproduce(self):
        self.counter += 3
    
class Cat(Animal):
    def reproduce(self):
        self.counter += 6

whiskers = Cat()
whiskers.reproduce()
print(whiskers.counter)