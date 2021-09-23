import os

from src.comms.multicomms import Multicomms


def init():

    os.system("sudo hciconfig hci0 piscan")

    test = Multicomms()
    test.start()


if __name__ == '__main__':
    init()
