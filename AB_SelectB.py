#!/usr/bin/python
#
# Telnet to AB Switch
# Change postion to B
# Requires python 2.7
# Revsion 29th July, 2019
# Andy Saunders

import sys
import getpass
import telnetlib

password = "dataman" # default password
HOST1 = "192.168.1.39" # default IP Address

def AB_SWITCH_SELECT_SW1_B():
    tn = telnetlib.Telnet(HOST1)
    tn.read_until("Please logon:")
    tn.write(password + "\n")
    tn.write ("set system b" + "\n")
    tn.read_until("OK")
    tn.write("quit\n")
    print (" \r")
    print ("SW1 AB Switch Changed to Port B")
    print ("\r")

AB_SWITCH_SELECT_SW1_B()
