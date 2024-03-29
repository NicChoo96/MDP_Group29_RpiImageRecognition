import time
import grpc

from src.comms import imagecomm_pb2
from src.comms import imagecomm_pb2_grpc
from src.comms import camera_setup
from src.comms import string_data

from picamera import PiCamera
from picamera.array import PiRGBArray

class Image_Client:

    def __init__(self):
        self.img_ip = '192.168.29.202'
        self.img_port = '50051'
        # open a gRPC channel
        self.channel = grpc.insecure_channel('{}:{}'.format(self.img_ip, self.img_port))
        # create a stub (client)
        self.stub = imagecomm_pb2_grpc.ImageCommStub(self.channel)

    
    def take_picture(self):
        try:
            # camera = PiCamera(resolution = '640x480')
            # 3D RGB numpy array (row, col, colour)
            
            # camera warm up time
            # time.sleep(2)
            # OpenCV takes bgr, resize = '640x480'

            camera = camera_setup.camera
            picArray = PiRGBArray(camera)
            camera.capture(picArray, format='bgr', resize=(640,480))
            image = picArray.array
            # camera.close()
            
            print('[Image taken successfully]')

        except Exception as error:
            print('Error while taking picture: ' + str(error))
        
        # converts the image into a 1D array   
        array = image.reshape(-1)
        #print(array)
        return array

    def process_pic(self):
        try:
            #channel = grpc.insecure_channel('192.168.1.218:12345')
            #stub = imagecomm_pb2_grpc.ImageCommStub(channel)
            
            # take picture and convert it to 1D
            picture = self.take_picture()
        
            # update image on server
            request = imagecomm_pb2.PicArray()
            request.image.extend(picture)

            # count = 1 means last image
            request.count = string_data.obs_count
            string_data.obs_count -= 1
            print(f"[Remaining obstacle count]: {string_data.obs_count}")
            # result of the image recognition model
            print("[Sending image to the server]")
            response = self.stub.ProcessImage(request)
            
            return response.result
            
        except Exception as error:
            print("Error when processing picture: " + str(error))

    def stop_server(self):
        self.stub.StopServer()
        print("Stopping the image server")
        

if __name__ == "__main__":
    process_pic()

