import imagecomm_pb2
import imagecomm_pb2_grpc
import grpc
from picamera import PiCamera
from picamera.array import PiRGBArray
import time

def take_picture():
    try:
        camera = PiCamera()
        camera.resolution = (640,480)
        # 3D RGB numpy array (row, col, colour)
        picArray = PiRGBArray(camera)
            
        # camera warm up time
        time.sleep(0.1)
        # OpenCV takes bgr
        camera.capture(picArray,format='jpeg')
        #image = picArray.array
        #print(image)
        camera.close()

        print('Image taken successfully')

    except Exception as error:
        print('Error while taking picture: ' + str(error))
        
    # converts the image into a 1D array   
    # array = image.reshape(-1)
    #print(array)
    return picArray

def process_pic():
    try:
        channel = grpc.insecure_channel('127.0.0.1:12345')
        stub = imagecomm_pb2_grpc.ImageCommStub(channel)
            
        # take picture and convert it to 1D
        picture = take_picture()
        
        # update image on server
        request = imagecomm_pb2.PicArray()
        #request.image.extend(picture)
        request.image = picture
            
        # result of the image recognition model
        print("Image processing...")
        result = stub.ProcessImage(request)
            
        print(result)
            
    except Exception as error:
        print("Error when processing picture: " + str(error))
        

if __name__ == "__main__":
    process_pic()

