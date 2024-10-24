import os
import sys
import time
import smbus
# from imusensor.MPU9250 import MPU9250

class GY91:
  def __init__(self, address) -> None:
    self.test = None
  #   self.address = address
  #   self.bus = smbus.SMBus(1)
  #   self.imu = MPU9250.MPU9250(self.bus, self.address)
  #   self.imu.begin()
  #   self.imu.readSensor()
  #   self.imu.computeOrientation()

  # def get_accel(self, raw=False):
  #   self.imu.readSensor()
  #   self.imu.computeOrientation()
  #   values = self.imu.AccelVals
  #   if (raw): return values
  #   return { 'x': values[0], 'y': values[1], 'z': values[2] }

  # def get_gyro(self):
  #   self.imu.readSensor()
  #   self.imu.computeOrientation()
  #   values = self.imu.GyroVals
  #   return { 'x': values[0], 'y': values[1], 'z': values[2] }

  # def get_mag(self):
  #   self.imu.readSensor()
  #   self.imu.computeOrientation()
  #   values = self.imu.MagVals
  #   return { 'x': values[0], 'y': values[1], 'z': values[2] }

if __name__ == "__main__":
  I2C_ADDRESS = 0x68
  sensor = GY91(I2C_ADDRESS)
  # sensor.get_accel(raw=True)
