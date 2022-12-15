#!/bin/python3
#

"""
Part B

Create a Python file, named IP_address.py, that:

    Input: Prompt the user to enter an IPv4 address. An IPv4 address is made up of four octets, each separated by a dot.
       Examples: 192.168.1.1, 10.0.0.1, 148.34.51.200, 1.2.3.4
    Using the user-supplied information, determine:
        The address's class: A, B, C, D, or E
                (capital letters must be used)
        If any address begins with 0 or if any octet has a value greater than 255, then it is invalid
                (this word must be used)
        If the address begins with 127, the address is a loopback
                (this word must be used)
        If the address is public or a private
                (these words must be used)
    Output the IPv4 address's class and whether it is a public, private, loopback, or invalid.

IPv4 address ranges, classes, and private ranges (if an address is not private, it is public).
        x is any number from 0 to 255:

Class A:   1.x.x.x through 127.x.x.x (private range: 10.x.x.x, 127.x.x.x is loopback)
Class B: 128.x.x.x through 191.x.x.x (private range: 172.16.x.x through 172.31.x.x)
Class C: 192.x.x.x through 223.x.x.x (private range: 192.168.x.x)
Class D: 224.x.x.x through 239.x.x.x (known as multicast)
Class E: 240.x.x.x through 255.x.x.x (known as experimental)

"""

# Beginning of the code for the Part B of the assignment.

"""

 Input: Prompt the user to enter an IPv4 address. An IPv4 address is made up of four octets, each separated by a dot. 
       Examples: 192.168.1.1, 10.0.0.1, 148.34.51.200, 1.2.3.4
       
"""

address = input('\nEnter an ip address using this format, xxx.xxx.xxx.xxx : ')

address_split = address.split(".")

# Determine the Class and type of address.

""" 
Using the user-supplied information, determine:
        The address's class: A, B, C, D, or E
                (capital letters must be used)
        If the address begins with 127, the address is a loopback
                (this word must be used)
        If the address is public or a private
                (these words must be used)
    Output the IPv4 address's class and whether it is a public, private, loopback, or invalid.
"""

if 1 <= int(address_split[0]) <= 127:
    class_t = "A"
    class_p = "private" if int(address_split[0]) == 10 else "loopback" if int(address_split[0]) == 127 else "public"
elif int(address_split[0]) <= 191:
    class_t = "B"
    class_p = "private" if int(address_split[0]) == 172 and (16 <= int(address_split[1]) <= 31) else "public"
elif int(address_split[0]) <= 223:
    class_t = "C"
    class_p = "private" if (int(address_split[0]) == 192 and int(address_split[1]) == 168) else "public"
elif int(address_split[0]) <= 239:
    class_t = "D"
    class_p = "multicast"
else:
    class_t = "E"
    class_p = "experimental"


# Display the 4 Octets during testing, will be commented out when completed.

# print(f'\nFirst Octet is: {int(address_split[0])}')
# print(f'\n\tSecond Octet is: {int(address_split[1])}')
# print(f'\n\t\tThird Octet is: {int(address_split[2])}')
# print(f'\n\t\t\tForth Octet is: {int(address_split[3])}')

#  Output the IPv4 address's class and whether it is a public, private, loopback, or invalid.

# Validate the data being entered.

""" 
If any address begins with 0 or if any octet has a value greater than 255, then it is invalid
                (this word must be used)
"""

for i in range(0, 4):
    if int(address_split[i]) > 255 or int(address_split[i]) == 0:
        class_p = "invalid"

if class_p == "invalid":
    print(f'\nThe IP address entered {address}, was {class_p}')
else:
    print(f'\nThe ip address you entered {address}, is a Class {class_t} {class_p} address.')

# End of file
