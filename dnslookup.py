"""

DNS Enumeration project. Right now we just do the basic one IP and one
hostname lookup. In the future I am looking to add more options such as
MX Record lookup and thd like. 

"""
#Basic imports
import sys
import socket
import argparse

#Setting up parsers for arguments
parser = argparse.ArgumentParser("Looking for command line arguments of domain names")
parser.add_argument('-d', default='None', type=str, help='Domain name you are looking up')
parser.add_argument('-a', default='None', help='Ip address you are looking up')

args = parser.parse_args()
a = args.a
d = args.d

"""
namelookup() function. This will be the main workhorse of the applciation for now. 
"""
def nameLookup():
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
    return

"""
Calling the function
"""
nameLookup()
