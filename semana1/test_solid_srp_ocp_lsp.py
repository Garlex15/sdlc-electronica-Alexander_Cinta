from semana1.solid_srp_ocp_lsp import (
    AnomalyDetector,
    ConsoleAlert,
    DataLogger,
    FileAlert,
    HumiditySensor,
    SensorReader,
    SensorReading,
    SensorService,
    TemperatureSensor,
    process_sensor,
)


def test_sensor_reader_read_returns_default_value() -> None:
    reader = SensorReader()

    assert reader.read("sensor-1") == 25.4


def test_data_logger_save_prints_message(capsys) -> None:
    logger = DataLogger()

    logger.save("sensor-2", 12.3)
    captured = capsys.readouterr()

    assert "Guardando sensor-2: 12.3" in captured.out


def test_sensor_service_process_reads_and_logs() -> None:
    class RecordingReader(SensorReader):
        def __init__(self) -> None:
            self.last_id = ""

        def read(self, sensor_id: str) -> float:
            self.last_id = sensor_id
            return 7.8

    class RecordingLogger(DataLogger):
        def __init__(self) -> None:
            self.saved = []

        def save(self, sensor_id: str, value: float) -> None:
            self.saved.append((sensor_id, value))

    reader = RecordingReader()
    logger = RecordingLogger()
    service = SensorService(reader, logger)

    service.process("sensor-3")

    assert reader.last_id == "sensor-3"
    assert logger.saved == [("sensor-3", 7.8)]


def test_anomaly_detector_check_sends_console_alert(capsys) -> None:
    detector = AnomalyDetector(ConsoleAlert(), 10.0)

    detector.check(SensorReading("temp-1", 11.0))
    captured = capsys.readouterr()

    assert "[console] Anomalía en temp-1" in captured.out


def test_anomaly_detector_check_sends_file_alert(capsys) -> None:
    detector = AnomalyDetector(FileAlert(), 20.0)

    detector.check(SensorReading("temp-2", 21.0))
    captured = capsys.readouterr()

    assert "[file] Anomalía en temp-2" in captured.out


def test_process_sensor_supports_temperature_and_humidity() -> None:
    assert process_sensor(TemperatureSensor()) == 21.5
    assert process_sensor(HumiditySensor()) == 60.0
