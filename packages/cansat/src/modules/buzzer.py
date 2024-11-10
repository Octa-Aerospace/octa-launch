from time import sleep
#
from modules.interfaces.buzzer_interface import BuzzerInterface

try:
  import RPi.GPIO as GPIO
except ImportError:
  GPIO = None

class Buzzer(BuzzerInterface):
  def __init__(self, pin: int):
    self.pin = pin
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.pin, GPIO.OUT)
    self.pwm = GPIO.PWM(self.pin, 1)

  def init(self):
    for frequency in [440, 523, 600, 990]:
      self.play_tone(frequency, 0.1)
      sleep(0.0005)
  
  def play_tone(self, frequency, duration):
    self.pwm.start(50) # 50% duty cycle
    self.pwm.ChangeFrequency(frequency)
    sleep(duration)
    self.pwm.stop()

  def destroy(self):
    for frequency in [990, 600, 523, 440]:
      self.play_tone(frequency, 0.1)
      sleep(0.0005)
    print("[!] Buzzer -- cleaning up GPIO")
    GPIO.cleanup(self.pin)
