import threading

import grpc
from concurrent import futures
import time

from src.comms import algocomm_pb2
from src.comms import algocomm_pb2_grpc


class Listener(algocomm_pb2_grpc.AlgoCommsServicer):

    def getLocation(self, request, context):
        # get value of Number
        response = algocomm_pb2.Location()
        response.x = 123
        response.y = 456
        return response

    def test(self, request, context):
        print("TEST")
        return "Test"


# create a gRPC server
class Algo_Server:
    def __init__(self):
        a = 1

    def connect(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        algocomm_pb2_grpc.add_AlgoCommsServicer_to_server(Listener(), server)

        # listen on every available ip
        server.add_insecure_port('0.0.0.0:9999')
        print('Starting Algo server... Listening on port 9999.')
        server.start()
        try:
            while True:
                print("Number of threads: " + str(threading.active_count()))
                time.sleep(86400)
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            server.stop(0)


if __name__ == "__main__":
    Algo_Server.connect()
