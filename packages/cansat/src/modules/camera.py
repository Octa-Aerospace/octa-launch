from picamera import PiCamera
from datetime import datetime
from time import sleep

class Camera:
    def __init__(self):
        self.camera = PiCamera()

    def shot(self):
        try:
            now = datetime.now()
            date_time_string = now.strftime("%Y%m%d_%H%M%S")
            file_name = f"images/OCTA_{date_time_string}.jpg"
            self.camera.resolution = (1280, 720)
            self.camera.capture(file_name)
        finally:
            self.camera.close()

if __name__ == "__main__":
    camera = Camera()
    camera.shot()
