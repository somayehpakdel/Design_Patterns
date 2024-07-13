from src.utils import DisplayElement
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temp, humidity, pressure):
        pass 


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.temperature = 0.0
        self.humidity = 0.0
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature}F degrees and {self.humidity}% humidity")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(temperature={self.temperature}, humidity={self.humidity})"