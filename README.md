Nice — I’ll make this README friendlier, more robust, and cross-platform so anyone (Windows / macOS / Linux) can run your Subnet Analyzer with minimal fuss — and so it’s Docker-friendly for environments that don’t want to install system deps.

Below is a polished, ready-to-paste `README.md`. It includes local install instructions for all OSes, a Docker quick start (recommended for consistency), non-interactive tips (for CI), troubleshooting, file format examples, and a short CONTRIBUTING / License block.

---

```markdown
# 🛰️ Subnet Analyzer

A small CLI tool to analyze and visualize subnet and IP data from Excel (`.xlsx`) files.

- Reads an Excel file with `IP Address` + `Subnet Mask` columns  
- Calculates CIDR, network address, broadcast address, and number of usable hosts  
- Exports a CSV summary (`network_summary.csv`)  
- Generates two charts:
  - `network_plot number_of_ips_per_subnet.png`
  - `network_plot usable_hosts_per_subnet.png`  
- Interactive CLI entrypoint via `main.py`

---

## Key outputs
- `network_summary.csv` — row per input IP plus computed fields
- `network_plot number_of_ips_per_subnet.png` — bar chart: how many IPs per subnet
- `network_plot usable_hosts_per_subnet.png` — bar chart: usable hosts per subnet

---

## Project structure

```

barq-devops-subnet-task/
├── Dockerfile
├── ip\_data.xlsx                         # Example input (replace with your own)
├── main.py                              # CLI menu / entry point
├── subnet\_analyzer.py                   # Analyzer: reads Excel -> CSV
├── visualize.py                         # Reads CSV -> generates charts (PNGs)
├── network\_summary.csv                  # Example output
├── network\_plot number\_of\_ips\_per\_subnet.png
├── network\_plot usable\_hosts\_per\_subnet.png
├── requirements.txt
└── README.md

````

---

## Requirements

- Python 3.8+
- `pip` (Python package manager)
- Excel file with two columns (headers are required):  
  - `IP Address`  
  - `Subnet Mask`  

Example spreadsheet row:

| IP Address     | Subnet Mask       |
|----------------|-------------------|
| 192.168.1.24   | 255.255.255.0     |
| 10.0.0.1       | 255.255.254.0     |

> Note: The script reads the first sheet of the Excel workbook. Column names must match exactly (case-sensitive).

---

## Recommended (Easiest) — Run with Docker (cross-platform)

Docker gives you the same environment on Windows/macOS/Linux and avoids native dependencies (matplotlib system libs, openpyxl issues).

### Build the image
From the project root:
```bash
docker build -t subnet-analyzer .
````

### Run the interactive CLI (analyze or plot)

Mount your working folder so outputs persist locally:

```bash
docker run -it --rm -v "$PWD:/app" subnet-analyzer
```

* `-it` needed because the analyzer prompts for a filename.
* Enter the Excel filename when prompted (e.g., `ip_data.xlsx`).

### Run analyzer only (non-interactive)

If you want to feed the filename non-interactively:

```bash
echo "ip_data.xlsx" | docker run -i --rm -v "$PWD:/app" subnet-analyzer python subnet_analyzer.py
```

### Run plotting only (reads `network_summary.csv`)

```bash
docker run --rm -v "$PWD:/app" subnet-analyzer python visualize.py
```

Outputs will appear in your local folder because of `-v "$PWD:/app"`.

---

## Run locally (without Docker)

> If you want to run locally, create a Python virtual environment first to avoid polluting the system Python.

### 1) Create & activate virtualenv

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2) Install Python dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

`requirements.txt` should include:

```
pandas
openpyxl
matplotlib
pyfiglet
```

> **Heads up (Linux servers):** Matplotlib sometimes requires system libraries (`libfreetype`, `libpng`). If plotting fails on a headless server, either use Docker or switch matplotlib backend to `Agg` (the scripts already use saving-to-file, which works with `Agg`).

### 3) Run the CLI

```bash
python main.py
```

Follow the menu to analyze or visualize.

### Non-interactive execution (CI-friendly)

If you want to provide the filename without prompts:

```bash
echo "ip_data.xlsx" | python subnet_analyzer.py
# or
python subnet_analyzer.py < <(printf "ip_data.xlsx\n")
```

(These feed the filename into the script’s `input()` prompt.)

---

## CLI & Script usage

* `python main.py` — interactive menu (recommended)
* `python subnet_analyzer.py` — runs analyzer; script prompts for an Excel filename
* `python visualize.py` — reads `network_summary.csv` and writes the two PNG charts

Outputs are written to the current working directory:

* `network_summary.csv`
* `network_plot number_of_ips_per_subnet.png`
* `network_plot usable_hosts_per_subnet.png`

---

## Troubleshooting

* **Excel read error:** ensure file is `.xlsx` (not `.xls`) and headers are exactly `IP Address` and `Subnet Mask`.
* **Matplotlib backend errors on headless Linux:** run in Docker (recommended) or set backend manually:

  ```python
  import matplotlib
  matplotlib.use('Agg')
  ```
* **Windows line endings:** if scripts show `$'\r': command not found`, run:

  ```bash
  dos2unix script.sh
  ```
* **Permission errors:** make sure you have write permission to the folder (for CSV and PNG outputs).
* **Docker permission / file not appearing:** use absolute path for mounting, e.g., `-v /home/user/project:/app`.

---

## Example workflow

1. Place `ip_data.xlsx` in project folder.
2. Build and run Docker (recommended):

   ```bash
   docker build -t subnet-analyzer .
   docker run -it --rm -v "$PWD:/app" subnet-analyzer
   ```
3. Choose “Analyze” in the menu and enter `ip_data.xlsx`.
4. Choose “Plot” in the menu (or run `python visualize.py`) to create PNG charts.

---

## Developer notes

* The analyzer uses Python’s `ipaddress` module for accurate IPv4 calculations (network, broadcast, host counts).
* The visualizer aggregates the `Network` field from the produced CSV to compute:

  * `count_per_subnet` — number of input IPs in each subnet
  * `usable_hosts_per_subnet` — usable host capacity per subnet
* Charts are saved as PNG files; no GUI required.

---
## License & Contact

This project is provided for demonstration and learning purposes.
Author: **Omar Ibrahem** — [omaribrahem24@gmail.com](mailto:omaribrahem24@gmail.com)

---

