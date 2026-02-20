# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_streams.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 15:10:47 by rschimme        #+#    #+#               #
#  Updated: 2026/02/20 18:32:50 by rschimme        ###   ########.fr        #
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
            for data in data_batch:
                stuff, number = data.split(':')
                if stuff == "temp":
                    self.total_temp += number
                elif stuff == "humidity":
                    self.total_humidity += number
                elif stuff == "pressure":
                    self.total_pressure += number
            self.total_temp = self.total_temp/
            try:
                int(temp)
                int(humidity)
                int(pressure)
            except Exception as e:
                return (f"Error : {e}")
            return (f"Processing sensor batch: [temp:{temp}, \
humidity:{humidity}, pressure:{pressure}]")
    
    # def filter_data(self, data_batch, criteria = None) -> List[Any]:
    #     if len(data_batch) != 3:
    #         print("error")
    #     if isinstance(data_batch, int) is False:
    #         print("error")
    def get_stats(self)-> Dict[str, Union[str, int, float]]:
        return {
            "readings": self.stream_id
            "avg temp": 
            }

# class TransactionStream(DataStream):
#     def __init__(self, stream_id):


# class EventStream(DataStream):
#     def __init__(self, stream_id):
#         pass


streams: dict[str, Any] = {
    "SENSOR_001": ["temp:22", "humidity:65", "pressure:1013"],
    "TRANS_001": ["buy:100", "sell:150", "buy:75"],
    "EVENT_001": ["login", "error", "logout"],
    }


# class StreamProcessor:
#     """pilote les differents data stream en fonction de la data en input ?
#     """
    





def data_stream():
    sensorstream = SensorStream
    # transactionsstream = TransactionStream
    # eventstream = EventStream
    for name, data in streams.items():
        stream_id, number = name.split('_', 1)
        if stream_id == "SENSOR":
            print(sensorstream.process_batch(sensorstream, data))
        elif stream_id == "TRANS":
            print("trans")
        elif stream_id == "EVENT":
            print("event")
        else:
            print("unrecognized stream_id")

if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    data_stream()