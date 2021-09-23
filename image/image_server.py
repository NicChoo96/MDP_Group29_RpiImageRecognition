import threading

import imagecomm_pb2
import imagecomm_pb2_grpc

import time
from concurrent import futures


class Listener(imagecomm_pb2_grpc.ImageCommServicer):

    def ProcessImage(self, request, context):
        imgArray = imagecomm_pb2.PicArray()
        # pass into model
        result = 1
        return result


class Image_Server:

    def __init__(self):
        self.algo_server = Listener()
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        imagecomm_pb2_grpc.add_ImageCommServicer_to_server(Listener(), self.server)
        self.server.add_insecure_port('0.0.0.0:10001')

    def connect(self):
        print('Starting Image Server on port: 10001.')
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


if __name__ == "__main__":
    Image_Server().connect()
