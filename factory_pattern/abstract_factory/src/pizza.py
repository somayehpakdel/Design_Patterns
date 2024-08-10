from abc import ABC, abstractmethod
from typing import List, Optional
from src.ingredients import (Cheese, Clams, Dough, Pepperoni, Sauce, Veggies)
from src.pizza_ingredient_factory import PizzaIngredientFactory


class Pizza(ABC):
    """
    Abstract base class for pizzas.
    """

    def __init__(self) -> None:
        self.name: str = ''
        self.dough: Optional[Dough] = None
        self.sauce: Optional[Sauce] = None
        self.veggies: List[Veggies]  = []
        self.cheese: Optional[Cheese] = None
        self.pepperoni: Optional[Pepperoni] = None
        self.clam: Optional[Clams] = None

    @abstractmethod
    def prepare(self) -> None:
        pass

    def bake(self) -> None:
        print("Bake for 25 minutes at 350")

    def cut(self) -> None:
        print("Cutting the pizza into diagonal slices")

    def box(self) -> None:
        print("Place pizza in official PizzaStore box")

    def set_name(self, name) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name


class CheesePizza(Pizza):
    """
    Concrete implementation of a cheese pizza.
    """

    def __init__(self, ingredientFactory: PizzaIngredientFactory):
        super().__init__()
        self.ingredientFactory = ingredientFactory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self.dough = self.ingredientFactory.createDough()
        print(f'Dough: {self.dough}')
        self.sauce = self.ingredientFactory.createSauce()
        print(f'Sauce: {self.sauce}')
        self.cheese = self.ingredientFactory.createCheese()
        print(f'Cheese: {self.cheese}')

class ClamPizza(Pizza) :
    def __init__(self, ingredientFactory: PizzaIngredientFactory):
        super().__init__()
        self.ingredientFactory = ingredientFactory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self.dough = self.ingredientFactory.createDough()
        print(f'Dough: {self.dough}')
        self.sauce = self.ingredientFactory.createSauce()
        print(f'Sauce: {self.sauce}')
        self.cheese = self.ingredientFactory.createCheese()
        print(f'Cheese: {self.cheese}')
        self.clam = self.ingredientFactory.createClam()
        print(f'Clam: {self.clam}')


class VeggiePizza(Pizza):
    def __init__(self, ingredientFactory: PizzaIngredientFactory):
        super().__init__()
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredientFactory.createDough()
        print(f'Dough: {self.dough}')
        self.sauce = self.ingredientFactory.createSauce()
        print(f'Sauce: {self.sauce}')
        self.cheese = self.ingredientFactory.createCheese()
        print(f'Cheese: {self.cheese}')
        self.veggies = self.ingredientFactory.createVeggies()
        print(f'Veggies: {self.veggies}')


class PepperoniPizza(Pizza):
    def __init__(self, ingredientFactory: PizzaIngredientFactory):
        super().__init__()
        self.ingredientFactory = ingredientFactory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self.dough = self.ingredientFactory.createDough()
        print(f'Dough: {self.dough}')
        self.sauce = self.ingredientFactory.createSauce()
        print(f'Sauce: {self.sauce}')
        self.cheese = self.ingredientFactory.createCheese()
        print(f'Cheese: {self.cheese}')
        self.veggies = self.ingredientFactory.createVeggies()
        print(f'Veggies: {self.veggies}')
        self.pepperoni = self.ingredientFactory.createPepperoni()
        print(f'Pepperoni: {self.pepperoni}')