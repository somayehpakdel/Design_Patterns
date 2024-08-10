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
        if pizza_type == "cheese":
            return NYStyleCheesePizza()
        elif pizza_type == "veggie":
            return NYStyleVeggiePizza()
        elif pizza_type == "clam":
            return NYStyleClamPizza()
        elif pizza_type == "pepperoni":
            return NYStylePepperoniPizza()
        else:
            return None

class ChicagoPizzaStore(PizzaStore):
    """
    A concrete implementation of PizzaStore that creates Chicago-style pizzas.
    """
    def create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        if pizza_type == "cheese":
            return ChicagoStyleCheesePizza()
        elif pizza_type == "veggie":
            return ChicagoStyleVeggiePizza()
        elif pizza_type == "clam":
            return ChicagoStyleClamPizza()
        elif pizza_type == "pepperoni":
            return ChicagoStylePepperoniPizza()
        else:
            return None