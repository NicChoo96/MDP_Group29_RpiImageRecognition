import os
import time
import concurrent.futures
import threading

from src.comms import algo_server
from src.comms import android_server
from src.comms import stm_client


# import stmclient.py
class Multicomms:
    

    def __init__(self):

        print("Initializing Multithreading Comms...")

        self.algo = algo_server.Algo_Server()
        self.android = android_server.Android_Server()
        self.stm = stm_client.Stm_Client()

        #with concurrent.futures.ThreadPoolExecutor() as executor:
            #f1 = executor.submit(func, arg)
            #print(f1.results()) - print when is received
        # results = [executor.submit(do_something, 1) for _ in range(10)]
        # for f in concurrent.futures.as_completed(results):
        # results = executor.map(function, arg) - returns results in order of how they were started
    def start(self):
        try:
            #t1 = threading.Thread(target=self.algo.connect)
            #t2 = threading.Thread(target=self.stm.ping_request)
            #t3 = threading.Thread(target=self.android.connect)
            #t1.start()
            #t2.start()
            #t3.start()
            #t3.join()
            #t2.join()
            #t1.join()



        #try:
        #    with concurrent.futures.ThreadPoolExecutor() as executor:
        #        executor.submit(self.algo.connect())
        #        t2 = executor.submit(self.stm.ping_request())


        #        print(t2.results())
            self.android.connect()
            self.stm.ping_request()
            t1 = threading.Thread(target=self.algo.connect)
            t2 = threading.Thread(target=self.checklist_a1)
            #t3 = threading.Thread(target=self.read_android)
            #t4 = threading.Thread(target=self.write_android, args=['Hi RPI, MDPGRP29'])
            
            t1.start()
            t2.start()
            print("checklist")
            #t3.start()
            #t4.start()
            t2.join()
            print("check list end")
            t1.join()
            


        except Exception as error:
            raise error

    def checklist_a1(self):
        while True:
            radius_index = 0
            distance = 0.001
            android_string = self.android.read()
            new = android_string.decode().split("'")
            print(new)
            print(new[0])
            
            if (new[0] == 'F'):
                radius_index = 0
                distance = 0.5
                print("FFF")
            elif (new[0] == 'TR'):
                radius_index = -1
                distance = 0.1
                print("TRTRTR")
            elif (new[0] == 'TL'):
                radius_index = 1
                distance = 0.1
            elif (new[0] == 'R'):
                radius_index = 0
                distance = -0.5
            else:
                radius_index = 0
                distance = 0.001
                
            try:
                self.stm.move_request(radius_index,distance)
                self.android.write("Moving...")
                time.sleep(5)
            except Exception as error:
                print(error)
                raise error
        
    def read_android(self):
        while True:
            android_string = self.android.read()
            print(android_string)
    
    def write_android(self, message):
        time.sleep(20)
        self.android.write(message)
            
            
        

