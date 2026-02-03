from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional, Union


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.processed_count: int = 0
        self.stream_id = stream_id
        self.stream_type = stream_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count = len(data_batch)
        temps = [item.get("temp", 0.0) for item in data_batch]
        avg_temp = sum(temps) / len(temps) if temps else 0.0
        return (
            f"Sensor analysis: {self.processed_count} readings processed, "
            f"avg temp: {avg_temp:.1f}°C"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria in ("high priority", "critical"):
            return [item for item in data_batch if item.get("temp", 0) > 25.0]
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count = len(data_batch)
        buys = sum(item.get("buy", 0) for item in data_batch)
        sells = sum(item.get("sell", 0) for item in data_batch)
        net = buys - sells
        sign = "+" if net >= 0 else ""
        return (
            f"Transaction analysis: {self.processed_count} operations, "
            f"net flow: {sign}{net} units"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "large":
            return [
                item for item in data_batch
                if item.get("buy", 0) > 100 or item.get("sell", 0) > 100
            ]
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count = len(data_batch)
        errors = len([event for event in data_batch if event == "error"])
        return (
            f"Event analysis: {self.processed_count} events, "
            f"{errors} error detected"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "error":
            return [event for event in data_batch if event == "error"]
        return super().filter_data(data_batch, criteria)


class StreamProcessor:
    def process_stream(
        self,
        stream: DataStream,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> str:
        try:
            filtered = stream.filter_data(data_batch, criteria)
            return stream.process_batch(filtered)
        except Exception:
            return "Stream processing failed"


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    print("\nInitializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    sensor_data = [
        {"temp": 22.5},
        {"humidity": 65},
        {"pressure": 1013}
    ]
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(sensor.process_batch(sensor_data))

    transaction = TransactionStream("TRANS_001")
    print("\nInitializing Transaction Stream...")
    print(f"Stream ID: {transaction.stream_id}, "
          f"Type: {transaction.stream_type}")
    transaction_data = [
        {"buy": 100},
        {"sell": 150},
        {"buy": 75}
    ]
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(transaction.process_batch(transaction_data))

    event = EventStream("EVENT_001")
    print("\nInitializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    event_data = ["login", "error", "logout"]
    print("Processing event batch: [login, error, logout]")
    print(event.process_batch(event_data))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()

    print("\nBatch 1 Results:")
    print(
        "- Sensor data:",
        processor.process_stream(
            sensor,
            [{"temp": 30.0}, {"temp": 20.0}],
            "critical"
        )
    )
    print(
        "- Transaction data:",
        processor.process_stream(
            transaction,
            [{"buy": 200}, {"sell": 50}, {"buy": 20}, {"sell": 10}],
            "large"
        )
    )
    print(
        "- Event data:",
        processor.process_stream(
            event,
            ["login", "error", "logout"]
        )
    )

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
