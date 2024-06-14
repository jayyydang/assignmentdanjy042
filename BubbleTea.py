from abc import ABC, abstractmethod

class BBT(ABC):
    def __init__(self, name, size, iceLevel, sugarLevel, tea):
        self.__name = name
        self.__size = size 
        self.__iceLevel = iceLevel
        self.__sugarLevel = sugarLevel
        self.__tea = tea # string representing the type of tea (green or black)
        self.__toppings = [] # add toppings to the list after the object is created
        self.__price = 0 # initialise to 0 and calculate it with calculatePrice()


    def addToppings(self, topping):
        self.__toppings.append(topping)

    def removeTopping(self, topping):
        if topping in self.__toppings:
            self.__toppings.remove(topping)
        else: 
            print ("Couldnt find topping to remove")

    def calculatePrice(self):
        pass


    hello test