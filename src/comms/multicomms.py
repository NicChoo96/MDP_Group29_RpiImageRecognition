import os

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

    def start(self):
        try:
            self.algo.connect()
            self.android.connect()
            self.stm.ping_request()
        except:
            return
