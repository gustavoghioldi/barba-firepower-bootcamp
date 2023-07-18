# def es como function
# self es como el this
# todos los metodos de las clases empiezan con self como 
# primer parametro (self es: si mismo)

from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, feets, color):
        self.__feets = feets
        self.__color = color

    #color esta sobre cargado
    @property
    def color(self):
        return f"es de color {self.__color}"
    @color.setter
    def color(self, color):
        self.__color = color
    
    @abstractmethod
    def talk(self):
        pass
    
    @abstractmethod
    def run(self):
        pass
    
class Bird(Animal):
    def talk(self):
        print("pio pio")
    def run(self):
        print("fly-walk-swimg")

class Fish (Animal):
    def talk(self):
        print("blue blue")
    def run(self):
        print("swimg")
    
    #sobre escritura de la propiedad color
    @property
    def color(self, color):
        self.__color = color

    @property
    def feets(self):
        return self.__feets
    @feets.setter
    def feets(self, feets):
        self.__feets = feets
        
    @staticmethod # no necesitan ser de una instancia
    def who_i_am():
        print("i am a Fish")

bird = Bird(4, "red")
print(bird.color)

fish = Fish(0, "yellow")
fish.run()

print(id(bird))
print(id(fish))
print(id(Fish))

