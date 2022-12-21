from colorama import Fore,init
import requests
import subprocess
import socket
init()





hostname = socket.gethostname()
ip_local = socket.gethostbyname(hostname)
http = requests.get("https://api.ipify.org/").text



print(Fore.GREEN+"[+] "+Fore.GREEN+"Your Local IP : "+Fore.GREEN+ip_local)
print(Fore.RED+"[+] "+Fore.RED+"your Public IP : "+Fore.RED+http)
input()