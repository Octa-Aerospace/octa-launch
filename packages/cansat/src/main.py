import os
import pytz
from time import sleep
from datetime import datetime
from dotenv import load_dotenv
#
# from modules.Camera import Camera
# from modules.GY91 import GY91
# from modules.GPS import GPS

load_dotenv()

global dummy; dummy = True # TODO: it would be cool to receive this as a parsed argv

class OctaSat:
    def __init__(self, dummy=False):
        self.dummy = dummy
        self.BUZZER_PIN = 12
        self.I2C_ADDRESS = 0x68
        # self.GPS_PORT = '/dev/ttyAMA0'
        self.BUTTON_GPIO = 5
        self.data = {}
        self.timezone = pytz.timezone("America/Santiago")

        if not self.dummy:
            self.setup_button()

        self.db.connect()

    def setup_button(self):
        GPIO.setup(self.BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def init(self):
        # self.gy91 = GY91(self.I2C_ADDRESS)
        # self.gps = GPS(port=self.GPS_PORT)
        # self.camera = Camera()
        # self.e32 = E32()

        if not self.dummy:
            self.lora = LoRa()
            self.bme280 = BME280()
            self.buzzer = Buzzer(self.BUZZER_PIN)
            self.buzzer.init()

    def make_read(self):
        if self.dummy:
            return self.dummy_read()

        temperature, humidity, pressure, altitude = self.bme280.get_packed_data()
        self.data = {
            'timestamp': datetime.now(self.timezone),
            'latitude': -1,
            'longitude': -1,
            'altitude': altitude,
            'temperature': temperature,
            'humidity': humidity,
            'pressure': pressure,
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
    
    def dummy_read(self):
        dummy_data = self.db.get_dummy_telemetry()
        self.data = dummy_data

    def save_data(self):
        self.db.insert_telemetry_data(self.data)

    def send_payload(self):
        if self.dummy:
            return print(f'[ ! ] Dummy data >>\n{self.data}', end="\n\n")
        
        latitude, longitude = -1, -1
        temperature, humidity, pressure, altitude = self.bme280.get_packed_data()
        payload = f'Latitude: {latitude}\nLongitude: {longitude}\nTemperature: {temperature}\nHumidity: {humidity}\nPressure: {pressure}\nAltitude: {altitude}'
        self.lora.begin_packet_radio(payload)

    def kill(self):
        if not self.dummy:
            self.buzzer.destroy()
        else:
            print("[!] Buzzer -- cleaning up GPIO")

if __name__ == "__main__":
    if not dummy:
        import RPi.GPIO as GPIO
        #
        from modules.Buzzer import Buzzer
        from modules.BME280 import BME280
        from packages.cansat.src.modules.lora import LoRa

    device = OctaSat(dummy)
    device.init()

    try:
        while True:
            device.make_read()
            device.save_data()
            device.send_payload()
            sleep(1)

    except KeyboardInterrupt:
        print(f'\n[!] Process interrupted')
        device.kill()
