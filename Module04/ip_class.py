#!/bin/python3
#
address = input("Enter an ip address, xxx.xxx.xxx.xxx, ")

address_split = (address.split(".")

if 1 <= int(address_split[0]) <= 127:
    class_t = "A"
    class_p = "Public" if int(address_split[0]) != 10 else "Private"


print(address, "\n")

print(int(address_split[0]), "\n")

print(f'The ip address you entered, {address}, is a Class {class_t} {class_p} address.')


'''ip_oct = [0]*5

print(ip_oct, "\n")

for x in range(4):
    print(x+1, x, address_split[x])
    ip_oct[x] = address_split[x-1]
    print(f'{ip_oct[x]} \n')'''

'''
Class A Public & Private IP Address Range
Class A addresses are for networks with large number of total hosts. 
Class A allows for 126 networks by using the first octet for the network ID. 
The first bit in this octet, is always zero. 
The remaining seven bits in this octet complete the network ID. 
The 24 bits in the remaining three octets represent the hosts ID and allows for approximately 
    17 million hosts per network. Class A network number values begin at 1 and end at 127.
Public IP Range: 1.0.0.0 to 127.0.0.0
First octet value range from 1 to 127
Private IP Range: 10.0.0.0 to 10.255.255.255 (See Private IP Addresses below for more information)
Subnet Mask: 255.0.0.0 (8 bits)
Number of Networks: 126
Number of Hosts per Network: 16,777,214

Class B Public & Private IP Address Range
Class B addresses are for medium to large sized networks. 
Class B allows for 16,384 networks by using the first two octets for the network ID. 
The first two bits in the first octet are always 1 0. 
The remaining six bits, together with the second octet, complete the network ID. 
The 16 bits in the third and fourth octet represent host ID and allows for approximately 65,000 hosts per network.
Class B network number values begin at 128 and end at 191.
Public IP Range: 128.0.0.0 to 191.255.0.0
First octet value range from 128 to 191
Private IP Range: 172.16.0.0 to 172.31.255.255 (See Private IP Addresses below for more information)
Subnet Mask: 255.255.0.0 (16 bits)
Number of Networks: 16,382
Number of Hosts per Network: 65,534

Class C Public & Private IP Address Range
Class C addresses are used in small local area networks (LANs). 
Class C allows for approximately 2 million networks by using the first three octets for the network ID. 
In a class C IP address, the first three bits of the first octet are always 1 1 0. 
And the remaining 21 bits of first three octets complete the network ID. 
The last octet (8 bits) represent the host ID and allows for 254 hosts per network. 
Class C network number values begins at 192 and end at 223.
Public IP Range: 192.0.0.0 to 223.255.255.0
First octet value range from 192 to 223
Private IP Range: 192.168.0.0 to 192.168.255.255 (See Private IP Addresses below for more information)
Special IP Range: 127.0.0.1 to 127.255.255.255 (See Special IP Addresses below for more information)
Subnet Mask: 255.255.255.0 (24 bits)
Number of Networks: 2,097,150
Number of Hosts per Network: 254

Class D IP Address Range
Class D IP addresses are not allocated to hosts and are used for multicasting.
Multicasting allows a single host to send a single stream of data to thousands of hosts across
 the Internet at the same time. It is often used for audio and video streaming,
 such as IP-based cable TV networks. Another example is the delivery of real-time stock market data
 from one source to many brokerage companies.
Range: 224.0.0.0 to 239.255.255.255
First octet value range from 224 to 239
Number of Networks: N/A
Number of Hosts per Network: Multicasting

Class E IP Address Class
Class E IP addresses are not allocated to hosts and are not available for general use. 
These are reserved for research purposes.
Range: 240.0.0.0 to 255.255.255.255
First octet value range from 240 to 255
Number of Networks: N/A
Number of Hosts per Network: Research/Reserved/Experimental

Private IP Addresses
Within each network class, there are designated IP address that is reserved specifically for 
private/internal use only. This IP address cannot be used on Internet-facing devices as that are 
non-routable. For example, web servers and FTP servers must use non-private IP addresses. 
However, within your own home or business network, private IP addresses are assigned to your 
devices (such as workstations, printers, and file servers).

Class A Private Range: 10.0.0.0 to 10.255.255.255

Class B Private APIPA Range: 169.254.0.0 to 169.254.255.255
Automatic Private IP Addressing (APIPA) is a feature with Microsoft Windows-based computers 
to automatically assign itself an IP address within this range if a 
Dynamic Host Configuration Protocol (DHCP) server is not available on the network. 
A DHCP server is a network device that is responsible for assigning IP addresses to devices on the network.

At your home, your Internet modem or router likely provides this functionality. In your work place, 
a Microsoft Windows Server, a network firewall, or some other specialized network device likely provides 
this functionality for the computer at your work environment.

Class B Private Range: 172.16.0.0 to 172.31.255.255

Class C Private Range: 192.168.0.0 to 192.168.255.255
Special IP Addresses

IP Range: 127.0.0.1 to 127.255.255.255 are network testing addresses (also referred to as loop-back addresses). 
These are virtual IP address, in that they cannot be assigned to a device. 
Specifically, the IP 127.0.0.1 is often used to troubleshoot network connectivity issues using the ping command. 
Specifically, it tests a computer's TCP/IP network software driver to ensure it is working properly.

'''
