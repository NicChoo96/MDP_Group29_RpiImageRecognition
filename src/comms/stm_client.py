import grpc
import time

from src.comms import hdcomm_pb2
from src.comms import hdcomm_pb2_grpc

class Stm_Client:
    def __init__(self):
        a = 1

    def ping_request(self):
        print("Sending a ping request to the STM")
        # open a gRPC channel
        channel = grpc.insecure_channel('192.168.50.37:10002')

        # create a valid request message
        request = hdcomm_pb2.PingResponse(device_time=time.time())

        # create a stub (client)
        # temporary sub for yet-to-be-developed code
        stub = hdcomm_pb2_grpc.HdCommStub(channel)

        # make the call
        response = stub.Ping(request)

        print(response)
