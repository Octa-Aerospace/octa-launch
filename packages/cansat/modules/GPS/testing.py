import serial
import pynmea2

while True:
    port = "/dev/ttyAMA0"
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata = ser.readline().decode('unicode_escape')

    if newdata[0:6] == "$GPRMC":
        newmsg = pynmea2.parse(newdata)
        lat = newmsg.latitude
        lng = newmsg.longitude
        gps = f'Latitude = {str(lat)} and Longitude = {str(lng)}'
        print(gps)

        # Guardar en archivo .csv
        with open("gps_data.csv", "a") as file:
            file.write(str(lat) + "," + str(lng) + "\n")
            
