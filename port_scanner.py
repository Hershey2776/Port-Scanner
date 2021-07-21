#!/usr/bin/python3

import socket
import threading
from queue import Queue


target = socket.gethostbyname(socket.gethostname())
port_range = range(0,1024)
queue = Queue()
open_ports = []



def scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        return True
    except:
        return False


def port_queue(port_range):
    for port in port_range:
        queue.put(port)

# def get_value():
#     port_range = int(input("Enter the upper range of the port selection"))


def scanner():
    while not queue.empty():
        port = queue.get()
        if scan(port):
            print(f"{port} is open")
            open_ports.append(port)

port_range = range(0,65565)
port_queue(port_range)

thread_list = []

for th in range(300):
    thread = threading.Thread(target=scanner)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print(f"Open ports are {open_ports}")


















