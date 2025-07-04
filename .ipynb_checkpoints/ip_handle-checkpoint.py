import pandas as pd
import ipaddress
import matplotlib.pyplot as plt

# Step 1: Read Excel file
df = pd.read_excel("ip_data.xlsx")

# Function to convert IP and Subnet Mask into network info
def calculate_network_info(ip, subnet):
    network = ipaddress.IPv4Network(f"{ip}/{subnet}", strict=False)
    return {
        "CIDR": str(network.with_prefixlen),
        "Network Address": str(network.network_address),
        "Broadcast Address": str(network.broadcast_address),
        "Usable Hosts": network.num_addresses - 2
    }

# Step 2: Perform Calculations
results = []
for index, row in df.iterrows():
    info = calculate_network_info(row['IP Address'], row['Subnet Mask'])
    results.append({**row, **info})

result_df = pd.DataFrame(results)

# Step 3: Group by CIDR
grouped = result_df.groupby("CIDR").size().reset_index(name="Number of IPs")

# Step 4: Export Report
result_df.to_csv("network_summary.csv", index=False)

# Step 5: Visualize
plt.figure(figsize=(10,6))
plt.bar(grouped["CIDR"], grouped["Number of IPs"])
plt.title("Number of IPs per Subnet")
plt.xlabel("CIDR")
plt.ylabel("Number of IPs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("subnet_bar_chart.png")
plt.show()
