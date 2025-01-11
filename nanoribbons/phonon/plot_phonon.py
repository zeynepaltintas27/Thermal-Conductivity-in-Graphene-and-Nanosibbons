import yaml
import numpy as np
import matplotlib.pyplot as plt

# Load band.yaml file
with open("band.yaml", "r") as f:
    band_data = yaml.safe_load(f)

# Extract q-points and phonon frequencies
q_points = []  # Reciprocal space points
frequencies = []  # Phonon frequencies

for segment in band_data["phonon"]:
    q_points.append(segment["distance"])  # Distance along the q-path
    frequencies.append([mode["frequency"] for mode in segment["band"]])

# Convert frequencies to a NumPy array for easier manipulation
frequencies = np.array(frequencies).T  # Transpose to get branches

# Plot the phonon dispersion
plt.figure(figsize=(10, 6))
for i, branch in enumerate(frequencies):
    plt.plot(q_points, branch, 'b-', label=f"Mode {i+1}" if i < 10 else None)  # Limit labels for clarity

plt.xlabel("Wave Vector")
plt.ylabel("Frequency (THz)")
plt.title("Phonon Dispersion Relation")
plt.grid()
plt.savefig("phonon_dispersion.png")
plt.show()
