import matplotlib.pyplot as plt
import re

# File path - update this to the path of your file
file_path = r"C:\Users\yuche\Downloads\loss_log_3.txt"

# Initialize a dictionary to store the losses and a list for iteration numbers
losses = {'G_L1': []}
iterations = []

# Read and parse the data from the file
with open(file_path, 'r') as file:
    for line in file:
        if line.strip():
            # Extracting iteration number
            match = re.search(r'iters: (\d+)', line)
            if match:
                iterations.append(int(match.group(1)))

            # Splitting the line at parentheses and taking the second part
            loss_part = line.split(')')[1] if ')' in line else line

            # Extracting each loss value
            parts = re.findall(r'([A-Za-z_\d]+): ([\d]+[.][\d]+)', loss_part)
            for key, value in parts:
                if key in losses:
                    losses[key].append(float(value))

# Plotting
plt.figure(figsize=(10, 6))
for key, values in losses.items():
    plt.plot(iterations, values, label=key)

plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.title('Eval Loss Over Iterations')
plt.legend()
plt.show()
