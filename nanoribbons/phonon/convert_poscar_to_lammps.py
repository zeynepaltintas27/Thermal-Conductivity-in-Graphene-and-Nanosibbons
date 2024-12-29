from ase.io import read, write
import os

# Function to convert a POSCAR file to LAMMPS data format
def convert_poscar_to_data(input_file, output_file):
    try:
        # Read the POSCAR file
        atoms = read(input_file, format="vasp")
        # Write the LAMMPS data file
        write(output_file, atoms, format="lammps-data")
        print(f"Converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Failed to convert {input_file}: {e}")

# Loop to process multiple files
for i in range(1, 1009):  # Adjust the range if there are more than 1008 files
    poscar_file = f"POSCAR-{i:03d}"  # Format: POSCAR-001, POSCAR-002, etc.
    lammps_data_file = f"POSCAR-{i:03d}.data"
    
    # Check if the input file exists
    if os.path.exists(poscar_file):
        convert_poscar_to_data(poscar_file, lammps_data_file)
    else:
        print(f"File {poscar_file} does not exist, skipping.")
