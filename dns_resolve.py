import socket
import sys

# Get the path to the input file from the command line argument (if provided)
if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = "/path/to/default/input/file.txt"

# Open the input file for reading
with open(input_file, "r") as f:
    # Iterate over each line (i.e., domain name) in the file
    for domain in f:
        # Remove any whitespace from the domain name
        domain = domain.strip()
        
        # Perform a DNS lookup on the A record for the domain
        try:
            ip_addresses = socket.gethostbyname_ex(domain)[2]
        except socket.gaierror as e:
            print(f"Error resolving {domain}: {e}")
            continue
        
        # Print the IP address(es) associated with the domain
        print(f"IP addresses for {domain}: {', '.join(ip_addresses)}")
