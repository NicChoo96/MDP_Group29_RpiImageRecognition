import os

from src.comms.multicomms import Multicomms


def init():
    test = Multicomms()
    test.start()
    
    os.system("sudo hciconfig hci0 piscan")


if __name__ == '__main__':
    init()
