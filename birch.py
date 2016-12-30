# program: Birch
# Description: Simple port scanner
# Author: Shawn Rose
#########################################
#!/user/bin/env python3
import argparse
import socket
import subprocess
import sys
from port_data import known_ports

from datetime import datetime

# create argument parser and parse arguements
parser = argparse.ArgumentParser(description='Port scan remote host')
parser.add_argument('host', metavar='H', type=str, help='Remote host name or IP address')
args = vars(parser.parse_args())

# clear the screen
subprocess.run("clear")

# use parsed arguments
remote_server = args.get('host')
print(remote_server)

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

# Using the range function to specify ports
# Error handling for catching errors

try:
	for port in range(1, 65536):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remote_server_IP, port))
		if result == 0:
			try:
				print("Port {} \x1b[1;34;40m({})\x1b[0m:		\x1b[1;32;40mOpen\x1b[0m".format(port, known_ports[port]))

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