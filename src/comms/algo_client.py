# Not our problem
import grpc
import algocomm_pb2
import algocomm_pb2_grpc

# open a gRPC channel
# channel = grpc.insecure_channel('192.168.1.216:9999')
channel = grpc.insecure_channel('127.0.0.1:9999')

# create a valid request message
# number = algocomm_pb2.Number(value=16)
request = algocomm_pb2.Request(requested=True)

# create a stub (client)
# temporary sub for yet-to-be-developed code
stub = algocomm_pb2_grpc.AlgoCommsStub(channel)

# make the call
response = stub.getLocation(request)

#print(response.x)

print("x:" + str(response.x) + " | y:" + str(response.y))