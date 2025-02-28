import adafruit_rfm9x
import digitalio
import board
import busio
import logging
#
from modules.interfaces.lora_interface import LoraInterface

logger = logging.getLogger(__name__)

class LoRa(LoraInterface):
  def __init__(self, radio_freq_mhz: float, baudrate: int):
    self.CS = digitalio.DigitalInOut(board.CE1)
    self.RESET = digitalio.DigitalInOut(board.D25)
    self.spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    self.rfm9x = adafruit_rfm9x.RFM9x(
      self.spi,
      self.CS,
      self.RESET,
      radio_freq_mhz,
      baudrate=baudrate # not a positional arg, passing as a keyword arg
    )

  def begin_packet_radio(self, payload):
    if len(payload) > 252:
      return "[ ! ] You can only send a message up to 252 bytes in length at a time!"

    self.rfm9x.tx_power = 23 # min 5dB; max 23dB

    try:
      self.rfm9x.send(bytes(payload, "utf-8"))
      logger.info(f"[ ok ] packet sent: \n{payload}\n")
      return True
    except Exception as e:
      logger.exception(f"[ ! ] Error during packet transmission: {e}")
      logger.exception(f"[ ! ] packet not sent: {payload}")
      return False

  def receive_packet_radio(self):
    self.rfm9x.tx_power = 23
    times = 0
    packet = self.rfm9x.receive(timeout=3)

    if packet is not None:
        packet_text = str(packet, 'ascii')
        rssi = self.rfm9x.last_rssi
        times += 1

        print(f'[ OK ] Packet received! >> {packet_text}')
        print(f'[ OK ] RSSI: {rssi}')
        print(f'[ OK ] Times: {times}\n')
        return packet, rssi, packet_text # RAW bytes, signal strength, ASCII

    else:
        return '[ ! ] The conection is interrupted.'
