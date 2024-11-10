from time import sleep
import logging
#
from modules.interfaces.buzzer_interface import BuzzerInterface

logger = logging.getLogger(__name__)

try:
  import RPi.GPIO as GPIO
except ImportError:
  logger.warning("RPi.GPIO module not found. Buzzer functionality will be disabled.")
  GPIO = None


class Buzzer(BuzzerInterface):
  def __init__(self, pin: int, silent=False, muted=False):
    self.pin = pin
    self.silent = silent
    self.muted = muted
    self.duty_cycle = 70 # default duty cycle for semi-loud volume (0-100)

    if silent:
      self.duty_cycle = 10 # reduce duty cycle to make buzzer quieter
      logger.info("Buzzer set to silent mode")
    
    if muted:
      self.duty_cycle = 0
      logger.info("Buzzer set to muted mode")

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.pin, GPIO.OUT)
    self.pwm = GPIO.PWM(self.pin, 1) # frequency is set later

  def init(self):
    for frequency in [440, 523, 600, 990]:
      self.play_tone(frequency, 0.1)
      sleep(0.0005)
  
  def play_tone(self, frequency, duration):
    self.pwm.ChangeFrequency(frequency)
    self.pwm.start(self.duty_cycle)
    sleep(duration)
    self.pwm.stop()
  
  def beep(self):
    """ Play a short beep sound """
    beep_freq = 1000
    if self.silent: beep_freq = 25
    if self.muted: beep_freq = 20
    self.play_tone(beep_freq, 0.1)

  def destroy(self):
    for frequency in [990, 600, 523, 440]:
      self.play_tone(frequency, 0.1)
      sleep(0.0005)
    logger.info("Cleaning up GPIO for buzzer")
    GPIO.cleanup(self.pin)
