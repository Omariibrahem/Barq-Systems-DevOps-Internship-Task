FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements & dependencies to run the container and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#run the main script which will in Turn Run the analyzer or the plotter
COPY main.py .
CMD ["python", "main.py"]


