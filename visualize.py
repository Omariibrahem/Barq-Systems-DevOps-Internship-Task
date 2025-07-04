import pandas as pd
import matplotlib.pyplot as plt
import pyfiglet 

# Print a  banner 
print(pyfiglet.figlet_format("Subnet Plotter"))

# Load the previously generated CSV summary
df = pd.read_csv("network_summary.csv")

# Count how many IPs belong to each unique subnet
count_per_subnet = df["Network"].value_counts().sort_index()

# Get the number of usable hosts per subnet 
usable_hosts_per_subnet = df.groupby("Network")["Usable Hosts"].first().sort_index()
# first() if a subnet appears multiple times it still has one usable host value

# first Plot  Number of IPs per Subnet

plt.figure(figsize=(10, 6))
count_per_subnet.plot(kind="bar", color="cornflowerblue")
plt.title("Number of IPs per Subnet")
plt.xlabel("Network (CIDR)")
plt.ylabel("Count of IPs")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("number_of_ips_per_subnet.png")
plt.close()  # Close the figure after saving to file


# Plot 2: Number of Usable Hosts per Subnet

plt.figure(figsize=(10, 6))
usable_hosts_per_subnet.plot(kind="bar", color="mediumseagreen")
plt.title("Number of Usable Hosts per Subnet")
plt.xlabel("Network (CIDR)")
plt.ylabel("Usable Hosts")
plt.xticks(rotation=45, ha='right') #just for better Display
plt.tight_layout()
plt.savefig("usable_hosts_per_subnet.png")
plt.close()

print(" Charts saved as: ")
print(" - number_of_ips_per_subnet.png")
print(" - usable_hosts_per_subnet.png")

