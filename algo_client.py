# Get image from the rpi server and stitch them together
import grpc
import cv2
import numpy as np
from PIL import Image
from src.comms import algocomm_pb2
from src.comms import algocomm_pb2_grpc

# FOR TESTING
# Delon's home
#channel = grpc.insecure_channel('192.168.50.37:9999')
# in school
channel = grpc.insecure_channel('127.0.0.1:9999')
stub = algocomm_pb2_grpc.algoStub(channel)
empty = algocomm_pb2.Empty()

# move request test
#request = algocomm_pb2.MoveRequest(radius_indexed=0, distance=0.3)
#test = stub.Move(request)

# get radii test
# rpc GetRadii (Empty) returns (RadiiResponse);
# test = stub.GetRadii(empty)

# test_string = 'RP:1:3:N'
# request = algocomm_pb2.RobotPosition(robotCoordinates=test_string)
# stub.MoveVirtual(request)

start = False

while True:
    
    request = stub.CheckStart(empty)
    start = request.start
    
    if start:
        request = stub.ReceiveCoordinates(empty)
        obs_string = request.obstacles
        print(obs_string)
    

print("Algo Client End")
