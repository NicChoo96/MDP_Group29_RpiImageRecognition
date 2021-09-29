from picamera import PiCamera
from picamera.array import PiRGBArray

def init():
    global camera

    camera = PiCamera(resolution = '640x480')
            # 3D RGB numpy array (row, col, colour)

def close():
    global camera

    camera.close()


        