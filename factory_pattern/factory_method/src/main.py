from src.pizza_store import NYPizzaStore, ChicagoPizzaStore

if __name__ == '__main__':
    ny_store = NYPizzaStore()
    pizza = ny_store.order_pizza('cheese')
    if pizza is None:
        print("Sorry, we don't have this type of pizza")
    else:
        print(f"Ethan ordered a {pizza.get_name()}\n")

    pizza = ny_store.order_pizza('veggie')
    if pizza is None:
        print("Sorry, we don't have this type of pizza")
    else:
        print(f"Joel ordered a {pizza.get_name()}\n")

    chicago_store = ChicagoPizzaStore()
    pizza = chicago_store.order_pizza("cheese")
    if pizza is None:
        print("Sorry, we don't have this type of pizza")
    else:
        print(f"Ethan ordered a {pizza.get_name()}\n")

    pizza = chicago_store.order_pizza("veggie")
    if pizza is None:
        print("Sorry, we don't have this type of pizza")
    else:
        print(f"Joel ordered a {pizza.get_name()}\n")
