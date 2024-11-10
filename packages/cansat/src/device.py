#
import pytz
import logging
from datetime import datetime
#
from modules.interfaces.lora_interface import LoraInterface
from modules.mocks.mock_lora import MockLora
from modules.mocks.mock_buzzer import MockBuzzer
from modules.lora import LoRa
from modules.buzzer import Buzzer

class OctaSat:
    def __init__(self, dummy=False, lora=None, bme280=None, buzzer=None, timezone='America/Santiago'):
        self.dummy = dummy
        self.lora = lora or (MockLora() if dummy else LoRa())
        self.buzzer = buzzer or (MockBuzzer() if dummy else Buzzer())
        # self.bme280 = bme280
        self.data = {}
        self.timezone = pytz.timezone(timezone)
        self.logger = logging.getLogger(__name__)

    def init(self):
        """ Initialize the OctaSat device components """
        if self.buzzer:
            self.buzzer.init()
        else:
            self.logger.warning('Buzzer not initialized.')

        if not self.dummy:
            self.lora = LoRa()
            self.buzzer = Buzzer(self.BUZZER_PIN)
            # self.bme280 = BME280()
            self.buzzer.init()

    def make_read(self):
        """ Collect data from sensors """
        if self.dummy:
            return self.dummy_read()

        # temperature, humidity, pressure, altitude = self.bme280.get_packed_data()
        self.data = {
            'timestamp': datetime.now(self.timezone),
            # 'altitude': altitude,
            # 'temperature': temperature,
            # 'humidity': humidity,
            # 'pressure': pressure,
            'latitude': -1,
            'longitude': -1,
            'accel_x': 0,
            'accel_y': 0,
            'accel_z': 0,
            'gyro_x': 0,
            'gyro_y': 0,
            'gyro_z': 0,
            'mag_x': 0,
            'mag_y': 0,
            'mag_z': 0
        }

    def send_payload(self):
        """ Send the payload to the LoRa module """
        if self.lora:
            payload = self._prepare_payload()
            self.lora.begin_packet_radio(payload)
        else:
            self.logger.warning('LoRa module not initialized.')

    def kill(self):
        """ Clean up resources """
        if self.buzzer:
            self.buzzer.destroy()
        else:
            self.logger.warning('Buzzer module not initialized.')
    
    def dummy_read(self):
        """ Generate dummy data for testing """
        return {
            'timestamp': datetime.now(self.timezone),
            'temperature': 25.0,
            'humidity': 50.0,
            'pressure': 1013.25,
            'altitude': 100.0,
            # ...
        }

    def _prepare_payload(self):
        """ Prepare the payload for transmission """
        return f"Latitude: {self.data['latitude']}\nLongitude: {self.data['longitude']}\nTemperature: {self.data['temperature']}\nHumidity: {self.data['humidity']}\nPressure: {self.data['pressure']}"
