# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_streams.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 15:10:47 by rschimme        #+#    #+#               #
#  Updated: 2026/02/23 17:51:46 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id: str = stream_id
        self.processed: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return (data_batch)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        created_dict = [str, Union[str, int, float]]
        # str = self.stream_id
        # int = self.processed
        return (created_dict)


class SensorStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"
        self.readings_count = 0
        self.total_temp: float = 0.0
        self.total_humidity = 0
        self.total_pressure = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        temp_occur = 0
        humidity_occur = 0
        pressure_occur = 0
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
        return (f"Processing sensor batch: [temp:{self.total_temp}, \
humidity:{self.total_humidity}, pressure:{self.total_pressure:.1f}]")

    def filter_data(self, data_batch, criteria: Optional[str] = None) -> List[Any]:
        filtered_data = []
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

# class TransactionStream(DataStream):
#     def __init__(self, stream_id):


# class EventStream(DataStream):
#     def __init__(self, stream_id):
#         pass


streams: dict[str, Any] = {
    "SENSOR_001": ["temp:22", "temp:800", "humidity:65", "pressure:1013"],
    "TRANS_001": ["buy:100", "sell:150", "buy:75"],
    "EVENT_001": ["login", "error", "logout"],
    }


# class StreamProcessor:
#     """pilote les differents data stream en fonction de la data en input ?
#     """
#     def process_all(streams: list):
#         for stream in streams:
#             stream.process_batch()






def data_stream():
    # processor = StreamProcessor
    # stream_list = []
    for name, data in streams.items():
        stream_id, number = name.split('_', 1)
        if stream_id == "SENSOR":
            new_stream = SensorStream(name)
            # print(sensorstream.filter_data(data, "temperature"))
            # print(sensorstream.process_batch(data))
            # print(sensorstream.get_stats())
        elif stream_id == "TRANS":
            print("placeholder")
        elif stream_id == "EVENT":
            print("placeholder")
        else:
            print("unrecognized stream_id")
    #     stream_list.append(new_stream)
    # processor.process_all(stream_list)
if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    data_stream()