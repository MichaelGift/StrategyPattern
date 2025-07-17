class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observer attached: {observer.__class__.__name__}")

    def detach(self, observer):
        try:
            self._observers.remove(observer)
            print(f"Observer detached: {observer.__class__.__name__}")
        except ValueError:
            pass  # Observer not found

    def notify(self):
        print("Notifying observers...")
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify()  # Notify observers when measurements change
