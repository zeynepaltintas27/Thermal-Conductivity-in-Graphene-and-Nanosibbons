from ase.io import read, write

# Read the POSCAR file
poscar_file = "POSCAR-001"  # Change to POSCAR-002 for the next file
atoms = read(poscar_file, format="vasp")

# Write the LAMMPS data file
lammps_data_file = "POSCAR-001.data"  # Output file name
write(lammps_data_file, atoms, format="lammps-data")
print(f"Converted {poscar_file} to {lammps_data_file}")

# Don't forget do it for POSCAR-001 and POSCAR-002 seperately.



