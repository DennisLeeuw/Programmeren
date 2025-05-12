import requests

host="google.com"
domain="www.google.com"

def check_virtual_host(ip, domain):
    url = f"http://{ip}"
    headers = {
        "Host": domain
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            print(f"De server op {ip} reageert op domein '{domain}' (HTTP {response.status_code}).")
        else:
            print(f"De server op {ip} reageert, maar gaf status {response.status_code} voor domein '{domain}'.")
    except requests.ConnectionError:
        print(f"Geen verbinding mogelijk met {ip}.")
    except requests.Timeout:
        print(f"Timeout bij het verbinden met {ip}.")
    except requests.RequestException as e:
        print(f"Er trad een fout op: {e}")

check_virtual_host(host,domain)

exit()

if __name__ == "__main__":
    ip_adres = input("Voer het IP-adres van de server in: ")
    domeinnaam = input("Voer de domeinnaam in (bijv. example.com): ")
    check_virtual_host(ip_adres, domeinnaam)
