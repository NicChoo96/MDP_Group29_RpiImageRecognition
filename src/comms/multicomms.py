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
from src.comms import camera_setup

from src.comms import image_client

from src.comms import imagecomm_pb2
from src.comms import imagecomm_pb2_grpc



# import stmclient.py
class Multicomms:
    
    def __init__(self):

        print("Initializing Multithreading Comms...")

        self.algo = algo_server.Algo_Server()
        self.android = android_server.Android_Server()
        self.stm = stm_client.Stm_Client().ping_request()
        
        string_data.init()
        camera_setup.init()

    def start(self):
        try:

            t1 = threading.Thread(target=self.algo.connect)
            t2 = threading.Thread(target=self.android.connect)
            t3 = threading.Thread(target=self.write_android)
            t4 = threading.Thread(target=self.read_android)
            
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t4.join()
            t3.join()
            t2.join()
            t1.join()
            print("All threads terminated.")
            
        except Exception as error:
            raise error

        
    def read_android(self):
        while True:
            try:
                android_string = self.android.read()
                
                # no read yet
                if android_string is None:
                    continue
                
                # OBS String has been sent

                android_string = android_string.decode("utf-8")
                print(f"[Decoded string is...] : {android_string}")
                
                # check if start is issued 
                if android_string == 'START':
                    if string_data.obs_value != 'No value':
                        string_data.start = True
                        print("Android read thread is closed")
                        self.timer()
                        break
                    print("Can't start. You have not given the obstacle information...")
                    continue
                
                # update obs_value only if its different
                string_data.obs_value = android_string
                
                string_data.obs_count = self.count_obstacle(android_string)
                print(f"[OBS COUNT]:{string_data.obs_count}")

            except Exception as error:
                print(str(error))
                
    
    def write_android(self):
        curr_robot_coord = "No value"
        curr_status = "No value"
        curr_pic_updated = 0

        while True:
            # updating RP
            if string_data.robot_coord != curr_robot_coord:
                self.android.write(string_data.robot_coord)
                curr_robot_coord = string_data.robot_coord
                time.sleep(0.5)
                # unlock
            
            # move status
            if string_data.status != curr_status:
                self.android.write(string_data.status)
                curr_status = string_data.status
                time.sleep(0.5)

            if string_data.pic_updated != curr_pic_updated:
                self.android.write(string_data.pic_result)
                curr_pic_updated = string_data.pic_updated
                time.sleep(0.5)

            # robot completed movement
            if string_data.status == 'C':
                time.sleep(5)
                self.disconnect()

    def count_obstacle(self, obs_string):
        text = obs_string.split(':X')
        count = 8 - (len(text)-1)
        return int(count)

    # this function handles the shutdown of the robot
    def timer(self):
        time.sleep(240)
        self.disconnect()


    def disconnect(self):
        print("Terminating connection with android and algo")
        self.algo.disconnect()
        self.android.disconnect()