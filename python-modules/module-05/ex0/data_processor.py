from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self._data) == 0:
            raise Exception("No data available")

        rank = self._rank
        self._rank += 1
        return rank, self._data.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, int | float):
            return True
        if isinstance(data, list):
            return all(isinstance(item, int | float) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if isinstance(data, int | float):
            self._data.append(str(data))
        else:
            for item in data:
                self._data.append(str(item))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        if isinstance(data, str):
            self._data.append(data)
        else:
            for item in data:
                self._data.append(item)


class LogProcessor(DataProcessor):
    def _is_log(self, data: Any) -> bool:
        if not isinstance(data, dict):
            return False
        return all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in data.items()
        )

    def validate(self, data: Any) -> bool:
        if self._is_log(data):
            return True
        if isinstance(data, list):
            return all(self._is_log(item) for item in data)
        return False

    def _format_log(self, data: dict[str, str]) -> str:
        if "log_level" in data and "log_message" in data:
            return data["log_level"] + ": " + data["log_message"]

        items = [key + ": " + value for key, value in data.items()]
        return ", ".join(items)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        if isinstance(data, dict):
            self._data.append(self._format_log(data))
        else:
            for item in data:
                self._data.append(self._format_log(item))


def show_value(prefix: str, processor: DataProcessor) -> None:
    rank, value = processor.output()
    print(prefix + " " + str(rank) + ": " + value)


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Testing Numeric Processor...")
    print("Trying to validate input '42': " + str(numeric.validate(42)))
    print("Trying to validate input 'Hello': "
          + str(numeric.validate("Hello")))

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")  # type: ignore[arg-type]
    except Exception as exc:
        print("Got exception: " + str(exc))

    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])

    print("Extracting 3 values...")
    show_value("Numeric value", numeric)
    show_value("Numeric value", numeric)
    show_value("Numeric value", numeric)

    print("Testing Text Processor...")
    print("Trying to validate input '42': " + str(text.validate(42)))

    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(["Hello", "Nexus", "World"])

    print("Extracting 1 value...")
    show_value("Text value", text)

    print("Testing Log Processor...")
    print("Trying to validate input 'Hello': " + str(log.validate("Hello")))

    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]

    print("Processing data: " + str(logs))
    log.ingest(logs)

    print("Extracting 2 values...")
    show_value("Log entry", log)
    show_value("Log entry", log)


if __name__ == "__main__":
    main()
