from abc import ABC, abstractmethod
from typing import Optional

from src.pizza import CheesePizza, ClamPizza, PepperoniPizza, VeggiePizza
from src.pizza_ingredient_factory import (ChicagoPizzaIngredientFactory,
                                        NYPizzaIngredientFactory)
from src.pizza import Pizza

class PizzaStore(ABC):
    city: str
    """
    Abstract base class for pizza stores.

    This class defines the common behavior for all pizza stores,
    including the order_pizza method, which handles the process
    of creating, preparing, baking, cutting, and boxing a pizza.
    """

    def order_pizza(self, pizza_type: str) -> Optional[Pizza]:
        """
        Orders a pizza of the specified type.

        Args:
            pizza_type (str): The type of pizza to order.

        Returns:
            Pizza: The prepared pizza.
        """
        pizza = self.create_pizza(pizza_type.lower())
        if pizza is None:
            print(f'A customer from {self.city} ordered a {pizza_type} pizza')
            print(f"Sorry, we don't have {pizza_type} pizza.")
            return None
        print(f'A customer from {self.city} ordered a {pizza.get_name()}')
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        """
        Creates a pizza of the specified type.

        Args:
            pizza_type (str): The type of pizza to create.

        Returns:
            Pizza: The created pizza.
        """
        pass


class NYPizzaStore(PizzaStore):
    city = "New York"
    """
    Concrete implementation of a pizza store for New York-style pizzas.
    """

    def create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        """
        Creates a New York-style pizza of the specified type.

        Args:
            item (str): The type of pizza to create.

        Returns:
            Pizza: The created New York-style pizza.
        """

        ingredient_factory = NYPizzaIngredientFactory()
        pizza: Optional[Pizza] = None
        if pizza_type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("New York Style Cheese Pizza")
        elif pizza_type == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("New York Style Veggie Pizza")
        elif pizza_type == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("New York Style Clam Pizza")
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("New York Style Pepperoni Pizza")

        return pizza


class ChicagoPizzaStore(PizzaStore):
    city = "Chicago"
    """
    Concrete implementation of a pizza store for Chicago-style pizzas.
    """

    def create_pizza(self, pizza_type: str) -> Optional[Pizza]:
        """
        Creates a Chicago-style pizza of the specified type.

        Args:
            item (str): The type of pizza to create.

        Returns:
            Pizza: The created Chicago-style pizza.
        """

        ingredient_factory = ChicagoPizzaIngredientFactory()
        pizza: Optional[Pizza] = None

        if pizza_type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("Chicago Style Cheese Pizza")
        elif pizza_type == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("Chicago Style Veggie Pizza")
        elif pizza_type == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("Chicago Style Clam Pizza")
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("Chicago Style Pepperoni Pizza")

        return pizza