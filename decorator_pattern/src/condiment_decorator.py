from abc import ABC, abstractmethod
from src.beverage import Beverage

class CondimentDecorator(Beverage, ABC):
    def __init__(self, beverage: Beverage):
        self.beverage: Beverage = beverage

    @abstractmethod
    def get_description(self) -> str:
        pass


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage: Beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return self.beverage.cost() + 0.20


class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage: Beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Whip"

    def cost(self) -> float:
        return self.beverage.cost() + 0.10


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage: Beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Soy"

    def cost(self) -> float:
        return self.beverage.cost() + 0.15