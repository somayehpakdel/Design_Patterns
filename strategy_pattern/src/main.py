from src.duck import Duck
from src.fly_behavior import FlyWithWings, FlyNoWay, FlyRocketPowered
from src.quack_behavior import Quack


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck")


class MiniDuckSimulator:
    mallardDuck = MallardDuck()
    mallardDuck.display()
    mallardDuck.perform_fly()
    mallardDuck.perform_quack()


#Setting behavior dynamically
class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a model duck")


class MiniRocketSimulator:
    model = ModelDuck()
    model.display()
    model.perform_fly()
    model.set_fly_behavior(FlyRocketPowered())
    model.perform_fly()


def main():
    print('MiniDuckSimulator')
    MiniDuckSimulator()
    MiniRocketSimulator()


if __name__ == "__main__":
    main()
    