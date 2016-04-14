import serial
import time
import random


def main():

    port = 'COM4'
    ser = serial.Serial(port, 9600, timeout=1)
    print(ser.name)
    while True:

        value = random.randrange(0, 100)
        print(value)

        ser.write(str(value).encode())

        time.sleep(1)

    ser.close()
    return

if __name__ == '__main__':
    main()
