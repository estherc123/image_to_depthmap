import matplotlib.pyplot as plt
import re

# File path - update this to the path of your file
file_path = r"C:\Users\yuche\Documents\image_to_depthmap\scripts\loss_epoch170.txt"

# Initialize a dictionary to store the losses
losses = {'G_GAN': []}

# Read and parse the data from the file
with open(file_path, 'r') as file:
    for line in file:
        if line.strip():
            # Splitting the line at parentheses and taking the second part
            loss_part = line.split(')')[1] if ')' in line else line

            # Extracting each loss value
            parts = re.findall(r'([A-Za-z_\d]+): ([\d]+[.][\d]+)', loss_part)
            print(parts)
            for key, value in parts:
                if key in losses:
                    losses[key].append(float(value))

# Plotting
plt.figure(figsize=(10, 6))
for key, values in losses.items():
    plt.plot(values, label=key)

plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.title('Training Loss Over Iterations')
plt.legend()
plt.show()
