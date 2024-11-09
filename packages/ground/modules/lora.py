import adafruit_rfm9x
import digitalio
import board
import busio
import time as t

class LoRa:
    def __init__(self):
        self.BAUDRATE = 1000000  # min 1Mhz; max 10MHz
        self.RADIO_FREQ_MHZ = 915.0  # 915 Mhz
        self.CS = digitalio.DigitalInOut(board.CE1)
        self.RESET = digitalio.DigitalInOut(board.D25)
        self.spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
        try:
            self.rfm9x = adafruit_rfm9x.RFM9x(self.spi, self.CS, self.RESET, self.RADIO_FREQ_MHZ, baudrate=self.BAUDRATE)
        except Exception as e:
            print(f'[ ! ] Error initializing RFM9x: {e}')

        self.rfm9x.tx_power = 23  # min 5dB; max 23dB
        self.times_received = 0

    def begin_packet_radio(self, payload):
        payload = str(payload)
        if len(payload) > 252:
            return "[ ! ] You can only send a message up to 252 bytes in length at a time!"

        try:
            response = self.rfm9x.send(bytes(payload, "utf-8"))
            print(f'[ ! ] Send response: {response}')
            if response:
                print(f'[ OK ] Packet sent >> {payload}')
            else:
                print('[ ! ] Failed to send packet!')
        except Exception as e:
            print(f'[ ! ] Error during packet transmission: {e}')

    def receive_packet_radio(self):
        print('[ OK ] Waiting for packets...')
        packet = self.rfm9x.receive(timeout=3.0)

        if packet is not None:
            packet_text = packet
            rssi = self.rfm9x.last_rssi
            self.times_received += 1

            print(f'[ OK ] Packet received! >> {packet_text}')
            print(f'[ OK ] RSSI: {rssi}')
            print(f'[ OK ] Times received: {self.times_received}\n')
            # Upload to database here
        else:
            print('[ ! ] No packet received!\n')

if __name__ == "__main__":
    lora = LoRa()

    while True:
        try:
            user_input = input("Enter 's' to send or 'l' to listen: ")
            if user_input == "s":
                payload = input("Enter your payload: ")
                lora.begin_packet_radio(payload)
                t.sleep(1)
            elif user_input == "l":
                lora.receive_packet_radio()
                t.sleep(1)
        except KeyboardInterrupt:
            print('\n[ OK ] Exiting...')
            break
