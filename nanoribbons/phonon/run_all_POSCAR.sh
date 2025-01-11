#!/bin/bash

# Explicitly set OMP_NUM_THREADS for LAMMPS
export OMP_NUM_THREADS=4

# Loop through all zero-padded filenames
for i in $(seq 1 50); do
  data_file=$(printf "POSCAR-%03d.data" $i)  # Zero-padded file name
  dump_file=$(printf "forces_POSCAR-%03d.dump" $i)
  lammps_input=$(printf "lammps_input_%03d.in" $i)

  if [[ -f $data_file ]]; then
    echo "Processing $data_file..."
    cat > $lammps_input <<EOF
# ---------- Initialize Simulation ---------------------
units metal                  
dimension 3                  
boundary p p p               
atom_style atomic            

# ---------- Read the Supercell Data ---------------------
read_data ${data_file}    

# ---------- Define Interatomic Potential ---------------------
pair_style tersoff           
pair_coeff * * BNC.tersoff C 

# ---------- Set Atomic Mass ---------------------
mass 1 12.011  # Atomic mass of carbon for type 1

# ---------- Compute Forces ---------------------
compute myforces all property/atom fx fy fz  
dump 1 all custom 1 ${dump_file} id type x y z fx fy fz  

# ---------- Run the Simulation ---------------------
run 0                         
EOF

    # Run LAMMPS
    lmp_mpi -in $lammps_input > log_${i}.txt 2>&1

    # Check if dump file was created
    if [[ -f $dump_file ]]; then
      echo "Successfully created ${dump_file}"
    else
      echo "Error: Failed to create ${dump_file}" >> error_log.txt
      echo "Check log_${i}.txt for details."
    fi

    # Clean up
    rm $lammps_input
  else
    echo "File $data_file does not exist, skipping."
  fi
done
