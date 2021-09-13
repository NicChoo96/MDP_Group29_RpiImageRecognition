from src.comms import multicomms


def init():
    test = multicomms.Multicomms()
    test.start()


if __name__ == '__main__':
    init()
