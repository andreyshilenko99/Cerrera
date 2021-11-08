import multiprocessing
import os
import socket
from datetime import datetime
from multiprocessing import Process, Pool, Queue
from peewee import *
import pika
from info.check_uniping import main_check
from google.protobuf import json_format
from Trace import trace_remote_pb2

pg_db = PostgresqlDatabase('stuff', user='dron', password='555',
                           host='localhost', port=5432)

pg_db.connect()







class geo_strigstate(Model):
    strig_name = CharField()
    ip1_state = CharField()
    ip2_state = CharField()
    temperature = CharField()
    temperature_state = CharField()
    wetness = CharField()
    wetness_state = CharField()
    cooler = CharField()

    class Meta:
        database = pg_db


class geo_strizh(Model):
    name = CharField()
    lat = FloatField()
    lon = FloatField()
    ip1 = CharField()
    ip2 = CharField()
    uniping_ip = CharField()
    radius = FloatField()
    seconds_drone_show = IntegerField()

    class Meta:
        database = pg_db


class geo_point(Model):
    drone_id = CharField()
    system_name = CharField()
    center_freq = FloatField()
    brandwidth = FloatField()
    detection_time = CharField()
    comment_string = CharField()
    drone_lat = FloatField()
    drone_lon = FloatField()
    remote_lat = FloatField()
    remote_lon = FloatField()
    azimuth = CharField()
    area_sector_start_grad = FloatField()
    area_sector_end_grad = FloatField()
    area_radius_m = FloatField()
    ip = CharField()
    current_time = CharField()
    height = FloatField()
    strig_name = CharField()

    class Meta:
        database = pg_db


class Kringe(Exception):
    def __init__(self, host_name):
        self.txt = "Error on host " + host_name


class Connection:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.sock.connect((self.host, self.port))


class CommandConnect(object):
    def __init__(self, host, port, name):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.sock.connect((self.host, self.port))
        self.name = name

    # def __init__(self, sock):
    #     self.sock = sock

    # def connect(self):
    #     self.sock.connect((self.host, self.port))

    def data_recv(self):
        while True:
            data = self.sock.recv(1024)
            # print(data)
            data = decode_data_msg(data)
            if len(data) > 0 and data['messageType'] == 'ALARM':
                data = data['alarmState']['signalParams']
                point = geo_point(drone_id=0,
                                  system_name=str(data['systemName']),
                                  center_freq=data['centerFrequencyHz'],
                                  brandwidth=data['bandwidthHz'], detection_time=data['detectionTime'],
                                  comment_string=data['commentString'],
                                  drone_lat=float(data['location']['latitude']),
                                  drone_lon=float(data['location']['longitude']),
                                  remote_lat=0,
                                  remote_lon=0,
                                  azimuth=data['location']['name'],
                                  area_sector_start_grad=float(data['location']['areaSectorStartGrad']),
                                  area_sector_end_grad=float(data['location']['areaSectorEndGrad']),
                                  area_radius_m=float(data['location']['areaRadiusM']),
                                  ip=self.host,
                                  current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                  height=0,
                                  strig_name=self.name)
                point.save()
            elif len(data) > 0 and data['messageType'] == 'SCANNER_BUTTON_TOGGLE':
                state = data['buttonState']['isEnabled']
                print(state)
            # elif data['message'] = ''
            else:
                pass

    def send_command(self, command):
        self.sock.send(bytearray(command))

    def close_connection(self):
        self.sock.close()

    def set_timeout(self, timeout):
        self.sock.settimeout(timeout)

    def check_state(self):
        message = trace_remote_pb2.TraceRemoteMessage()
        message.message_type = 7
        serialized_command = message.SerializeToString()
        self.send_command(bytearray(serialized_command))

    def jammer_on_off(self):
        message = trace_remote_pb2.TraceRemoteMessage()
        message.message_type = 1
        serialized_command = message.SerializeToString()
        self.send_command(bytearray(serialized_command))

    def scan_on_off(self):
        message = trace_remote_pb2.TraceRemoteMessage()
        message.message_type = 0
        serialized_command = message.SerializeToString()
        self.send_command(bytearray(serialized_command))


def decode_data_msg(data):
    information_length = int.from_bytes(data[0:4], byteorder='little', signed=True)
    data = data[4:len(data)]
    data = data[:information_length]
    decoder_obj = trace_remote_pb2.TraceRemoteMessage()
    decoder_obj.ParseFromString(data)
    msg = json_format.MessageToDict(decoder_obj)
    print(msg)
    return msg


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def double(i):
    print("I'm process", os.getpid())
    return i * 2


connections_list = []
process_list = []
port = 10100


def start_process():
    try:
        # if len(dead_hosts) != 0:
        #     for i in dead_hosts:
        #         connection  = CommandConnect(i, port, i)
        #         connections_list.append(connection)
        #
        hosts = geo_strizh.select().dicts()
        for i in hosts:
            connection_ip1 = CommandConnect(i['ip1'], port, i['name'])
            # connection_ip2 = CommandConnect(i['ip2'], port, i['name'])
            connections_list.append(connection_ip1)
            # connections_list.append(connection_ip2)
            print(connections_list)
        for i in connections_list:
            p = Process(target=i.data_recv, name=i.host, args=())
            p.start()
            process_list.append(p)
            # info(p)
            # print(process_list)
        # for i in connections_list:
        #     print(i)
        #     i.scan_on_off()
    except (
            ConnectionRefusedError, BrokenPipeError, OSError, socket.timeout,
            IOError) as e:
        print(e)
        print(connections_list)
        # start_process()


def check_process():
    if len(process_list) == 0:
        pass
    else:
        for i in process_list:
            if i.is_alive():
                pass
            else:
                start_process()


def send_command(command):
    if command == 'jammer_on_off':
        for i in connections_list:
            i.jammer_on_off()
    elif command == 'scan_on_off':
        for i in connections_list:
            i.scan_on_off()
    elif command == 'check_state':
        for i in connections_list:
            i.check_state()


start_process()
send_command('jammer_on_off')
