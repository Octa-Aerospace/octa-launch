from serial import Serial
import pynmea2

class GPS:
  def __init__(self, port, baudrate=9600, timeout=0.5):
    self.ser = Serial(port=port, baudrate=baudrate, timeout=timeout)

  def read_data(self):
    pynmea2.NMEAStreamReader()
    incoming_data = self.ser.readline().decode('unicode_escape')
    
    if (incoming_data[0:6] == "$GPRMC"):
      newmsg = pynmea2.parse(incoming_data)
      lat = str(newmsg.latitude)
      lng = str(newmsg.longitude)
      return lat, lng
    else:
      return (None, None)
