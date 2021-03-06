import socket
import time
from django.apps import apps
from Trace import trace_remote_pb2 as con


def check_state(host):
    message = con.TraceRemoteMessage()
    message.message_type = 7
    lel = message.SerializeToString()
    port = 10100  # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.settimeout(0.3)
        s.connect((host, port))
        s.send(bytearray(lel))
        data = s.recv(1024)
        print(data)
        data = data[9:-8]
        print(data)
        s.close()
    except (socket.timeout, ConnectionRefusedError, OSError) as e:
        print(e)
        s.close()
        data = 'KAL'
    if data == b'\x00\x10\x00':
        return "all_stop"
    elif data == b'\x01\x10\x00':
        return "scan_on"
    elif data == b'\x00\x10\x01':
        return "jammer_on"
    elif data == 'KAL':
        return "no_connect"
    else:
        return "no_connect"


def scan_on_off(host):
    # TODO Исключения
    message = con.TraceRemoteMessage()
    message.message_type = 0
    mes = message.SerializeToString()
    print(message)
    port = 10100  # The same port as used by the server
    _try = 0
    if check_state(host) == "jammer_on":
        while _try < 3:
            state = check_state(host)
            while state == "jammer_on":
                scan_on_off(host)
                time.sleep(1)
                state = check_state(host)
    if check_state(host) == "all_stop":
        while _try < 3:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.send(bytearray(mes))
            data = s.recv(1024)
            print(data)
            s.close()
            time.sleep(1)
            if data and check_state(host) == "scan_on":
                return "scan_on"
            elif _try > 3:
                return "error"
            else:
                _try += 1

    elif check_state(host) == "scan_on":
        while _try < 3:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.send(bytearray(mes))
            data = s.recv(1024)
            print(data)
            s.close()
            time.sleep(1)
            if data and check_state(host) == "all_stop":
                return "all_stop"
            elif _try > 3:
                return "error"
            else:
                _try += 1


def jammer_on_off(host):
    # TODO Исключения
    message = con.TraceRemoteMessage()
    message.message_type = 1
    mes = message.SerializeToString()
    print(message)
    port = 10100  # The same port as used by the server
    _try = 0
    if check_state(host) == "scan_on":
        state = check_state(host)
        while state == "scan_on":
            scan_on_off(host)
            time.sleep(1)
            state = check_state(host)
    if check_state(host) == "all_stop":
        while _try < 3:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.send(bytearray(mes))
            data = s.recv(1024)
            print(data)
            s.close()
            if data and check_state(host) == "jammer_on":
                return "jammer_on"
            elif _try > 3:
                return "error"
            else:
                _try += 1
    elif check_state(host) == "jammer_on":
        while _try < 3:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.send(bytearray(mes))
            data = s.recv(1024)
            print(data)
            s.close()
            if data and check_state(host) == "all_stop":
                return "all_stop"
            elif _try > 3:
                return "error"
            else:
                _try += 1


