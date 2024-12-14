import os

# List of supercell files
supercells = ["POSCAR-001", "POSCAR-002"]

# Loop through each supercell and run LAMMPS
for supercell in supercells:
    # Modify this command to match your LAMMPS executable and input file
    command = f"lmp_mpi -in in.graphene.phonopy -var DATA_FILE {supercell}"
    os.system(command)
