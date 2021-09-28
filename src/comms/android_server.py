from bluetooth import *


class Android_Server:
    def __init__(self):
        self.server_sock = None
        self.client_sock = None

        self.server_sock = BluetoothSocket(RFCOMM)
        self.server_sock.bind(("",PORT_ANY))
        self.server_sock.listen(1)
        self.port = self.server_sock.getsockname()[1]
        self.uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"


        advertise_service(self.server_sock, "MDPGroup29",
                          service_id=self.uuid,
                          service_classes=[self.uuid, SERIAL_PORT_CLASS],
                          profiles=[SERIAL_PORT_PROFILE]
                          )

        #if(self.port != 1):
        #    self.server_sock.close()
        #    Android_Server().init()
        #    print("Wrong port")

        print("Waiting for connection on RFCOMM channel %d" % self.port)

    def connect(self):
        while True:
            connected = False
            try:
                if self.client_sock is None:
                    self.client_sock, client_info = self.server_sock.accept()
                    print("Accepted connection from ", client_info)
                    connected = True

            except Exception as error:
                print("Connection failed: " + str(error))

            if not connected:
                break


    def disconnect(self):
        try:
            # connected to a client socket
            if self.client_sock is not None:
                self.client_sock.close()
                self.client_sock = None

            print("Android disconnected Successfully")

        except Exception as error:
            print("Android disconnect failed: " + str(error))

    def clear_socket(self):
        try:
            if self.client_sock is not None:
                self.client_sock.close()
                self.client_sock = None

            if self.server_sock is not None:
                self.server_sock.close()
                self.server_sock = None

            print("Cleared both server and client socket")

        except Exception as error:
            print("Clear socket failed: " + str(error))


    def read(self):
        try:
            if self.client_sock is None:
                return None 
                
            data = self.client_sock.recv(1024).strip()
            
            if data is None:
                return None

            if len(data) > 0:
                print("From android: [%s]" % data)
                return data
            
            return None
        

        except Exception as error:
            print("Android read failed: " + str(error))
            raise error

    def write(self, message):
        try:
            print("Writing to android: ")
            print(message)
            self.client_sock.send(message)

        except Exception as error:
            print("Android write failed: " + str(error))
            raise error


if __name__ == '__main__':
    Android_Server().connect()

