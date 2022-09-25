import logging
import os
import socket
import random
#from alive_progress import alive_bar

logger = logging.getLogger(__name__)
stream = logging.StreamHandler()
file = logging.FileHandler('server.log')
stream.setLevel(logging.WARNING)
file.setLevel(logging.ERROR)
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
stream.setFormatter(formater)
file.setFormatter(formater)
logger.addHandler(stream)
logger.addHandler(file)
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

devices = []

for devise in os.popen('arp -a'):
    devices.append(devise.split()[1].strip("()"))

#filter

for i in devices:
    if not i.startswith('192'):
        devices.remove(i)

random.shuffle(devices)

port = 8000
# def connect():
#     for device in devices:
#         try:
#             my_socket.connect((device, port))
#             make_server = False
#             print(f"Connected to {device}")
#             break
#         except socket.error as error:
#             logger.error(f'{error} on {device}')

# with alive_bar(1000, force_tty=True) as bar:
for device in devices:
    try:
        my_socket.connect(("192.168.4.24", port))
        make_server = False
        print(f"Connected to {device}")
        break
    except socket.error as error:
        logger.error(f'{error} on {device}')


