from client_mqtt import ClientMQTT
from threading import Thread
import serial

mqtt_server = '10.0.0.17'
mqtt_port = 1883


def write_mqtt(topic, payload):
    mqtt_client = ClientMQTT(ip_address=mqtt_server, port=mqtt_port)
    mqtt_client.publish('mqtt/' + topic, payload)


def start_server_mqtt():
    print('Connecting MQTT Client on port ' + mqtt_port)
    mqtt_client = ClientMQTT(ip_address=mqtt_server, port=mqtt_port)
    mqtt_client.simulate()


def start_server_serial():
    port = '/dev/ttyS1'
    ser = serial.Serial(port, 9600, timeout=1)
    print(ser.name)
    while True:

        try:
            s = ser.read(4)
            print(s)  # Debug print
            s_value = int(s)

            if s_value > 85:
                print('ALERT|' + s)
                write_mqtt('test', s)
                # print(s_value)

        except ValueError:
            print('ERROR|Value')

    ser.close()
    return


def main():

    st = Thread(target=start_server_serial, args=())
    st.start()

    # Used for just throwing data at the MQTT server from the IOx application
    # mt = Thread(target=start_server_mqtt, args=())
    # mt.start()


if __name__ == '__main__':
    main()
