from src.beverage import Espresso, DarkRoast, HouseBlend
from src.condiment_decorator import Mocha, Whip, Soy

if __name__ == "__main__":
    
    #create an Espresso with no condiments
    beverage = Espresso()
    print(f"{beverage.get_description()} ${beverage.cost()}")

    #create a DarkRoast with condiments
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f"{beverage2.get_description()} ${beverage2.cost()}")

    #create a HouseBlend with condiments
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"{beverage3.get_description()} ${beverage3.cost()}")