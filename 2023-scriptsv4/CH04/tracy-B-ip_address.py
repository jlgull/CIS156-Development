# This program will take an IPv4 address and tell the user what class
# the address is, whether is is public or private. Certain other cases
# must also be handled: If the first octet is 0, the address is invalid,
# if it is 128, it is a loopback address.
#
# Let the student know about the split() function.

print('\nThis program will accept an IPv4 address and tell you:')
print("- it's class (A, B, C, D, E)")
print('- if it is public or private')
print('- if it is invalid')
print('- if it a loopback')

print('\nPlease input a valid IPv4 address in the form of x.x.x.x,')
print('where each x is a number from 0 to 255. For example 192.168.1.1')
ipv4_address = input('address: ')

# First, split the address into 4 octets, which results in a list of strings
# The, convert the list of strings to a list of integers
octet_list = ipv4_address.split('.')
octet_list = [eval(i) for i in octet_list]

# IPv4 classes and (private):
# A:   0 - 127 (10.x.x.x)
# B: 128 - 191 (172.16.x.x -> 172.31.x.x)
# C: 192 - 223 (192.168.x.x)
# D: 224 - 239 "multicast"
# E: 240 - 255 "experimental"

print(f'\nThe address, {ipv4_address}, as been split into a list: {octet_list}')

if octet_list[0] >= 256 or octet_list[1] >= 256 or octet_list[2] >= 256 or octet_list[3] >= 256:
    print('\nNo octect can have a number greater than 255!')
else:
    ipv4_scope = 'public address.'

    if octet_list[0] <= 127:
        ipv4_class = 'A'
        if octet_list[0] == 0:
            ipv4_class = ipv4_class + ' (although no address can start with 0, so this is invalid).'
            ipv4_scope = ''
        elif octet_list[0] == 127:
            ipv4_class = ipv4_class + ' (loopback).'
            ipv4_scope = ''
        elif octet_list[0] == 10:
            ipv4_scope = 'private address.'

    elif octet_list[0] <= 191:
        ipv4_class = 'B'
        if octet_list[0] == 172 and (octet_list[1] >= 16 and octet_list[1] <= 31):
            ipv4_scope = 'private address.'

    elif octet_list[0] <= 223:
        ipv4_class = 'C'
        if octet_list[0] == 192 and octet_list[1] == 168:
            ipv4_scope = 'private address.'

    elif octet_list[0] <= 230:
        ipv4_class = 'D'
        ipv4_scope = '(multicast)'
    
    else:
        ipv4_class = 'E'
        ipv4_scope = '(experimental)'

    print(f'\n{ipv4_address} is a class {ipv4_class} {ipv4_scope}')

