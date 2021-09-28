import imagecomm_pb2
import imagecomm_pb2_grpc
import grpc
from picamera import PiCamera
from picamera.array import PiRGBArray
import time

def take_picture():
    try:
        camera = PiCamera(resolution = '640x480')
        # 3D RGB numpy array (row, col, colour)
        picArray = PiRGBArray(camera)
            
        # camera warm up time
        time.sleep(2)
        # OpenCV takes bgr
        camera.capture(picArray, format='bgr')
        image = picArray.array
        camera.close()

        print('Image taken successfully')

    except Exception as error:
        print('Error while taking picture: ' + str(error))
        
    # converts the image into a 1D array   
    array = image.reshape(-1)
    #print(array)
    return array

def process_pic():
    try:
        channel = grpc.insecure_channel('192.168.1.218:12345')
        stub = imagecomm_pb2_grpc.ImageCommStub(channel)
            
        # take picture and convert it to 1D
        picture = take_picture()
        
        # update image on server
        request = imagecomm_pb2.PicArray()
        request.image.extend(picture)
            
        # result of the image recognition model
        print("Image processing...")
        result = stub.ProcessImage(request)
            
        print(result)
            
    except Exception as error:
        print("Error when processing picture: " + str(error))
        

if __name__ == "__main__":
    process_pic()

