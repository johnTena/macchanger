#!/usr/bin/env python3

import argparse
import subprocess
import re

def get_arguments():
    parser = argparse.ArgumentParser(description="Herramienta para cambiar la MAC en la interfaz de red")
    parser.add_argument("-i","--interface",required=True,dest="interface",help="Nombre de la interfaz de red")
    parser.add_argument("-m","--mac",required=True,dest="mac_address",help="Nueva dirección MAC para la interfaz de red")

    return parser.parse_args()

def is_valid_input(interface,mac):
    is_valid_interface = re.match(r'^[w][l|t][p|h]\d{1}[s]\d{1,2}$',interface)
    is_valid_mac = re.match(r'^([A-F-a-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$',mac)
    return is_valid_interface and is_valid_mac
def change_mac(interface,mac):
    if is_valid_input(interface,mac):
       subprocess.run(["ifconfig", interface,"down"])
       subprocess.run(["ifconfig",interface,"hw","ether",mac])
       subprocess.run(["ifconfig",interface,"up"])
       print(f"\n[+] La MAC ha sido cambiada exitosamente\n")
    else:
        print("\nLos datos introducidos no son correctos\n")
def main():
    args = get_arguments()
    change_mac(args.interface,args.mac_address)
if __name__ == '__main__':
    main()
