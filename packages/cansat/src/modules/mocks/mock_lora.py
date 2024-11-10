#
from modules.interfaces.lora_interface import LoraInterface

class MockLoRa(LoraInterface):
    def begin_packet_radio(self, payload):
        print(f'[mock-lora] Mock sending payload: {payload}')

    def receive_packet_radio(self):
        return '[mock-lora] Mock received packet'
