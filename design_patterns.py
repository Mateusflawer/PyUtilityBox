from abc import ABC, abstractmethod


# Singleton: SensorManager

class SensorManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SensorManager, cls).__new__(cls)
            cls._instance._sensors = []
        return cls._instance

    def add_sensor(self, sensor):
        self._sensors.append(sensor)

    def remove_sensor(self, sensor):
        self._sensors.remove(sensor)

    def get_sensors(self):
        return self._sensors


# Factory Method: SensorFactory

class Sensor(ABC):
    def __init__(self, name):
        self.name = name
        self.data = None

    @abstractmethod
    def read_data(self):
        pass

    def get_data(self):
        return self.data

class TemperatureSensor(Sensor):
    def read_data(self):
        self.data = "36°C"
        return self.data

class HumiditySensor(Sensor):
    def read_data(self):
        self.data = "60%"
        return self.data

class SensorFactory:
    @staticmethod
    def create_sensor(sensor_type, name):
        if sensor_type == 'temperature':
            return TemperatureSensor(name)
        elif sensor_type == 'humidity':
            return HumiditySensor(name)
        else:
            raise ValueError("Unknown sensor type")


# Observer: SensorObserver

class SensorObserver:
    def update(self, sensor):
        pass

class Display(SensorObserver):
    def update(self, sensor):
        print(f"Display: Sensor {sensor.name} has new data: {sensor.get_data()}")

class Alarm(SensorObserver):
    def update(self, sensor):
        if sensor.get_data() > "30°C":  # Exemplo simplificado
            print(f"Alarm: Sensor {sensor.name} is too hot!")

class ObservableSensor(Sensor):
    def __init__(self, sensor):
        super().__init__(sensor.name)
        self.sensor = sensor
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    def read_data(self):
        self.sensor.read_data()
        self.data = self.sensor.get_data()
        self.notify_observers()
        return self.data


if __name__ == "__main__":
    # Criar o gerenciador de sensores (Singleton)
    sensor_manager = SensorManager()

    # Criar sensores usando o Factory Method
    temp_sensor = SensorFactory.create_sensor('temperature', 'TempSensor1')
    humidity_sensor = SensorFactory.create_sensor('humidity', 'HumiditySensor1')

    # Adicionar sensores ao gerenciador
    sensor_manager.add_sensor(temp_sensor)
    sensor_manager.add_sensor(humidity_sensor)

    # # Criar observadores
    display = Display()
    alarm = Alarm()

    # Converter sensores para sensores observáveis
    observable_temp_sensor = ObservableSensor(temp_sensor)
    observable_humidity_sensor = ObservableSensor(humidity_sensor)

    # Adicionar observadores aos sensores
    observable_temp_sensor.add_observer(display)
    observable_temp_sensor.add_observer(alarm)
    observable_humidity_sensor.add_observer(display)

    # Ler dados dos sensores e notificar observadores
    observable_temp_sensor.read_data()
    observable_humidity_sensor.read_data()

