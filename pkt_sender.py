from scapy.all import *
import time

# MAC, IP source addresses and MAC, IP destination addresses for VMs
src_mac = "ff:ff:ff:ff:ff:ff"
dst_mac = "ff:ff:ff:ff:ff:ff"
src_ip = "192.168.56.1"
target_ip = "192.168.56.2"
iface = "eth1\0"

# Packets to be send
arp_packet = Ether(src=src_mac, dst=dst_mac)/ARP(op=1, psrc=src_ip, pdst=target_ip, hwdst=dst_mac)
icmp_packet = Ether(src=src_mac, dst=dst_mac)/IP(src=src_ip, dst=target_ip)/ICMP()
ip_packet = Ether(src=src_mac, dst=dst_mac)/IP(src=src_ip, dst=target_ip)/"Custom Payload"
tcp_packet = Ether(src=src_mac, dst=dst_mac)/IP(src=src_ip, dst=target_ip)/TCP(dport=80, flags="S")
udp_packet = Ether(src=src_mac, dst=dst_mac)/IP(src=src_ip, dst=target_ip)/UDP(dport=53)/"DNS Query Simulation"

def send_packet():
    
    try:
        while True:
        
            sendp(icmp_packet, iface=iface)
            print(f"icmp_packet sent to {target_ip}")
            #time.sleep(0.3)
            sendp(ip_packet, iface=iface)
            print(f"ip_packet sent to {target_ip}")
            #time.sleep(0.3)
            sendp(tcp_packet, iface=iface)
            print(f"tcp_packet sent to {target_ip}")
            #time.sleep(0.3)
            sendp(udp_packet, iface=iface)
            print(f"udp_packet sent to {target_ip}")
            #time.sleep(0.3)
            sendp(arp_packet, iface=iface)
            print(f"arp_packet sent to {target_ip}")
            #time.sleep(0.3)
    
    except KeyboardInterrupt:
        print("\nExiting...\n")   

if __name__ == "__main__":
    send_packet()