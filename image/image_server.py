import grpc
import threading
import numpy as np
import cv2


import imagecomm_pb2
import imagecomm_pb2_grpc

import time
from concurrent import futures


class Listener(imagecomm_pb2_grpc.ImageCommServicer):

    def ProcessImage(self, request, context):
        # get the 1D array of the image
        imageArr = request.image
        Image_Server().store_image(imageArr)
        #Image_Server().display_image()
        # pass into model and get result
        result = 1
        return imagecomm_pb2.ProcessResult(result=result)


class Image_Server:

    def __init__(self):
        # self.algo_server = Listener()
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        imagecomm_pb2_grpc.add_ImageCommServicer_to_server(Listener(), self.server)
        self.server.add_insecure_port('0.0.0.0:12345')

    def connect(self):
        print('Starting Image Server on port: 12345')
        self.server.start()
        try:
            while True:
                print("Number of threads: " + str(threading.active_count()))
                time.sleep(86400)

        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            self.disconnect()

    def disconnect(self):
        print("Disconnecting Algo server")
        self.server.stop(0)
        
    def store_image(self,imageArr):
        imageNp = np.array(imageArr).reshape(480,640,3)
        # reshape and form as an image?
        print(imageNp.shape)
        print(type(imageNp))
        
        cv2.imwrite('image.png',imageNp)
        print("Image is stored")
    
    def display_image(self):
        im = cv2.imread('image.png')
        cv2.imshow('Test', im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    Image_Server().connect()
