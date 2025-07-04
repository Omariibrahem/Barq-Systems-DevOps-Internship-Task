import pandas as pd
import ipaddress 	#built in module fffor ip and subnet handling
import pyfiglet         #for the Banner
import os

# Display a Banner
print(pyfiglet.figlet_format("Subnet Analyzer"))

# Ask user for the input Excel file name
input_file = input("Enter the Excel file name (e.g., ip_data.xlsx): ").strip() #remove white spaces

# Check if file exists in the current path / directory
if not os.path.exists(input_file):
    print(f"File '{input_file}' not found. Please make sure its in the current Directory.")
    exit(1)


print("Analyzing The Data...\n")

# Function to calculate network info
def calculate_network_info(ip, subnet):
    ip = str(ip).strip()
    subnet = str(subnet).strip() # check the format  
    try:
        network = ipaddress.IPv4Network(f"{ip}/{subnet}", strict=False) #Extract the original subnet out of the given info
        return {
            "CIDR": str(network.with_prefixlen),
            "Network": f"{network.network_address}/{network.prefixlen}",
            "Broadcast Address": str(network.broadcast_address),
            "Usable Hosts": max(network.num_addresses - 2, 0)
        }
    except Exception as e:
        return {
            "CIDR": "Invalid",
            "Network": "N/A",
            "Broadcast Address": "N/A",
            "Usable Hosts": 0
        }

# Read Excel as pandas DataFrame
df = pd.read_excel(input_file)

# Analyze each row and appent the vlaue in results row by row
results = []
for index, row in df.iterrows():
    info = calculate_network_info(row["IP Address"], row["Subnet Mask"])
    results.append({**row, **info})
    print(f" Processed {row['IP Address']}")

# Save to CSV
output_file = "network_summary.csv"
pd.DataFrame(results).to_csv(output_file, index=False)

print(f"\n Report generated: {output_file}")
print("Analysis complete!")
