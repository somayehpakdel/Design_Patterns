import unittest
from src.pizza_store import NYPizzaStore, ChicagoPizzaStore
from src.ingredients import *


class TestPizzaStore(unittest.TestCase):
    
    def setUp(self):
        """
        Sets up the test cases by creating instances of the pizza stores.
        This method is called before each test case is executed.
        """
        self.ny_pizza_store = NYPizzaStore()
        self.chicago_pizza_store = ChicagoPizzaStore()
    
    def test_ny_pizza_store(self):
        """
        Tests the New York pizza store by ordering a Veggie pizza and verifying
        that the pizza has the correct ingredients tyep.
        """

        pizza = self.ny_pizza_store.order_pizza('Veggie')
        self.assertEqual(pizza.name, 'New York Style Veggie Pizza')
        self.assertIsInstance(pizza.dough, Dough)
        self.assertIsInstance(pizza.sauce, Sauce)
        self.assertIsInstance(pizza.veggies[0], Garlic)
        self.assertIsInstance(pizza.veggies[1], Onion)
        self.assertIsInstance(pizza.veggies[2], Mushroom)
        self.assertIsInstance(pizza.veggies[3], RedPepper)
    
    def test_ny_pizza_store_invalid_pizza(self):
        """
        Tests the New York pizza store by ordering a Greek pizza, which should
        return None since the pizza is not supported.
        """
        pizza = self.ny_pizza_store.order_pizza('Greek')
        self.assertIsNone(pizza)

    def test_chicago_pizza_store(self):
        """
        Tests the Chicago pizza store by ordering a Pepperoni pizza and verifying
        that the pizza has the correct ingredients tyep.
        """

        pizza = self.chicago_pizza_store.order_pizza('Pepperoni')
        self.assertEqual(pizza.name, 'Chicago Style Pepperoni Pizza')
        self.assertIsInstance(pizza.dough, Dough)
        self.assertIsInstance(pizza.sauce, Sauce)
        self.assertIsInstance(pizza.veggies[0], BlackOlives)
        self.assertIsInstance(pizza.veggies[1], Spinach)
        self.assertIsInstance(pizza.veggies[2], Eggplant)

    def test_chicago_pizza_store_invalid_pizza(self):
        """
        Tests the Chicago pizza store by ordering a Greek pizza, which should
        return None since the pizza is not supported.
        """
        pizza = self.chicago_pizza_store.order_pizza('Greek')
        self.assertIsNone(pizza)


if __name__ == '__main__':
    unittest.main()