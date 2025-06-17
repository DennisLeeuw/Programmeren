lst_netwerk = []

print("We vragen om 3 IP-adressen die in uw netwerk voorkomen")

while True:
    ip = input("Wat is IP-adres 1 in het netwerk? ")
    if ip not in lst_netwerk:
        lst_netwerk.append(ip)
        break
    print(f"IP-adres {ip} komt al in de lijst voor")

while True:
    ip = input("Wat is IP-adres 2 in het netwerk? ")
    if ip not in lst_netwerk:
        lst_netwerk.append(ip)
        break
    print(f"IP-adres {ip} komt al in de lijst voor")

while True:
    ip = input("Wat is IP-adres 3 in het netwerk? ")
    if ip not in lst_netwerk:
        lst_netwerk.append(ip)
        break
    print(f"IP-adres {ip} komt al in de lijst voor")

print("Uw netwerk bevat de volgende IP-adressen:")
print(lst_netwerk)

