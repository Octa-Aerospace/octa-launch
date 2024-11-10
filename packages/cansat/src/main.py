#
import os
import argparse
import logging
from time import sleep
from dotenv import load_dotenv
#
from device import OctaSat
from modules.buzzer import Buzzer
from modules.lora import LoRa
# from octasat.modules.bme280 import BME280
from modules.mocks.mock_buzzer import MockBuzzer
from modules.mocks.mock_lora import MockLoRa

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description='OctaSat Main Program')
    parser.add_argument('--dummy', action='store_true', help='Run in dummy mode (no hardware)')
    parser.add_argument('--silent', action='store_true', help='Run with buzzer at lower volume')
    parser.add_argument('--muted', action='store_true', help='Run with buzzer muted')
    parser.add_argument('--notify', action='store_true', help='Play a sound when a packet is successfully sent')

    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Reading config from env variables
    buzzer_pin = int(os.getenv('BUZZER_PIN', 12))
    # i2c_address = int(os.getenv('I2C_ADDRESS', '0x68'), 16)
    radio_freq_mhz = float(os.getenv('RADIO_FREQ_MHZ', 915))
    baudrate = int(os.getenv('BAUDRATE', 1000000))
    timezone = os.getenv('TIMEZONE', 'America/Santiago')

    # Initialize modules
    if args.dummy:
        buzzer = MockBuzzer()
        lora = MockLoRa()
    else:
        buzzer = Buzzer(buzzer_pin, silent=args.silent, muted=args.muted)
        lora = LoRa(radio_freq_mhz, baudrate)

    # Initialize OctaSat device
    device = OctaSat(
        dummy=args.dummy,
        buzzer=buzzer,
        lora=lora,
        timezone=timezone,
        notify=args.notify
    )
    device.init()

    try:
        while True:
            device.make_read()
            device.send_payload()
            sleep(1)
    except KeyboardInterrupt:
        logger.info('Process interrupted')
        device.kill()

if __name__ == '__main__':
    main()
