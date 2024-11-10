#
from modules.interfaces.buzzer_interface import BuzzerInterface

class MockBuzzer(BuzzerInterface):
    def init(self):
        print(f'[mock-buzzer] Mock buzzer initialized.')

    def play_tone(self, frequency, duration):
        print(f'[mock-buzzer] Mock playing tone: {frequency}Hz for {duration}s')

    def destroy(self):
        print(f'[mock-buzzer] Mock buzzer destroyed.')
