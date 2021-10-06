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

    def CheckStart(self, request, context):
        response = algocomm_pb2.StartResponse()
        start = string_data.start
        response.start = start

        if start:
            print("[Sending start status to algo...] Start status:" + str(start)) 
        
        return response

    def ReceiveCoordinates(self, request, context):
        response = algocomm_pb2.ObstacleString()
        # Get obstacles string
        # ("OBS:X:Y:Dir:X:Y:Dir:...")
        
        obs_string = string_data.obs_value
        print(f"[Sending obstacle string to algo...]: {obs_string}")
        
        response.obstacles = obs_string
        return response

    def MoveVirtual(self, request, context):
        robot_coordinates = request.robotCoordinates
        string_data.robot_coord = robot_coordinates

        print(f"[Algo sent robot coordinates to Android]: Robot coordinates: {robot_coordinates}")
        
        return algocomm_pb2.Empty()

    def UpdateStatus(self, request, context):
        status_string = request.status
        # ST: RTS, RS, PLAN, MOV, STCI, IC, C

        f_result = (f"ST:{status_string}")
        string_data.status = f_result
        
        if status_string == 'C':
            print("Robot move completed. Terminating the server.")
            

        print(f"[Algo sent a status update to Android]: Status: {f_result}")

        return algocomm_pb2.Empty()

    # commands the robot to move with a given radius index and distance
    # returns the estimated time required for move
    def Move(self, request, context):
        # get the radius_index and move distance from the algo
        radius_index = request.radius_indexed
        distance = request.distance
        # send a move_request to the stm server, returns the time required for the move
        time_required = stm_client.Stm_Client().move_request(radius_index, distance)
        response = algocomm_pb2.MoveResponse(time_required=(time_required.ToNanoseconds() / 1e9))

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
    
        # the picture classification result. eg. id:1
    def TakePicture(self, request, context):
        result = image_client.Image_Client().process_pic()
        print(f"[Algo sent a take picture request to Image]: The result is {result}")
        if request.id == 0:
            print("Model did not identify any possible image")
        
        string_data.pic_result = (f"TT:{request.id}:{result}")

        print(f"Current pic_updated value is {string_data.pic_updated}")
        string_data.pic_updated = string_data.pic_updated + 1
        
        #time.sleep(1)
        return algocomm_pb2.Empty()
        

class Algo_Server:
    def __init__(self):
        self.algo_server = Listener()
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
        algocomm_pb2_grpc.add_algoServicer_to_server(self.algo_server, self.server)
        self.server.add_insecure_port('0.0.0.0:9999')
        self.connected = False

        print("Initializing Algo Server")

    def connect(self):
        print('Starting Algo server on port 9999.')
        self.server.start()
        self.connected = True
        try:
            while True:
                if self.connected:
                    print("Number of threads: " + str(threading.active_count()))
                    time.sleep(30)
                else:
                    break

        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            self.server.stop(0)

    def disconnect(self):
        print("Disconnecting Algo server")
        
        # send a move request to stop the robot before shutting down
        stm_client.Stm_Client().move_cancel()
        self.server.wait_for_termination(timeout=None)
        self.server.stop(None)


if __name__ == "__main__":
    Algo_Server().connect()
