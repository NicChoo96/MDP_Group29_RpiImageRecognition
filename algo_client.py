# Not our problem
import grpc
from src.comms import algocomm_pb2
from src.comms import algocomm_pb2_grpc

# open a gRPC channel
# channel = grpc.insecure_channel('192.168.1.216:9999')
channel = grpc.insecure_channel('127.0.0.1:9999')

# create a valid request message
# number = algocomm_pb2.Number(value=16)
algocomm_pb2.Request(requested=True)

# create a stub (client)
# temporary sub for yet-to-be-developed code
stub = algocomm_pb2_grpc.AlgoCommsStub(channel)
empty = algocomm_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
# make the call
response = stub.getLocation(empty)
try:
    stub.test(empty)

except:
    print("x:" + str(response.x) + " | y:" + str(response.y))