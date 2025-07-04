```markdown
# 🛰️ Subnet Analyzer

A CLI-based tool to analyze and visualize subnet and IP data from Excel files.

---

##  Features

- Interactive CLI with terminal menu
- Reads IPs and subnet masks from Excel `.xlsx` and you will need to Enter the Excel Data FileName
- Calculates:
  - CIDR notation
  - Network address
  - Broadcast address
  - Number of usable hosts
- Exports results to CSV
- Generates:
  - 📊 Bar chart of number of IPs per subnet
  - 📊 Bar chart of usable hosts per subnet
- you wil choose to either analyze the given data or generate the charts

---

## Project Structure

```

barq-devops-subnet-task/
├── Dockerfile                            # Docker build file
├── ip_data.xlsx                          # Sample input 
├── main.py                               #  options menu 
├── subnet_analyzer.py                    # Subnet analysis logic
├── visualize.py                          # Visualization logic
├── network_summary.csv                   # Output CSV 
├── network_plot number_of_ips_per_subnet.png   # Chart: IPs per subnet
├── network_plot usable_hosts_per_subnet.png    # Chart: Usable hosts per subnet
├── requirements.txt                      # Python dependencies
└── README.md                             # Guide

````

---

##  Requirements

- Python 3.8+
- pip
- Excel file with two columns:
  - `IP Address`
  - `Subnet Mask`

Example:

| IP Address     | Subnet Mask       |
|----------------|-------------------|
| 192.168.1.24   | 255.255.255.0     |
| 10.0.0.1       | 255.255.254.0     |

---

## 🧪 Run Locally

### 1. Install Dependencies

```bash
pip install -r requirements.txt
````

### 2.Run the CLI

```bash
python3 main.py
```

Follow the terminal prompts to:

* Analyze an Excel file
* Generate visual reports
* Exit the program

---

## 🐳 Run with Docker

### 1. Build the Image

```bash
docker build -t subnet-analyzer .
```

### 2. Run the CLI in Container

```bash
docker run -it -v "$PWD:/app" subnet-analyzer
```

This runs the interactive CLI (`main.py`) inside Docker.

* Make sure your input Excel file (e.g., `ip_data.xlsx`) is in the current directory
* Outputs (CSV and plots) will appear in the same folder

---

## Output Files

* `network_summary.csv`: Analysis report
* `network_plot number_of_ips_per_subnet.png`: IP count chart
* `network_plot usable_hosts_per_subnet.png`: Usable hosts chart

---

## Author

**Omar Ibrahem**
DevOps & Cloud Enthusiast
📧 [omaribrahem24@gmail.com]

```

