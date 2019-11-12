import sys
import socket
import argparse

parser = argparse.ArgumentParser("Looking for command line arguments of domain names")
parser.add_argument('-d', default='None', type=str, help='Domain name you are looking up')
parser.add_argument('-a', default='None', help='Ip address you are looking up')

args = parser.parse_args()
a = args.a
d = args.d



if d == 'None' and a == 'None':
    print("Please enter a name or address to look up")
elif d != 'None' and a == 'None':
    addr2 = socket.gethostbyname(d)
    print 'The IP Address for', d, 'is', addr2
elif a != 'None' and d == 'None':
    addr2 = socket.gethostbyaddr(a)
    print 'The hosename for', a, 'is', addr2[0]
else:
    print("You can only pick a name or address not both.")