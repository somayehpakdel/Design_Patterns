from src.pizza import Pizza


class ChicagoStyleCheesePizza(Pizza):
    """
    A subclass representing Chicago-style cheese pizza.
    """

    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")


class ChicagoStylePepperoniPizza(Pizza):
    """
    A subclass representing Chicago-style Pepperoni Pizza
    """

    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Pepperoni Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Pepperoni")


class ChicagoStyleClamPizza(Pizza):
    """
    A subclass representing Chicago-style clam pizza.
    """

    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Clam Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Clams")


class ChicagoStyleVeggiePizza(Pizza):
    """
    A subclass representing Chicago-style Veggie pizza.
    """

    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Veggie Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Black Olives")
        self.toppings.append("Spinach")
        self.toppings.append("Eggplant")