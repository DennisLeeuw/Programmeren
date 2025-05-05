#!/usr/bin/python

# 2025 03 10 DL Check for OS (platform)
# 2025 03 09 DL Eerste versie

import os
import platform

server_ips = ["127.0.0.1", "192.168.10.1", "192.168.10.4", "192.168.10.5", "192.168.10.10", "192.168.10.55", "192.168.10.56"]

# Als windows gebruik -n anders -c (linux) als optie voor ping
my_platform = platform.system().lower()
if my_platform=='windows':
    param = '-n'
else:
    param = '-c'

# Loop door de ip adressen, we gebruiken FOR omdat we een lijst hebben.
for ip in server_ips:
    # Enkelvoudige ping naar CMD
    response = os.system(f"ping " + param + "1 " + ip)

    # Controleer de RETURN code
    # 0 is foutloos (ping returns)
    # iets anders is er is een fout
    if response == 0:
        print(f"{ip} is UP")
    else:
        print(f"{ip} is DOWN")

# END
