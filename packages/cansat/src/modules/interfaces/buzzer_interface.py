#
from abc import ABC, abstractmethod

class BuzzerInterface(ABC):
    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def play_tone(self, frequency, duration):
        pass

    @abstractmethod
    def destroy(self):
        pass
