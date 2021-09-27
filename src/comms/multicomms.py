import os
import time
import concurrent.futures
import threading
import grpc

from picamera import PiCamera

from picamera.array import PiRGBArray

from src.comms import algo_server
from src.comms import android_server
from src.comms import stm_client
from src.comms import string_data

from src.comms import imagecomm_pb2
from src.comms import imagecomm_pb2_grpc



# import stmclient.py
class Multicomms:
    
    def __init__(self):

        print("Initializing Multithreading Comms...")

        self.algo = algo_server.Algo_Server()
        self.android = android_server.Android_Server()
        #self.stm = stm_client.Stm_Client()
        
        string_data.init()

    def start(self):
        try:

        #try:
        #    with concurrent.futures.ThreadPoolExecutor() as executor:
        #        executor.submit(self.algo.connect())
        #        t2 = executor.submit(self.stm.ping_request())


        #        print(t2.results())
            #self.android.connect()
            #self.stm.ping_request()
            t1 = threading.Thread(target=self.algo.connect)
            t2 = threading.Thread(target=self.android.connect)
            t3 = threading.Thread(target=self.read_android)
            #t2 = threading.Thread(target=self.checklist_a1)
            #t3 = threading.Thread(target=self.read_android)
            #t4 = threading.Thread(target=self.write_android, args=['Hi RPI, MDPGRP29'])
            
            t1.start()
            t2.start()
            time.sleep(15)
            t3.start()
            #print("checklist")
            #t3.start()
            #t4.start()
            t3.join()
            t2.join()
            t1.join()
            print("end")
            
        except Exception as error:
            raise error

        
    def read_android(self):
        while True:
            try:
                android_string = self.android.read()
                android_string = android_string.decode("utf-8")
                print(f"[Decoded string is...] : {android_string}]")
                
                if android_string is None:
                    continue
                # TODO: Check if android_string is obs
                string_data.obs_value = android_string
            
            except Exception as error:
                print(str(error))
                
    
    def write_android(self):
        time.sleep(20)
        self.android.write(message)
    

    def take_picture(self):
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

    def process_pic(self):
        try:
            channel = grpc.insecure_channel('127.0.0.1:12345')
            stub = imagecomm_pb2_grpc.ImageCommStub(channel)
            
            # take picture and convert it to 1D
            picture = self.take_picture()
        
            # update image on server
            request = imagecomm_pb2.PicArray()
            request.image.extend(picture)
            
            # result of the image recognition model
            print("Image processing...")
            result = stub.ProcessImage(request)
            
            print(result)
            
        except Exception as error:
            print("Error when processing picture: " + str(error))
