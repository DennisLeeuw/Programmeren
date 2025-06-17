import os
import platform

# Netwerk address
netaddr = "192.168.22"
ping_param = ''

# Check hoe we ping moeten aanspreken
if platform.system().lower() == 'windows':
    ping_param += '-n'
else:
    ping_param += '-c'

# Loop door de IP adressen 1 t/m 10 van ons netwerk
for addr in range(1,11):
    if addr == 5 or addr == 7:
        continue
    ip_addr = netaddr + "." + str(addr)

    response = os.system(f"ping " + ping_param + "1 " + ip_addr)

