import sys
import random
import subprocess

# Check if the number of iterations is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python wholecode.py <num_iterations>")
    sys.exit(1)

# Get the number of iterations from the command-line argument
num_iterations = int(sys.argv[1])

# Execute gsv.py
#subprocess.run(["python", "gsv.py"])

# Loop for the specified number of iterations
for _ in range(num_iterations):
    # Generate a random number between 10 and 30
    random_number = random.randint(10, 30)

    subprocess.run(["python", "gsv.py"])
    
    # Run the Python script with the random number as argument
    subprocess.run(["python", "allthreeafter2mix2b.py", str(random_number)])
