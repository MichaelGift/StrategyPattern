from abc import ABC, abstractmethod


class WeatherDisplay(ABC):  # Abstract base class acting as an interface
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass
