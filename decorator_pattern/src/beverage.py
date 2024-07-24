from abc import ABC, abstractmethod

class Beverage(ABC):
    def __init__(self) -> None:
        self.description: str = "Unknown Beverage"

    def get_description(self) -> str:
        return self.description

    @abstractmethod
    def cost(self) -> float:
        pass


class Espresso(Beverage):
    def __init__(self):
        self.description: str = "Espresso"

    def cost(self) -> float:
        return 1.99

class HouseBlend(Beverage):
    def __init__(self) -> None:
        self.description: str = "House Blend Coffee"

    def cost(self) -> float:
        return 0.89

class DarkRoast(Beverage):
    def __init__(self) -> None:
        self.description: str = "Dark Roast Coffee"

    def cost(self) -> float:
        return 1.49