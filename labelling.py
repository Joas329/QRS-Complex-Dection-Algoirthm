import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Load the dataset with comma as delimiter
df = pd.read_csv("lab5_Philco-L05.txt", delimiter=",")


time = df.iloc[:, 0]

# Get the Channel data
data = df.iloc[:, 1]

time_subset = time[:10000]

df_subset = data[:10000]


p_indices = [110, 910, 1670, 2490, 3300, 4085]
q_indices = [219, 1018, 1785, 2605, 3400, 4160]
r_indices = [257, 1052, 1825, 2641, 3450, 4238]
s_indices = [284, 1079, 1851, 2663, 3474, 4265]
t_indices = [460, 1250, 2020, 2840, 3650, 4436]

# Plot the ECG signal
plt.figure(figsize=(10, 6))
plt.plot(time_subset, df_subset, label='ECG Data')
plt.xlabel('Time')
plt.ylabel('Data')
plt.title('ECG Data from Joaquin Philco')
plt.grid(True)


# Marking P Features
plt.scatter(time_subset[p_indices], df_subset[p_indices], color='black', marker='x', label='P')

# Marking Q Features
plt.scatter(time_subset[q_indices], df_subset[q_indices], color='purple', marker='x', label='Q')

# Marking R Features
plt.scatter(time_subset[r_indices], df_subset[r_indices], color='green', marker='x', label='R')

# Marking S Features
plt.scatter(time_subset[s_indices], df_subset[s_indices], color='red', marker='x', label='S')

# Marking T Features
plt.scatter(time_subset[t_indices], df_subset[t_indices], color='black', marker='x', label='T')

plt.xlabel('Time')
plt.ylabel('Data')
plt.title('ECG Data with QRS Features')
plt.legend()
plt.grid(True)
plt.show()