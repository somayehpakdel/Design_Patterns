from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def register_observer(self, o):
        pass
    
    @abstractmethod
    def remove_observer(self, o):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass


class WeatherData(Subject):
    def __init__(self):
        self.observers = set()
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def register_observer(self, o):
        self.observers.add(o)

    def remove_observer(self, o):
        self.observers.remove(o)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()