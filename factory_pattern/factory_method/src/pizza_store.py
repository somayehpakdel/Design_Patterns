from abc import ABC, abstractmethod

from src.chicago_style_pizza import (ChicagoStyleCheesePizza,
                                    ChicagoStyleClamPizza,
                                    ChicagoStylePepperoniPizza,
                                    ChicagoStyleVeggiePizza)
from src.ny_style_pizza import (NYStyleCheesePizza, NYStyleClamPizza,
                                NYStylePepperoniPizza, NYStyleVeggiePizza)
from src.pizza import Pizza
from typing import Optional


class PizzaStore(ABC):
    """
    The base class for all pizza stores, responsible for ordering pizzas.
    """

    def order_pizza(self, pizza_type: str) -> Optional[Pizza]:
        pizza = self.create_pizza(pizza_type.lower())
        if pizza is not None:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        pass


class NYPizzaStore(PizzaStore):
    """
    A concrete implementation of PizzaStore that creates New York-style pizzas.
    """

    def create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        pizza: Optional[Pizza] = None
        if pizza_type == "cheese":
            pizza = NYStyleCheesePizza()
        elif pizza_type == "veggie":
            pizza = NYStyleVeggiePizza()
        elif pizza_type == "clam":
            pizza =  NYStyleClamPizza()
        elif pizza_type == "pepperoni":
            pizza =  NYStylePepperoniPizza()
        return pizza

class ChicagoPizzaStore(PizzaStore):
    """
    A concrete implementation of PizzaStore that creates Chicago-style pizzas.
    """
    def create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        pizza: Optional[Pizza] = None
        if pizza_type == "cheese":
            pizza = ChicagoStyleCheesePizza()
        elif pizza_type == "veggie":
            pizza = ChicagoStyleVeggiePizza()
        elif pizza_type == "clam":
            pizza = ChicagoStyleClamPizza()
        elif pizza_type == "pepperoni":
            pizza = ChicagoStylePepperoniPizza()
        return pizza