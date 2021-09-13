from src.comms.multicomms import Multicomms


def init():
    test = Multicomms()
    test.start()


if __name__ == '__main__':
    init()
