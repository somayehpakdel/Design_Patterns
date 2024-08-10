from abc import ABC, abstractmethod
from typing import List

from src.ingredients import *


class PizzaIngredientFactory(ABC):
    """
    Provides an abstract interface for creating a family of products (the ingredients).
    Each subclass implements the ingredients using its own regional suppliers.
    """

    @abstractmethod
    def createDough(self) -> Dough:
        pass

    @abstractmethod
    def createSauce(self) -> Sauce:
        pass

    @abstractmethod
    def createCheese(self) -> Cheese:
        pass

    @abstractmethod
    def createVeggies(self) -> List[Veggies]:
        pass

    @abstractmethod
    def createPepperoni(self) -> Pepperoni:
        pass

    @abstractmethod
    def createClam(self) -> Clams:
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    """
    Concrete implementation of the PizzaIngredientFactory for New York-style pizza ingredients.
    """

    def createDough(self) -> Dough:
        return ThinCrustDough()

    def createSauce(self) -> Sauce:
        return MarinaraSauce()

    def createCheese(self) -> Cheese:
        return ReggianoCheese()

    def createVeggies(self) -> List[Veggies]:
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def createPepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def createClam(self) -> Clams:
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    """
    Concrete implementation of the PizzaIngredientFactory for Chicago-style pizza ingredients.
    """

    def createDough(self) -> Dough:
        return ThickCrustDough()

    def createSauce(self) -> Sauce:
        return PlumTomatoSauce()

    def createCheese(self) -> Cheese:
        return MozzarellaCheese()

    def createVeggies(self) -> List[Veggies]:
        veggies = [BlackOlives(), Spinach(), Eggplant()]
        return veggies

    def createPepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def createClam(self) -> Clams:
        return FrozenClams()
