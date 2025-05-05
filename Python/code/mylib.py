def vraag_ip(nummer,net_lst):
    while True:
        ip = input(f"Wat is IP-adres nummer {nummer}: ")
        if ip not in net_lst:
            return(ip)
        print(f"IP-adres {ip} komt al in de lijst voor")

