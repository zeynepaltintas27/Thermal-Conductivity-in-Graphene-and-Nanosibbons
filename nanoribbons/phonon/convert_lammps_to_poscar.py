from ase.io import read, write

# Read LAMMPS data file
structure = read("nanoribbons.data", format="lammps-data")

# Write to POSCAR (VASP format)
write("POSCAR", structure, format="vasp")
