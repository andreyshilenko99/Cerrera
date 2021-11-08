import socket
import celery
from celery.app.control import Inspect
from celery.exceptions import MaxRetriesExceededError
# from django.apps import apps
from google.protobuf import json_format
import datetime
from Trace import found_signal_params_pb2


# Добавить поддержку нескольких стрижей
# Херовая расшифровка сообщений

def trace_info():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.settimeout(5)
    s.connect(('192.168.2.241', 10100))
    while True:
        try:
            # # srizhes = apps.get_model('geo', 'Strizh').objects.all()
            # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # # s.settimeout(5)
            # s.connect(('192.168.2.241', 10100))

            # Point = apps.get_model('geo', 'Point')
            print('works')
            # print(f'connect to {i}, port {port}')
            data = s.recv(1024)
            # s.close()
            print(data)
            signal = found_signal_params_pb2.FoundSignalParams()
            signal.ParseFromString(data[14::])
            signal_dict = json_format.MessageToDict(signal)
            print(signal_dict)
            # if signal_dict:
            # point = Point(drone_id=0,
            #               system_name=str(signal_dict['systemName']),
            #               center_freq=signal_dict['centerFrequencyHz'],
            #               brandwidth=signal_dict['bandwidthHz'], detection_time=signal_dict['detectionTime'],
            #               comment_string=signal_dict['commentString'],
            #               drone_lat=float(signal_dict['location']['latitude']),
            #               drone_lon=float(signal_dict['location']['longitude']),
            #               remote_lat=0,
            #               remote_lon=0,
            #               azimuth=signal_dict['location']['name'],
            #               area_sector_start_grad=float(signal_dict['location']['areaSectorStartGrad']),
            #               area_sector_end_grad=float(signal_dict['location']['areaSectorEndGrad']),
            #               area_radius_m=float(signal_dict['location']['areaRadiusM']),
            #               ip='192.168.2.241',
            #               current_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            #               height=0,
            #               strig_name="strizh")
            # point.save()
        except (
        ConnectionRefusedError, BrokenPipeError, OSError, socket.timeout, MaxRetriesExceededError, IOError) as e:
            print(e)
            pass


# trace_info()
