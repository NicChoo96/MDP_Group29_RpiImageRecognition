import bluetooth as bt


class Android_Server:
    def __init__(self):
        self.a = 1

    def connect(self):
        self.a = 2
        print("TODO: Bluetooth connect.")

    def disconnect(self):
        return

    def read(self):
        return

    def write(self, message):
        try:
            print("Writing to android: ")
            print(message)
            self.client.sock.send(message)

        except Exception as error:
            print("Android write failed: " + str(error))
            raise error
