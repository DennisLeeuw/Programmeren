import os
import platform

# Netwerk address
netaddr = "192.168.22"

# Check hoe we ping moeten aanspreken
if platform.system().lower() == 'windows':
    param = '-n'
else:
    param = '-c'

# Loop door de IP adressen 1 t/m 10 van ons netwerk
for addr in range(1,11):
    if addr == 5 or addr == 7:
        continue
    ip_addr = netaddr + "." + str(addr)

    response = os.system(f"ping " + param + "1 " + ip_addr)

