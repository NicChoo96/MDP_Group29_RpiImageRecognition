from google.protobuf import empty_pb2
import grpc
import time

from src.comms import hdcomm_pb2
from src.comms import hdcomm_pb2_grpc

class Stm_Client:

    empty = hdcomm_pb2.google_dot_protobuf_dot_empty__pb2.Empty()

    def __init__(self):
        #self.stm_ip = '192.168.50.37'
        self.stm_ip = '127.0.0.1'
        self.stm_port = '10002'
        # open a gRPC channel
        self.channel = grpc.insecure_channel('{}:{}'.format(self.stm_ip, self.stm_port))
        # create a stub (client)
        self.stub = hdcomm_pb2_grpc.HdCommStub(self.channel)

    # sends a ping request to ensure connection with stm
    def ping_request(self):
        print("Sending a ping request to the STM")
        
        try:
            request = hdcomm_pb2.PingResponse(device_time=time.time())
            response = self.stub.Ping(request)
            print(response)
            return
        
        except Exception as error:
            print("Ping request failed")
            print(str(error))
            

    def move_request(self, radius_index, distance):
        try: 
            request = hdcomm_pb2.MoveRequest(radius_indexed=radius_index, distance=distance)
            # rpc Move (MoveRequest) returns (MoveResponse);
            response = self.stub.Move(request)
            return response.time_required
        
        except Exception as error:
            print("Move request failed")
            print(str(error))

    def move_cancel(self):
        print("Sending a cancel move request")
        try:
            self.stub.MoveCancel(empty_pb2)
        
        except Exception as error:
            print("Move cancel failed")
            print(str(error))

    def get_radii(self):
        try:
            response = self.stub.GetRadii(empty)
            return response.radii
        
        except Exception as error:
            print("Get radii request failed")
            print(str(error))

    def get_heading(self):
        return

    def get_front_dist(self):
        return



