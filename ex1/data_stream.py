from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = 0
        self._total_processed: int = 0

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

    def remaining(self) -> int:
        return len(self._data)

    def total_processed(self) -> int:
        return self._total_processed

    def _add_processed(self, count: int) -> None:
        self._total_processed += count

    def display_name(self) -> str:
        name = type(self).__name__
        if name.endswith("Processor"):
            name = name[:-9] + " Processor"
        return name


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
            self._add_processed(1)
        else:
            for item in data:
                self._data.append(str(item))
            self._add_processed(len(data))


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
            self._add_processed(1)
        else:
            for item in data:
                self._data.append(item)
            self._add_processed(len(data))


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
            self._add_processed(1)
        else:
            for item in data:
                self._data.append(self._format_log(item))
            self._add_processed(len(data))


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = False

            for processor in self._processors:
                if processor.validate(element):
                    processor.ingest(element)
                    processed = True
                    break

            if not processed:
                print(
                    "DataStream error - Can't process element in stream: "
                    + str(element)
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if len(self._processors) == 0:
            print("No processor found, no data")
            return

        for processor in self._processors:
            print(
                processor.display_name()
                + ": total "
                + str(processor.total_processed())
                + " items processed, remaining "
                + str(processor.remaining())
                + " on processor"
            )


def consume(processor: DataProcessor, amount: int) -> None:
    for _ in range(amount):
        processor.output()


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")

    stream = DataStream()
    stream.print_processors_stats()

    batch: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print("Registering Numeric Processor")
    numeric = NumericProcessor()
    stream.register_processor(numeric)

    print("Send first batch of data on stream: " + str(batch))
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Registering other data processors")
    text = TextProcessor()
    log = LogProcessor()

    stream.register_processor(text)
    stream.register_processor(log)

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    consume(numeric, 3)
    consume(text, 2)
    consume(log, 1)

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
