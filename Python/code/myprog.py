import mylib

lst_netwerk = []

print("We vragen om 3 IP-adressen uit uw netwerk")

for i in range(1,4):
    antw = mylib.vraag_ip(i,lst_netwerk)
    lst_netwerk.append(antw)

print(lst_netwerk)
