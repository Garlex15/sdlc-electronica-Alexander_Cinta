
#Importamos al inicio
from dataclasses import dataclass
from enum import Enum, auto
from typing import Protocol



#Definimo de un Enum (Enumeración)
class SensorType(Enum):
    TEMPERATURE = auto()
    HUMIDITY = auto()


#DEFINICIÓN DE UN DATA CLASSES (CLASES DE DATOS)
@dataclass(frozen=True)
class Reading:
    sensor_id: str
    value: float
    sensor_type: SensorType


#DEFINICIÓN DE UN PROTOCOL 
class Transport(Protocol):
    def send(self, payload: bytes) -> None: ...

#FUNCIÓN PURA FACIL DE TESTEAR
def to_frame(r: Reading) -> bytes:
    return f"{r.sensor_id}:{r.value:.2f}".encode()


def convert_temperature_celsius_to_fahrenheit(r: Reading) -> Reading:
    """Return a new Reading with temperature converted from Celsius to Fahrenheit."""
    if r.sensor_type != SensorType.TEMPERATURE:
        return r

    return Reading(
        sensor_id=r.sensor_id,
        value=r.value * 9.0 / 5.0 + 32.0,
        sensor_type=r.sensor_type,
    )


def format_reading_as_csv(r: Reading) -> str:
    """Return the reading formatted as a single CSV record."""
    return f"{r.sensor_id},{r.sensor_type.name},{r.value:.2f}"


def is_temperature_above_threshold(r: Reading, threshold: float) -> bool:
    """Return True when the reading is a temperature above the given threshold."""
    return r.sensor_type == SensorType.TEMPERATURE and r.value > threshold


def reading_summary(r: Reading) -> str:
    """Return a simple text summary of the reading."""
    return f"Reading(id={r.sensor_id}, type={r.sensor_type.name}, value={r.value:.2f})"


def with_scaled_value(r: Reading, factor: float) -> Reading:
    """Return a new Reading with the value scaled by the given factor."""
    return Reading(sensor_id=r.sensor_id, value=r.value * factor, sensor_type=r.sensor_type)

