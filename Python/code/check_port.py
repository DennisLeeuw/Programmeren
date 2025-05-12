try:
    import socket
except ModuleNotFoundError:
    exit("De 'socket' module is niet aanwezig op dit systeem")

# https://docs.python.org/3/library/socket.html

def port_check(HOST,PORT):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.settimeout(2) #Timeout in case of port not open
   try:
      s.connect((HOST, PORT))
      return True
   except:
      return False

ip = "127.0.1.1"
port = 80

if port_check(ip,port):
    print(f"On {ip} port {port} is open")
else:
    print(f"On {ip} port {port} is closed")

