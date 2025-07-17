class CurrentConditionsDisplay:
    def __init__(self):
        self._temperature = 18
        self._humidity = 30

    def update(self, temperature, humidity, pressure):
        print(f"Temperature changed from {self._temperature}°C to {temperature}°C")
        self._temperature = temperature
        print(f"Humidity changed from {self._humidity}% to ${humidity}%")
        self._humidity = humidity
        self.display()

    def display(self):
        print(f"Current Conditions: {self._temperature}°C, {self._humidity}% humidity")


class ForecastDisplayer:
    def __init__(self):
        self._forecast = "Rainy"

    def update(self, temperature, humidity, pressure):
        forecast = "Rainy" if temperature < 10 else "Sunny"
        if forecast == self._forecast:
            print(f"Weather forecast stays the same: {self._forecast}")
        else:
            print(f"Weather forecast changes from {self._forecast} to {forecast}")
        self._forecast = forecast
        self.display()

    def display(self):
        print(f"Weather Forecast: {self._forecast}")


class WeatherStation:
    def __init__(self, current_condition: CurrentConditionsDisplay, forecast: ForecastDisplayer):
        self.cc_display = current_condition
        self.f_display = forecast

    def set_measurements(self, temperature, humidity, pressure):
        self.cc_display.update(temperature, humidity, pressure)
        self.f_display.update(temperature, humidity, pressure)


if __name__ == "__main__":
    cc_display = CurrentConditionsDisplay()
    f_display = ForecastDisplayer()
    station = WeatherStation(cc_display, f_display)

    station.set_measurements(9, 40, 90)
    station.set_measurements(15, 50, 100)
    station.set_measurements(20, 60, 110)

## Problems occur when you need to add new displays or change the way existing displays work.
## This is because the WeatherStation class is tightly coupled with the display classes.
## For example to add new display class you need to modify the WeatherStation class.


## To solve this, we can use the Observer Pattern to decouple the WeatherStation from the display classes.
