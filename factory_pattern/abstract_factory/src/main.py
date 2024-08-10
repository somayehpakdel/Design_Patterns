from src.pizza_store import NYPizzaStore, ChicagoPizzaStore


if __name__ == '__main__':
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = ny_store.order_pizza('cheese')
    print('__________________')

    pizza = chicago_store.order_pizza('veggie')
    print('__________________')
    
    pizza = ny_store.order_pizza('Pepperoni')
    print('__________________')

    pizza = chicago_store.order_pizza('Pepperoni')
    print('__________________')

    pizza = ny_store.order_pizza('Greek')