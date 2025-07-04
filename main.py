import os

print("""
===============================
   welcome to Subnet Analyzer
      We Got your Network 
===============================
1. Analyze IP Data
2. Generate Charts
3. Exit
""")

choice = input("Enter your choice: ")

if choice == "1":
    os.system("python subnet_analyzer.py") #run subnet analyzer
elif choice == "2":
    os.system("python visualize.py")       #Run the plotter
else:
    print("Looking forward to see you soon")

