import grpc
import time

from src.comms import hdcomm_pb2
from src.comms import hdcomm_pb2_grpc


class Stm_Client:
    def __init__(self):
        self.stm_ip = '192.168.50.37'
        self.stm_port = '10002'
        self.stub = None

    # sends a ping request to ensure connection with stm
    def ping_request(self):
        print("Sending a ping request to the STM")
        # open a gRPC channel
        channel = grpc.insecure_channel(self.stm_ip+':'+self.stm_port)
        # create a valid request message
        request = hdcomm_pb2.PingResponse(device_time=time.time())
        # create a stub (client)
        self.stub = hdcomm_pb2_grpc.HdCommStub(channel)
        # make the call
        response = self.stub.Ping(request)
        print(response)

    def move_request(self, radius_index, distance):
        request = hdcomm_pb2.MoveRequest(radius_index=radius_index, distance=distance)
        response = self.stub.Move(request)
        print("Sending a move request")
        print(response)

    def move_cancel(self):
        print("Sending a cancel move request")
        response = self.stub.MoveCancel
