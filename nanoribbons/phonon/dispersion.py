import numpy as np
import matplotlib.pyplot as plt

# Load band data from Phonopy
data = np.loadtxt("band.conf")

# Extract x-coordinates and phonon frequencies
x = data[:, 0]  # Reciprocal space
frequencies = data[:, 1:]  # Phonon frequencies

# Plot the phonon dispersion
for i in range(frequencies.shape[1]):
    plt.plot(x, frequencies[:, i], 'b*',label=f"Mode {i+1}")
plt.xlabel("Wave Vector")
plt.ylabel("Frequency (THz)")
plt.title("Phonon Dispersion Relation")
plt.grid()
plt.show()
plt.savefig("phonon_dispersion.png")