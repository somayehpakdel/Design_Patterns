from src.beverage import Espresso, DarkRoast, HouseBlend
from src.condiment_decorator import Mocha, Whip, Soy

if __name__ == "__main__":
    
    #create an Espresso with no condiments
    beverage = Espresso()
    print(f"{beverage.get_description()} ${beverage.cost()}")

    #be careful about variables reassigning, beacause it will change the data types
    #so, it's better to create a new variable for each condiment
    #create a DarkRoast with condiments
    dark_rost = DarkRoast()
    dark_rost_mocha = Mocha(dark_rost)
    dark_rost_mocha = Mocha(dark_rost_mocha)
    dark_rost_mocha_whip = Whip(dark_rost_mocha)
    print(f"{dark_rost_mocha_whip.get_description()} ${dark_rost_mocha_whip.cost()}")

    #create a HouseBlend with condiments
    house_blend = HouseBlend()
    house_blend_soy = Soy(house_blend)
    house_blend_soy_mocha = Mocha(house_blend_soy)
    house_blend_soy_mocha_whip = Whip(house_blend_soy_mocha)
    print(f"{house_blend_soy_mocha_whip.get_description()} ${house_blend_soy_mocha_whip.cost()}")