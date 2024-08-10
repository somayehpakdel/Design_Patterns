from abc import ABC, abstractmethod
from typing import List


class Pizza(ABC):
    """
    The base class for all pizza types
    """

    @abstractmethod
    def __init__(self) -> None:
        self.name: str = ''
        self.dough: str = ''
        self.sauce: str = ''
        self.toppings: List[str] = []


    def prepare(self):
        print(f"Preparing {self.name}")
        print(f"Tossing dough: {self.dough}")
        print(f"Adding sauce: {self.sauce}")
        print("Adding toppings:")
        for topping in self.toppings:
            print(f" {topping}")


    def bake(self):
        print("Bake for 25 minutes at 350")


    def cut(self):
        print("Cutting the pizza into diagonal slices")


    def box(self):
        print("Place pizza in official PizzaStore box")

    def get_name(self) -> str:
        return self.name