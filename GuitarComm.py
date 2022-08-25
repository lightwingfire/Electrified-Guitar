#https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0

#https://stackoverflow.com/questions/24214643/python-to-automatically-select-serial-ports-for-arduino

from serial import *
import serial.tools.list_ports
import time

class GuitarComm:

    def __init__(self):
        print("starting guitar")

    def startConnect(self):
        #finds the arduino
        try:
            comPort = "COM5"
            ports = list(serial.tools.list_ports.comports())
            for p in ports:
                print(p)
                if "CH340" in p.description:
                    comPort = p[0]

            print(f"watching for arduino is on {comPort}")

            self.arduino = serial.Serial(port=comPort,baudrate = 115200, timeout =.1)
        except:
            print("COULD NOT FIND ARDUINO")

    def shock(self, duration):
        self.arduino.write(("s"+str(duration)).encode('utf-8'))
        time.sleep(0.05)
        print(self.arduino.readline())

    def pressedRestart(self):
        if self.arduino.readline() == 'r':
            return True
        else:
            return False



#finds the arduino
# comPort = "COM5"
# ports = list(serial.tools.list_ports.comports())
# for p in ports:
#     print(p)
#     if "CH340" in p.description:
#         comPort = p[0]

# print(f"watching for arduino is on {comPort}")

# arduino = serial.Serial(port=comPort,baudrate = 115200, timeout =.1)

# def write_read(x):
#     arduino.write(x.encode('utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return data

# while True:
#     num = input("Enter a number: ") # Taking input from user
#     value = write_read(num)
#     print(value) # printing the value




