import shodan
import sys

# Get the Shodan API key from the command line argument
if len(sys.argv) > 1:
    api_key = sys.argv[1]
else:
    print("Error: No API key provided.")
    sys.exit()

# Get the path to the input file from the command line argument
if len(sys.argv) > 2:
    input_file = sys.argv[2]
else:
    print("Error: No input file provided.")
    sys.exit()

# Initialize the Shodan API client
api = shodan.Shodan(api_key)

# Open the input file for reading
with open(input_file, "r") as f:
    # Iterate over each line (i.e., IP address or domain name) in the file
    for target in f:
        # Remove any whitespace from the target
        target = target.strip()
        
        # Perform the Shodan search for the target
        try:
            results = api.host(target)
        except shodan.exception.APIError as e:
            print(f"Error searching for {target}: {e}")
            continue
        
        # Print the results to the console
        print(f"Results for {target}:")
        print(f"  IP Address: {results['ip_str']}")
        print(f"  Organization: {results.get('org', 'N/A')}")
        print(f"  Operating System: {results.get('os', 'N/A')}")
        print(f"  Open Ports: {', '.join(map(str, results.get('ports', 'N/A')))}")
        print(f"  Vulnerabilities: {', '.join(map(str, results.get('vulns', 'N/A')))}")
        print(f"  Last Update: {results.get('last_update', 'N/A')}")
        print(f"  Hostnames: {', '.join(map(str, results.get('hostnames', 'N/A')))}\n")
