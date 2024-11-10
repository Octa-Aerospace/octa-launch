#
from abc import ABC, abstractmethod

class LoraInterface(ABC):
    @abstractmethod
    def begin_packet_radio(self, payload):
        pass

    @abstractmethod
    def receive_packet_radio(self):
        pass
