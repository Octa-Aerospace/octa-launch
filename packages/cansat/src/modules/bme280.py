import board
from adafruit_bme280 import basic as sensor

class BME280:
  def __init__(self):
    self.i2c = board.I2C()
    self.bme280 = sensor.Adafruit_BME280_I2C(self.i2c)
    self.bme280.sea_level_pressure = 1013.25
  
  def get_packed_data(self):
    temperature = self.bme280.temperature
    humidity = self.bme280.humidity
    pressure = self.bme280.pressure
    altitude = self.bme280.altitude
    return temperature, humidity, pressure, altitude
