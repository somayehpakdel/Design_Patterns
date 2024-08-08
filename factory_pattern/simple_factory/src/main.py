from src.pizza import Pizza, CheesePizza, PepperoniPizza, ClamPizza, VeggiePizza

class SimplePizzaFactory:
    """
    A simple factory class that creates pizza instances based on the provided type.
    """
    def create_pizza(self, item: str) -> Pizza :
        """
        Creates a pizza object based on the provided item.
        
        Args:
            item(str): The type of pizza to create(e.g., "cheese", "pepperoni", "clam", "veggie")
        Returns:
            Pizza: The created pizza object.
        """
        pizza: Pizza
        if item == "cheese":
            pizza = CheesePizza()
        elif item == "pepperoni":
            pizza = PepperoniPizza()
        elif item == "clam":
            pizza = ClamPizza()
        elif item == "veggie":
            pizza = VeggiePizza()
        return pizza

class PizzaStore:
    """
    Responsible for ordering and prepairing pizzas.
    """
    def __init__(self, factory: SimplePizzaFactory):
        self.factory = factory

    def order_pizza(self, item: str) -> Pizza:
        pizza = self.factory.create_pizza(item)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


if __name__=="__main__":
    factory = SimplePizzaFactory()
    pizza = PizzaStore(factory).order_pizza(item='cheese')
