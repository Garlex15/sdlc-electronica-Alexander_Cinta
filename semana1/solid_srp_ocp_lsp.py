from abc import ABC, abstractmethod
from dataclasses import dataclass

# S - Principio de Responsabilidad Única
# Correcta: cada clase tiene una sola razón de cambio.
class SensorReader:
    def read(self, sensor_id: str) -> float:
        return 25.4

class DataLogger:
    def save(self, sensor_id: str, value: float) -> None:
        print(f"Guardando {sensor_id}: {value}")

class SensorService:
    def __init__(self, reader: SensorReader, logger: DataLogger) -> None:
        self._reader = reader
        self._logger = logger

    def process(self, sensor_id: str) -> None:
        value = self._reader.read(sensor_id)
        self._logger.save(sensor_id, value)

# Incorrecta: una clase mezcla lectura, persistencia y alertas.
class SensorMonitor:
    def read_and_log_and_alert(self, sensor_id: str) -> None:
        value = 25.4
        print(f"Guardando {sensor_id}: {value}")
        print(f"Alerta para {sensor_id}")

# O - Principio Abierto/Cerrado
# Correcta: se pueden agregar nuevas estrategias sin modificar AnomalyDetector.
class AlertStrategy(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        ...

class ConsoleAlert(AlertStrategy):
    def send(self, message: str) -> None:
        print(f"[console] {message}")

class FileAlert(AlertStrategy):
    def send(self, message: str) -> None:
        print(f"[file] {message}")

@dataclass
class SensorReading:
    sensor_id: str
    value: float

class AnomalyDetector:
    def __init__(self, alert: AlertStrategy, threshold: float) -> None:
        self._alert = alert
        self._threshold = threshold

    def check(self, reading: SensorReading) -> None:
        if reading.value > self._threshold:
            self._alert.send(f"Anomalía en {reading.sensor_id}")

# Incorrecta: agregar una nueva forma de alerta obliga a tocar este código.
class BadAnomalyDetector:
    def __init__(self, alert_type: str, threshold: float) -> None:
        self._alert_type = alert_type
        self._threshold = threshold

    def check(self, reading: SensorReading) -> None:
        if reading.value > self._threshold:
            if self._alert_type == "console":
                print(f"[console] Anomalía en {reading.sensor_id}")
            elif self._alert_type == "file":
                print(f"[file] Anomalía en {reading.sensor_id}")
            else:
                raise ValueError("Tipo de alerta no soportado")

# L - Principio de Sustitución de Liskov
# Correcta: los sensores derivados pueden reemplazar al base.
class BaseSensor(ABC):
    @abstractmethod
    def read_value(self) -> float:
        ...

class TemperatureSensor(BaseSensor):
    def read_value(self) -> float:
        return 21.5

class HumiditySensor(BaseSensor):
    def read_value(self) -> float:
        return 60.0

def process_sensor(sensor: BaseSensor) -> float:
    return sensor.read_value()

# Incorrecta: una subclase rompe el contrato esperado.
class BrokenSensor(BaseSensor):
    def read_value(self) -> float:
        raise RuntimeError("No se puede leer el sensor")