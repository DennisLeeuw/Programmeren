# Functie
def vraag_ip(nummer):
    while True:
        ip = input(f"Wat is IP-adres nummer {nummer} in uw netwerk? ")
        if ip not in lst_netwerk:
            return(ip)
        print(f"IP-adres {ip} komt al in de lijst voor")


# Hoofdprogramma
lst_netwerk = []

print("We vragen om 3 IP-adressen in uw netwerk:")

for i in range(1,4):
    antw = vraag_ip(i)
    lst_netwerk.append(antw)

print("U heeft deze IP-adressen in uw netwerk:")
print(lst_netwerk)

