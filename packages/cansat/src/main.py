#
import argparse
import logging
from time import sleep
#
from device import OctaSat
from modules.buzzer import Buzzer
from modules.lora import LoRa
# from octasat.modules.bme280 import BME280
from modules.mocks.mock_buzzer import MockBuzzer
from modules.mocks.mock_lora import MockLoRa

def main():
    parser = argparse.ArgumentParser(description='OctaSat Main Program')
    parser.add_argument('--dummy', action='store_true', help='Run in dummy mode (no hardware)')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Initialize modules
    if args.dummy:
        buzzer = MockBuzzer()
        lora = MockLoRa()
    else:
        buzzer = Buzzer(pin=12)
        lora = LoRa()

    # Initialize OctaSat device
    device = OctaSat(dummy=args.dummy, buzzer=buzzer, lora=lora)
    device.init()

    try:
        while True:
            device.make_read()
            device.save_data()
            device.send_payload()
            sleep(1)
    except KeyboardInterrupt:
        logger.info('Process interrupted')
        device.kill()

if __name__ == '__main__':
    main()
