from observer.observers import CurrentConditionsDisplay, ForecastDisplay
from observer.subject import WeatherStation

if __name__ == "__main__":
    weather_station = WeatherStation()
    current_display = CurrentConditionsDisplay(weather_station)
    forecast_display = ForecastDisplay(weather_station)
    # We already attached them in their __init__ methods for convenience
    print("\nFirst weather update:")
    weather_station.set_measurements(25, 65, 1012)

    print("\nSecond weather update:")
    weather_station.set_measurements(28, 70, 1010)

    print("\nDetaching Current Conditions Display:")
    weather_station.detach(current_display)

    print("\nThird weather update (Current Conditions Display should not update):")
    weather_station.set_measurements(22, 60, 1015)
