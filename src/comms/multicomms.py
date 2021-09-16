import os
import time
import concurrent.futures
import threading

from src.comms import algo_server
#from src.comms import android_server
from src.comms import stm_client


# import stmclient.py
class Multicomms:

    def __init__(self):

        print("Initializing Multithreading Comms...")

        self.algo = algo_server.Algo_Server()
        #self.android = android_server.Android_Server()
        self.stm = stm_client.Stm_Client()

        #with concurrent.futures.ThreadPoolExecutor() as executor:
            #f1 = executor.submit(func, arg)
            #print(f1.results()) - print when is received
        # results = [executor.submit(do_something, 1) for _ in range(10)]
        # for f in concurrent.futures.as_completed(results):
        # results = executor.map(function, arg) - returns results in order of how they were started
    def start(self):
        try:
            t1 = threading.Thread(target=self.algo.connect)
            t2 = threading.Thread(target=self.stm.ping_request)

            t1.start()
            print("HERE1")
            t2.start()
            print("HERE2")

            t2.join()
            print("HERE3")
            t1.join()



        #try:
        #    with concurrent.futures.ThreadPoolExecutor() as executor:
        #        executor.submit(self.algo.connect())
        #        t2 = executor.submit(self.stm.ping_request())


        #        print(t2.results())
            #self.algo.connect()
            #self.android.connect()
            #self.stm.ping_request()


        except:
            return

    def checklist(self):
        android_string = self.android.read()

