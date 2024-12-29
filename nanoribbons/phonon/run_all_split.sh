#!/bin/bash

# Set OMP_NUM_THREADS explicitly for LAMMPS
export OMP_NUM_THREADS=4

# Function to process a range of files
process_range() {
  local start=$1
  local end=$2

  for i in $(seq -w $start $end); do
    data_file="POSCAR-${i}.data"
    dump_file="forces_POSCAR-${i}.dump"
    lammps_input="lammps_input_${i}.in"

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

      lmp_mpi -in $lammps_input > log_${i}.txt 2>&1

      if [[ -f $dump_file ]]; then
        echo "Successfully created ${dump_file}"
      else
        echo "Failed to create ${dump_file}. Check log_${i}.txt for details."
      fi

      rm $lammps_input
    else
      echo "File $data_file does not exist, skipping."
    fi
  done
}

# Process ranges
process_range 1 999
process_range 1000 1008


# chmod +x run_all_split.sh

# ./run_all_split.sh
