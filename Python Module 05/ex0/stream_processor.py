from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if (isinstance(data, list) and all(isinstance(i, int) for i in data)):
            return True
        return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")
        try:
            num = len(data)
            sums = sum(data)
            av = sums / num if num > 0 else 0.0
            return f"Processed {num} numeric values, sum={sums}, avg={av}"
        except Exception as exc:
            raise ValueError("Error processing numeric data") from exc


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")
        try:
            char_count = len(data)
            word_count = len(data.split())
            return (f"Processed text: {char_count} characters, "
                    f"{word_count} words")
        except Exception as exc:
            raise ValueError("Error processing text data") from exc


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log data")
        try:
            if data[0] == "E":
                level = "ERROR"
            elif data[0] == "W":
                level = "WARNING"
            else:
                level = "INFO"
            message = data.split(":", 1)
            return self.format_output(f"{level} level detected:{message[1]}")
        except Exception as exc:
            raise ValueError("Error processing log data") from exc

    def format_output(self, result: str) -> str:
        if result[0] == "E":
            prefix = "[ALERT] "
        elif result[0] == "W":
            prefix = "[WARNING] "
        else:
            prefix = "[INFO] "
        formatted_output = super().format_output(result)
        return f"{prefix}{formatted_output}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    # Numeric Processor
    numeric_processor = NumericProcessor()
    numeric_data = [1, 2, 3, 4, 5]
    print("Initializing Numeric Processor...")
    print("Processing data:", numeric_data)
    if numeric_processor.validate(numeric_data):
        print("Validation:", "Numeric data verified")
    else:
        print("Invalid numeric data")
    print("Output:", numeric_processor.process(numeric_data))

    # Text Processor
    text_processor = TextProcessor()
    text_data = "Hello Nexus World"
    print("\nInitializing Text Processor...")
    print(f'Processing data: "{text_data}"')
    if text_processor.validate(text_data):
        print("Validation:", "Text data verified")
    else:
        print("Invalid text data")
    print("Output:", text_processor.process(text_data))

    # Log Processor
    log_processor = LogProcessor()
    log_data = "ERROR: Connection timeout"
    print("\nInitializing Log Processor...")
    print(f'Processing data: "{log_data}"')
    if log_processor.validate(log_data):
        print("Validation:", "Log entry verified")
    else:
        print("Invalid log data")
    print("Output:", log_processor.process(log_data))

    # Polymorphic demo
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    # Numeric
    result1 = numeric_processor.process([1, 2, 3])
    print("Result 1:", result1)

    # Text
    result2 = text_processor.process("Hello Nexus!")
    print("Result 2:", result2)

    # Log
    result3 = log_processor.process("INFO: System ready")
    print("Result 3:", result3)

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
