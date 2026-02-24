# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_stream.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 15:10:47 by rschimme        #+#    #+#               #
#  Updated: 2026/02/24 17:37:48 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed: int = 0
        print(f"Stream ID: {stream_id}", end='')

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return (data_batch)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.stream_type: str = "Environmental Data"
        self.readings_count: int = 0
        self.total_temp: float = 0.0
        self.total_humidity: float = 0
        self.total_pressure: float = 0
        print(f", Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        temp_occur: int = 0
        humidity_occur: int = 0
        pressure_occur: int = 0
        self.readings_count: int = 0
        self.total_temp: float = 0.0
        self.total_humidity: float = 0
        self.total_pressure: float = 0
        for data in data_batch:
            try:
                stuff, number = data.split(':')
                if stuff == "temp":
                    self.total_temp += float(number)
                    temp_occur += 1
                elif stuff == "humidity":
                    self.total_humidity += float(number)
                    humidity_occur += 1
                elif stuff == "pressure":
                    self.total_pressure += float(number)
                    pressure_occur += 1
                else:
                    return "Error: wrong data as input"
            except Exception as e:
                return (f"Error: {e}")
        if self.total_temp != 0:
            self.total_temp = self.total_temp/temp_occur
        if self.total_humidity != 0:
            self.total_humidity = self.total_humidity/humidity_occur
        if self.total_pressure != 0:
            self.total_pressure = self.total_pressure/pressure_occur
        total_operations: int = temp_occur + humidity_occur + pressure_occur
        return_str = f"Sensor analysis: {total_operations} readings processed"
        if self.total_temp != 0:
            return_str += f", avg temp: {self.total_temp}°C"
        if self.total_humidity != 0:
            return_str += f", avg humidity: {self.total_humidity}%"
        if self.total_pressure != 0:
            return_str += f", avg pressure: {self.total_pressure:.1f} hPa"
        return return_str

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        filtered_data: list[Any] = []
        if criteria == "temperature":
            for data in data_batch:
                try:
                    stuff, number = data.split(':')
                    if stuff == "temp":
                        if (float(number) <= 40) & (float(number) >= 0):
                            filtered_data.append(data)
                except Exception as e:
                    print(e)
                    return data_batch
            return (filtered_data)
        elif criteria == "humidity":
            for data in data_batch:
                try:
                    stuff, number = data.split(':')
                    if stuff == "humidity":
                        if (float(number) >= 0) & (float(number) <= 100):
                            filtered_data.append(data)
                except Exception as e:
                    print(e)
                    return data_batch
            return (filtered_data)
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "avg temp": self.total_temp,
            "avg humidity": self.total_humidity,
            "avg pressure": self.total_pressure,
            }


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.stream_type: str = "Financial Data"
        self.net_flow: float = 0
        print(f", Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        self.net_flow: float = 0
        for data in data_batch:
            try:
                stuff, number = data.split(':')
                if stuff == "buy":
                    self.net_flow += float(number)
                elif stuff == "sell":
                    self.net_flow -= float(number)
                else:
                    return "Error: wrong data as input"
            except Exception as e:
                return (f"Error: {e}")
        return f"Transaction analysis: {len(data_batch)} operations, \
net flow: +{self.net_flow} units"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        filtered_data: list[Any] = []
        if criteria == "high":
            for data in data_batch:
                try:
                    stuff, number = data.split(':')
                    if (float(number) >= 150):
                        filtered_data.append(data)
                except Exception as e:
                    print(e)
                    return data_batch
            return (filtered_data)
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "net_flow": self.net_flow
            }


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.stream_type = "System Events"
        self.error: int = 0
        self.login: int = 0
        self.logout: int = 0
        print(f", Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        self.error: int = 0
        self.login: int = 0
        self.logout: int = 0
        for data in data_batch:
            if data == "login":
                self.login += 1
            elif data == "error":
                self.error += 1
            elif data == "logout":
                self.logout += 1
            else:
                return "Error: wrong data as input"
        total_operations = self.login + self.logout + self.error
        return_str = f"Event analysis: {total_operations} readings processed"
        if self.error != 0:
            return_str += f", {self.error} error detected"
        if self.login != 0:
            return_str += f", {self.login} login detected"
        if self.logout != 0:
            return_str += f", {self.logout} logout detected"
        return return_str

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        filtered_data = []
        if criteria == "error":
            for data in data_batch:
                if data == "error":
                    filtered_data.append(data)
            return (filtered_data)
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "errors": self.error
            }


streams: dict[str, Any] = {
    "SENSOR_001": ["temp:22", "temp:800", "humidity:65", "pressure:1013"],
    "TRANS_001": ["buy:100", "sell:150", "buy:75"],
    "EVENT_001": ["login", "error", "logout"],
    "SENSOR_002": ["temp:15", "temp:64", "humidity:61", "humidity:63"],
    }


class StreamProcessor:
    """pilote les differents data stream en fonction de la data en input ?
    """
    @staticmethod
    def process_all(streams: dict) -> None:
        for stream, data in streams.items():
            if isinstance(stream, DataStream):
                print(stream.process_batch(data))

    def filter_all(streams: dict, keyword: str) -> None:
        for stream, data in streams.items():
            if isinstance(stream, DataStream):
                print(stream.filter_data(data, keyword))


def data_stream() -> None:
    processor: StreamProcessor = StreamProcessor
    stream_dict: dict[Any, list[Any]] = {}
    for name, data in streams.items():
        stream_id, number = name.split('_', 1)
        if stream_id == "SENSOR":
            new_stream: SensorStream = SensorStream(name)
            print(f"Processing sensor batch: {data}")
            print(new_stream.process_batch(data))
        elif stream_id == "TRANS":
            new_stream: TransactionStream = TransactionStream(name)
            print(f"Processing Transaction batch: {data}")
            print(new_stream.process_batch(data))
        elif stream_id == "EVENT":
            new_stream: EventStream = EventStream(name)
            print(f"Processing event batch: {data}")
            print(new_stream.process_batch(data))
        else:
            print("unrecognized stream_id")
            return
        print()
        if new_stream:
            stream_dict[new_stream] = data
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    processor.process_all(stream_dict)
    print("\nStream filtering active: error data only in Event streams")
    processor.filter_all(stream_dict, "error")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    data_stream()
