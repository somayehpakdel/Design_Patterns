from abc import ABC, abstractmethod
"""
This module defines abstract base classes and concrete implementations for various
ingredients used in pizza recipes.
"""

class Dough(ABC):
    @abstractmethod
    def  __str__(self) -> str:
        pass


class ThinCrustDough(Dough):
    def __str__(self) -> str:
        return "Thin Crust Dough"


class ThickCrustDough(Dough):
    def __str__(self) -> str:
        return "Thick Crust Dough"


class Sauce(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class MarinaraSauce(Sauce):
    def __str__(self) -> str:
        return "Marinara Sauce"


class PlumTomatoSauce(Sauce):
    def __str__(self) -> str:
        return "Plum Tomato Sauce"


class Clams(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class FreshClams(Clams):
    def __str__(self) -> str:
        return "Fresh Clams"


class  FrozenClams(Clams):
    def __str__(self) -> str:
        return "Frozen Clams"


class Cheese(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class ReggianoCheese(Cheese):
    def __str__(self) -> str:
        return "Reggiano Cheese"


class MozzarellaCheese(Cheese):
    def __str__(self) -> str:
        return "Mozzarella Cheese"


class Veggies(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass
    
    def __repr__(self) -> str:
        return str(self.__class__.__name__).title()


class Garlic(Veggies):
    def __str__(self) -> str:
        return "Garlic"


class Onion(Veggies):
    def __str__(self) -> str:
        return "Onion"


class Mushroom(Veggies):
    def __str__(self) -> str:
        return "Mashroom"
    
    


class RedPepper(Veggies):
    def __str__(self) -> str:
        return "Red Pepper"


class BlackOlives(Veggies):
    def __str__(self) -> str:
        return 'Black Olive'


class Spinach(Veggies):
    def __str__(self) -> str:
        return "Spinach"


class Eggplant(Veggies):
    def __str__(self) -> str:
        return "Eggplant"


class Pepperoni(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class SlicedPepperoni(Pepperoni):
    def __str__(self) -> str:
        return "Sliced Pepperoni"
