# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  stream_processor.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 13:35:08 by rschimme        #+#    #+#               #
#  Updated: 2026/02/18 15:58:53 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if self.validate(data) is True:
            num_sum: int = sum(data)
            nbr_data: int = len(data)
            avg: float = num_sum/nbr_data
            return (f"Processed {nbr_data} values, sum={num_sum}, avg={avg}")
        else:
            return ("[ALERT], ERROR level detected: not numeric \
data as dict[int]")

    def validate(self, data: Any) -> bool:
        try:
            for number in data:
                int(number)
        except (ValueError, TypeError):
            print("Validation: Validation failed")
            return False
        print("Validation: Numeric data verified")
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def process(self, data) -> str:
        if self.validate(data) is True:
            text_len = len(data)
            text_word = len(data.split())
            return (f"Processed text: {text_len} characters, \
{text_word} words")
        else:
            return ("[ALERT], ERROR level detected: not Text data as str")

    def validate(self, data: Any) -> bool:
        try:
            data + ""
        except TypeError:
            print("Validation: Validation failed")
            return False
        print("Validation: Text data verified")
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data) -> str:
        if self.validate(data) is True:
            content = data.split(" ", 1)
            if content[0] == "ERROR:":
                return (f"[ALERT] ERROR level detected: {content[1]}")
            elif content[0] == "INFO:":
                return (f"[INFO] INFO level detected: {content[1]}")
        else:
            return ("[ALERT], ERROR level detected: not Log data as \
<keyword: text> ")

    def validate(self, data: Any) -> bool:
        try:
            data + ""
            if data.split()[0] == "ERROR:":
                print("Validation: Log data verified")
                return True
            elif data.split()[0] == "INFO:":
                print("Validation: Log data verified")
                return True
        except TypeError:
            print("Validation: Validation failed")
            return False
        print("Validation: Validation failed")
        return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def stream_processor():
    data1 = [1, 5, 6, 8]
    print("Initializing Numeric Processor...")
    nprocessor = NumericProcessor()
    print(f"Processing data: {data1}")
    print(nprocessor.format_output(nprocessor.process(data1)))
    print()
    data2 = "Hello Nexus World"
    print("Initializing Text Processor...")
    tprocessor = TextProcessor()
    print(f"Processing data: {data2}")
    print(tprocessor.format_output(tprocessor.process(data2)))
    print()
    data3 = "ERROR: Connection timeout"
    print("Initializing Log Processor...")
    lprocessor = LogProcessor()
    print(f"Processing data: {data3}")
    print(lprocessor.format_output(lprocessor.process(data3)))
    print("\n=== Polymorphic Processing Demo ===")
    data_to_process = [
        (lprocessor, "INFO: System ready"),
        (tprocessor, "Hello guys"),
        (nprocessor, [1, 5, 8, 9]),
    ]
    i = 1
    for processor, data in data_to_process:
        print(f"Result {i}: {processor.process(data)}\n")
        i += 1


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    stream_processor()
