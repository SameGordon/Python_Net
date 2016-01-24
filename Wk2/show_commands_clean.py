#!/usr/bin/env python

'''
Modules to import
'''

import telnetlib
import time
import sys
import socket

'''
End of Modules
'''


TELNET_PORT = 23
TELNET_TIMEOUT = 6

##Send commands to remote device
def send_command(remote_conn, cmd):
	cmd = cmd.rstrip()
	remote_conn.write(cmd + '\n')
	time.sleep(1)
	return remote_conn.read_very_eager()

def login(remote_conn, username, password):
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')	
    return output

def telnet_connect(ip_addr):
	try:
		return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
	except socket.timout:
		sys.exit("Connection timed-out")

def spacer():
	print '-' * 30

##Log in to device and run commands
def main ():
    ip_addr = 
    username = 
    password = 

    remote_conn = telnet_connect(ip_addr)
    output = login(remote_conn, username, password)
    
    time.sleep(1)
    output = remote_conn.read_very_eager()


    output = send_command(remote_conn, "show version | in uptime")
    print output

    spacer()

    output = send_command(remote_conn, "show int status")
    print output


    remote_conn.close()

if __name__ == "__main__":
	main()


