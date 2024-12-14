from ase.io import read, write

# Read the LAMMPS data file
atoms = read("nanoribbons.data", format="lammps-data")

# Write to POSCAR format
write("POSCAR", atoms, format="vasp")
