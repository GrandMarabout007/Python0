# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_streams.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 15:10:47 by rschimme        #+#    #+#               #
#  Updated: 2026/02/19 19:39:14 by rschimme        ###   ########.fr        #
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
        return(data_batch)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        created_dict = [str, Union[str, int, float]]
        # str = self.stream_id
        # int = self.processed
        return(created_dict)

class SensorStream(DataStream):
    def __init__(self, stream_id):
        super().__init__


class TransactionStream(DataStream):
    def __init__(self, stream_id):


class EventStream(DataStream):
    def __init__(self, stream_id):


class StreamProcessor:
    """pilote les differents data stream en fonction de la data en input ?
    """


streams: dict[str, Any] = {
    "SENSOR_001":[22.5,65,1013],
    "TRANS_001":[100,150,75],
    "EVENT_001":["login", "error", "logout"],
    }

def data_stream():
    sensorstream = SensorStream
    transactionsstream = TransactionStream
    eventstream = EventStream

if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")