ip = '192.168.12.67'
mask = '11111111111111111111111111111'
mask = 11111000

ip_part = ip.split('.')

#for part in ip_part:
#    part_bin = bin(int(part))[2:]
#    
#    print(part_bin)

part = 67
part_bin = int(bin(int(part))[2:])

net = part_bin & mask

#net_dec = int(net,2)

print(net)
print(net_dec)

