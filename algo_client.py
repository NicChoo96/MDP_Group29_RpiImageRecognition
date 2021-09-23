# Get image from the rpi server and stitch them together
import grpc
import cv2
import numpy as np
from PIL import Image
from src.comms import algocomm_pb2
from src.comms import algocomm_pb2_grpc

# Delon's home
channel = grpc.insecure_channel('192.168.50.37:9999')
# in school
#channel = grpc.insecure_channel('127.0.0.1:9999')
stub = algocomm_pb2_grpc.algoStub(channel)
empty = algocomm_pb2.Empty()

image = stub.GetPicture(empty)
array = []
array.append(image.image)
a = np.array(array)
newarr = a.reshape(480,640,3)
# reshape and form as an image?
print(newarr.shape)
print(type(newarr))
print(newarr)

cv2.imwrite('image.png',newarr)
#im = cv2.imread('image.png')
#cv2.imshow('Test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
