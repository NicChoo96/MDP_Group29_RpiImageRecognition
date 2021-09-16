import concurrent.futures
import threading

import grpc
from concurrent import futures
import time

from src.comms import algocomm_pb2
from src.comms import algocomm_pb2_grpc


class Listener(algocomm_pb2_grpc.algoServicer):

    def ReceiveCoordinates(self, request, context):
        response = algocomm_pb2.ObstacleString()
        # Get obstacles string
        # ("OBS:X:Y:Dir:X:Y:Dir:...")
        response.obstacles = 'TEST'
        return response

    # commands the robot to move with a given radius index and distance
    # returns the estimated time required for move
    def Move(self, request, context):
        # TODO: some function to pass radius_index and distance to STM and get a return estimated time for move
        radius_index = request.radius_indexed
        distance = request.distance
        est_time = 123

        response = algocomm_pb2.MoveResponse()
        response.time_required = est_time
        return response

    def GetRadii(self, request, context):
        response = algocomm_pb2.RadiiResponse()
        # array of available turn radii.
        response.radii = []
        return response

    def MoveVirtual(self, request, context):
        robot_coordinates = request.robotCoordinates


class Algo_Server:
    def __init__(self):
        self.algo_server = Listener()
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        algocomm_pb2_grpc.add_algoServicer_to_server(Listener(), self.server)
        self.server.add_insecure_port('0.0.0.0:9999')

    def connect(self):
        print('Starting Algo server on port 9999.')
        self.server.start()
        try:
            while True:
                print("Number of threads: " + str(threading.active_count()))
                time.sleep(86400)

        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            self.server.stop(0)

    def disconnect(self):
        print("Disconnecting Algo server")


if __name__ == "__main__":
    Algo_Server().connect()
