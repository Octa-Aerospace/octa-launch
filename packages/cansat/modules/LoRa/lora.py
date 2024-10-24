import adafruit_rfm9x
import digitalio
import board
import busio
import time as t

class LoRa:
  def __init__(self):
    self.BAUDRATE = 1000000 # min 1Mhz; max 10MHz
    self.RADIO_FREQ_MHZ = 915.0 # 915 Mhz
    self.CS = digitalio.DigitalInOut(board.CE1)
    self.RESET = digitalio.DigitalInOut(board.D25)
    self.spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    self.rfm9x = adafruit_rfm9x.RFM9x(self.spi, self.CS, self.RESET, self.RADIO_FREQ_MHZ, baudrate=self.BAUDRATE)

  def begin_packet_radio(self, payload):
    if len(payload) > 252:
      return "[ ! ] You can only send a message up to 252 bytes in length at a time!"

    self.rfm9x.tx_power = 23 # min 5dB; max 23dB

    try:
      response = self.rfm9x.send(bytes(payload, "utf-8"))
      print(f'[ ! ] response {response}')
      if response:
        print(f'[ ! ] Packet sent >>\n{payload}')
    except Exception as e:
      print(f'[ ! ] {e}')
      print(f'[ ! ] Packet not sent! >> {payload}')


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

if __name__ == "__main__":
  lora = LoRa()
  lora.begin_packet_radio()
  lora.receive_packet_radio()
