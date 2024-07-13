from src.subject import WeatherData
from src.observer import CurrentConditionsDisplay


def weather_station():
    weather_data = WeatherData()
    CurrentConditionsDisplay(weather_data)
    print('observers: ', weather_data.observers)
    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)

# Example usage:
if __name__ == "__main__":
    weather_station()