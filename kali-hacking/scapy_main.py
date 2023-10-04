from scapy.all import ICMP
from scapy.all import IP
from scapy.all import sr

src_ip = "192.168.0.154"
dest_ip = "www.google.com"

ip_layer = IP(src = src_ip, dst = dest_ip)

print(ip_layer.show())
