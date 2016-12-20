# program: Birch
# Description: Simple port scanner
# Author: Shawn Rose
#########################################
#!/user/bin/env python3
import socket
import subprocess
import sys

from datetime import datetime

# clear the screen
subprocess.run("clear")

# Ask for imput
remote_server = input("Enter a remote host to scan: ")

try:
	remote_server_IP = socket.gethostbyname(remote_server)
except socket.gaierror:
	print("Unable to resolve host")
	quit()

#Printer banner with info on which host will be scanned
print("-" * 60)
print("Please wait, scanning remote host \x1b[1;33;40m{}\x1b[0m".format(remote_server_IP))
print("-" * 60)

#check what time scan starts
t1 = datetime.now()

# Dictonary of well known ports
known_ports = {
	1: "TCPMUX",
	5: "Remote job entry",
	7: "Echo",
	9: "Discard",
	11: "Systat",
	13: "Daytime",
	15: "Formerly netstat",
	17: "QOTD",
	18: "Message Send",
	19: "CHARGEN",
	20: "FTP",
	21: "FTP",
	22: "SSH",
	23: "Telnet",
	25: "SMTP",
	37: "Time",
	38: "RAP",
	39: "RLP",
	42: "Host Name Server",
	43: "WHOIS",
	49: "TACACS+",
	51: "IMP",
	52: "XNS",
	53: "DNS",
	54: "XNS",
	56: "XNS",
	57: "Private Terminal",
	58: "XNS",
	67: "BOOTP",
	80: "http",
	81: "TorPark",
	82: "TorPark",
	88: "Kerberos",
	90: "DNSIX",
}

# Using the range function to specify ports

# Error handling for catching errors

try:
	for port in range(1, 1024):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remote_server_IP, port))
		if result == 0:
			try:
				print("Port {} \x1b[1;34;40m({})\x1b[0m:\x1b[1;32;40mOpen\x1b[0m".format(port, known_ports[port]))

			except KeyError:
				print("Port {}: Open".format(port))
		sock.close()

except KeyboardInterrupt:
	print(" ---You pressed Ctrl+C---")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved. Exiting")
	sys.exit()

except socket.error:
	print("Could not connect to server")
	sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the elapsed time to run script
total = t2 - t1

# Printing the information to screen
print("")
print("Scanning completed in: \x1b[0;31;40m{}\x1b[0m".format(total))
print ("")