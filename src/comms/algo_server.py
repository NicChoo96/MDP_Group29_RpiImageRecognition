import concurrent.futures
import threading

import grpc
from concurrent import futures
import time

from src.comms import algocomm_pb2
from src.comms import algocomm_pb2_grpc

from src.comms import stm_client
from src.comms import image_client
from src.comms import string_data


class Listener(algocomm_pb2_grpc.algoServicer):

    def __init__(self):
        #self.stm = stm_client.Stm_Client()
        #self.img = image_client.Image_Client()
        pass

    def ReceiveCoordinates(self, request, context):
        response = algocomm_pb2.ObstacleString()
        # Get obstacles string
        # ("OBS:X:Y:Dir:X:Y:Dir:...")
        
        obs_string = string_data.obs_value
        
        print(f"[Sending obstaacle string to algo...]: {obs_string}")
        
        if m != "No value":
            response.obstacles = m
            
        return response

    def MoveVirtual(self, request, context):
        robot_coordinates = request.robotCoordinates
        string_data.robot_coord = robot_coordinates

        print(f"[Algo sent robot coordinates to Android]: Robot coordinates: {robot_coordinates}")
        
        return algocomm_pb2.Empty()

    def UpdateStatus(self, request, context):
        status_string = request.status
        string_data.status = status_string
        
        print(f"[Algo sent a status update to Android]: Robot coordinates: {status_string}")

        return algocomm_pb2.Empty()

    # commands the robot to move with a given radius index and distance
    # returns the estimated time required for move
    def Move(self, request, context):
        # get the radius_index and move distance from the algo
        radius_index = request.radius_indexed
        distance = request.distance
        # send a move_request to the stm server, returns the time required for the move
        time_required = stm_client.Stm_Client().move_request(radius_index, distance)
        response = algocomm_pb2.MoveResponse(time_required=(time_required.seconds-1e-9))

        print(f"[Algo sent a move request to the Stm]: Radius_index: {radius_index}, Distance: {distance}, Time required: {time_required}")
        return response

    # rpc GetRadii (Empty) returns (RadiiResponse);
    # get a list of available turn radii.
    def GetRadii(self, request, context):
        # send a request to get
        radii = stm_client.Stm_Client().get_radii()
        response = algocomm_pb2.RadiiResponse(radii=radii)

        print(f"[Algo sent a get radii request to the Stm]: List of radii: {radii}")
        return response
    
    def TakePicture(self, request, context):
        image_client.Image_Client().process_pic()
        print("[Algo sent a take picture request to Image]")
        return algocomm_pb2.Empty()
        

class Algo_Server:
    def __init__(self):
        self.algo_server = Listener()
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        algocomm_pb2_grpc.add_algoServicer_to_server(self.algo_server, self.server)
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
