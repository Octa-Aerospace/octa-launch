import random
from datetime import datetime

def get_random_telemetry():
  telemetry = {
    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'latitude': round(random.uniform(-90, 90), 6),
    'longitude': round(random.uniform(-180.0, 180.0), 6),
    'altitude': round(random.uniform(0, 1000), 2),
    'temperature': round(random.uniform(-15, 40), 2),
    'humidity': round(random.uniform(0, 100), 2),
    'pressure': round(random.uniform(900, 1100), 2),
    'accel_x': round(random.uniform(-10, 10), 2),
    'accel_y': round(random.uniform(-10, 10), 2),
    'accel_z': round(random.uniform(-10, 10), 2),
    'gyro_x': round(random.uniform(-10, 10), 2),
    'gyro_y': round(random.uniform(-10, 10), 2),
    'gyro_z': round(random.uniform(-10, 10), 2),
    'mag_x': round(random.uniform(-10, 10), 2),
    'mag_y': round(random.uniform(-10, 10), 2),
    'mag_z': round(random.uniform(-10, 10), 2)
  }
  return telemetry
