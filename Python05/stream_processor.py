# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  stream_processor.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 13:35:08 by rschimme        #+#    #+#               #
#  Updated: 2026/02/17 17:45:20 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        print("Output: default processed")
        return ("yes")


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        print("Initializing Numeric Processor...")
        print(f"Processing data: {data}")
        if self.validate(data) is True:
            num_sum: int = sum(data)
            nbr_data: int = len(data)
            avg: float = num_sum/nbr_data
            self.format_output(f"Processed {nbr_data} values, sum={num_sum}, avg={avg}")
        else:
            self.format_output("[ALERT], ERROR level detected: not numeric data as dict[int]")
        return "Done"

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
        super().format_output(result)
        return "Done"


class TextProcessor(DataProcessor):
    def process(self, data) -> str:
        print("Initializing Text Processor...")
        print(f"Processing data: {data}")
        if self.validate(data) is True:
            text_len = len(data)
            text_word = len(data.split())
            self.format_output(f"Processed text: {text_len} characters, {text_word} words")
        else:
            self.format_output("[ALERT], ERROR level detected: not Text data as str")
        return "Done"

    def validate(self, data: Any) -> bool:
        try:
            data + ""
        except TypeError:
            print("Validation: Validation failed")
            return False
        print("Validation: Text data verified")
        return True

    def format_output(self, result: str) -> str:
        super().format_output(result)
        return "Done"


class LogProcessor(DataProcessor):
    def process(self, data) -> str:
        print("Initializing Log Processor...")
        print(f"Processing data: {data}")
        if self.validate(data) is True:
            content = data.split(" ", 1)
            if content[0] == "ERROR:":
                self.format_output(f"[ALERT] ERROR level detected: {content[1]}")
            elif content[0] == "INFO:":
                self.format_output(f"[INFO] INFO level detected: {content[1]}")
        else:
            self.format_output("[ALERT], ERROR level detected: not Log data as <keyword: text> ")
        return "Done"

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
        super().format_output(result)
        return "Done"


def stream_processor():
    nprocessor = NumericProcessor()
    nprocessor.process([1, 5, 6, 8])
    print()
    tprocessor = TextProcessor()
    tprocessor.process("Hello Nexus World")
    print()
    lprocessor = LogProcessor()
    lprocessor.process("ERROR: Connection timeout")
    print("\n=== Polymorphic Processing Demo ===")
    data_to_process = [
        (lprocessor, "INFO: System ready"),
        (tprocessor, "Hello guys"),
        (nprocessor, [1, 5, 8, 9]),
    ]
    for processor, data in data_to_process:
        processor.process(data)
        print()


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    stream_processor()
