import paho.mqtt.client as mqtt
import time


class ClientMQTT:

    def __init__(self, ip_address, port):
        # super(ClientMQTT, self).__init__()
        self.ip_address = ip_address
        self.port = port

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.connect(ip_address, port, 60)

        # self.client.loop_forever()

    @staticmethod
    def on_connect(client, userdata, result_code):
        print('CONNECT|Result Code : ' + str(result_code))

    @staticmethod
    def on_message(self, userdata, msg):
        print('MESSAGE' + str(msg.payload))

    @staticmethod
    def on_publish(client, userdata, packet):
        # print('PUBLISHED ' + str(client))
        return

    def publish(self, topic, payload):
        print('PUBLISH ' + topic + " : " + payload)
        self.client.publish(topic, payload)

    def simulate(self):
        while True:
            self.publish('mqtt/test', 'iox')
            time.sleep(10)
