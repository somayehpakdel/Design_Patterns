import unittest
from src.pizza_store import NYPizzaStore, ChicagoPizzaStore
from src.ny_style_pizza import NYStyleCheesePizza, NYStyleVeggiePizza
from src.chicago_style_pizza import ChicagoStyleCheesePizza, ChicagoStyleVeggiePizza


class TestPizzaStore(unittest.TestCase):
    
    def setUp(self) -> None:
        """
        Set up the test case by creating instances of the pizza stores.
        """
        self.ny_store = NYPizzaStore()
        self.chicago_store = ChicagoPizzaStore()
    
    def test_ny_store_order_cheese_pizza(self):
        """
        Test ordering a cheese pizza from the New York pizza store.
        """
        pizza = self.ny_store.order_pizza("cheese")
        self.assertIsNotNone(pizza)
        self.assertIsInstance(pizza, NYStyleCheesePizza)
        self.assertEqual(pizza.name, "NY Style Sauce and Cheese Pizza")

    def test_ny_store_order_veggie_pizza(self):
        """
        Test ordering a veggie pizza from the New York pizza store.
        """
        pizza = self.ny_store.order_pizza("veggie")
        self.assertIsNotNone(pizza)
        self.assertIsInstance(pizza, NYStyleVeggiePizza)
        self.assertEqual(pizza.name, "NY Style Veggie Pizza")

    def test_chicago_store_order_cheese_pizza(self):
        """
        Test ordering a cheese pizza from the Chicago pizza store.
        """
        pizza = self.chicago_store.order_pizza("cheese")
        self.assertIsInstance(pizza, ChicagoStyleCheesePizza)
        self.assertEqual(pizza.name, "Chicago Style Deep Dish Cheese Pizza")
        self.assertIsInstance(pizza, ChicagoStyleCheesePizza)

    def test_chicago_store_order_veggie_pizza(self):
        """
        Test ordering a veggie pizza from the Chicago pizza store.
        """
        pizza = self.chicago_store.order_pizza("veggie")
        self.assertIsInstance(pizza, ChicagoStyleVeggiePizza)
        self.assertEqual(pizza.name, "Chicago Style Veggie Pizza")
        self.assertIsInstance(pizza, ChicagoStyleVeggiePizza)

    def test_ny_store_order_invalid_pizza(self):
        """
        Test ordering an invalid pizza type from the New York pizza store.
        """
        pizza = self.ny_store.order_pizza("invalid_pizza")
        self.assertIsNone(pizza)

    def test_chicago_store_order_invalid_pizza(self):
        """
        Test ordering an invalid pizza type from the Chicago pizza store.
        """
        pizza = self.chicago_store.order_pizza("invalid_pizza")
        self.assertIsNone(pizza)


if __name__ == '__main__':
    unittest.main()