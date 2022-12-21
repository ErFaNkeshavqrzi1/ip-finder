
import requests
import subprocess
import socket
init()





hostname = socket.gethostname()
ip_local = socket.gethostbyname(hostname)
http = requests.get("https://api.ipify.org/").text



print("[+] "+"Your Local IP : "+ip_local)
print("[+] ""your Public IP : "+http)
input()
