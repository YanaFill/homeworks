class CelsiusTemperatureSensor:
    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature_celsius(self):
        return self._temperature


class FahrenheitTemperatureSensor:
    def __init__(self):
        self._temperature = 77

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature_fahrenheit(self):
        return self._temperature


class TemperatureSensorAdapter(FahrenheitTemperatureSensor):
    def __init__(self, fahrenheit_sensor):
        super().__init__()
        self._fahrenheit_sensor = fahrenheit_sensor

    def get_temperature_celsius(self):
        return (self._fahrenheit_sensor.get_temperature_fahrenheit() - 32) * 5 / 9


def display_temperature(sensor):
    print(f"Temperature: {sensor.get_temperature_celsius():.2f} °C")


fahrenheit_sensor = FahrenheitTemperatureSensor()

adapter = TemperatureSensorAdapter(fahrenheit_sensor)

print(f"Temperature: {adapter.get_temperature_celsius():.2f} °C")
