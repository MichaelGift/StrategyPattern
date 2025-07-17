from .interface import WeatherDisplay


class CurrentConditionsDisplay(WeatherDisplay):
    def __init__(self, weather_station):
        self._weather_station = weather_station
        self._temperature = None
        self._humidity = None
        weather_station.attach(self)  # Attach self to the subject

    def update(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self.display()

    def display(self):
        print(f"Current Conditions: {self._temperature}°C, {self._humidity}% humidity")


class ForecastDisplay(WeatherDisplay):
    def __init__(self, weather_station):
        self._weather_station = weather_station
        self._forecast = "Sunny"  # Simplified
        weather_station.attach(self)

    def update(self, temperature, humidity, pressure):  # Logic to update forecast based on new data
        self._forecast = "Rainy" if temperature < 10 else "Sunny"
        self.display()

    def display(self):
        print(f"Weather Forecast: {self._forecast}")
