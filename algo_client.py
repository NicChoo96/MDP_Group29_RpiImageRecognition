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
channel = grpc.insecure_channel('192.168.1.218:9999')
stub = algocomm_pb2_grpc.algoStub(channel)
empty = algocomm_pb2.Empty()

test = stub.TakePicture(empty)
