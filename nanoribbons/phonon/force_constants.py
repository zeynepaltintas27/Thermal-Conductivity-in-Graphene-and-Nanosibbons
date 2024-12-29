import glob

output_file = "FORCE_SETS"
dump_files = sorted(glob.glob("forces_POSCAR-*.dump"))

displacements = []
forces = []

# Loop through all dump files
for dump_file in dump_files:
    with open(dump_file, "r") as f:
        lines = f.readlines()

    displacement = []  # Store displacement vector
    force_vectors = []  # Store forces for all atoms

    for line in lines:
        data = line.strip().split()
        # Skip lines with metadata like "ITEM:" or non-numeric headers
        if data[0] == "ITEM:" or data[0].isalpha():
            continue

        # Expected format: id type x y z fx fy fz
        if len(data) == 8:
            displacement = list(map(float, data[2:5]))
            force_vectors.append(list(map(float, data[5:8])))

    displacements.append(displacement)
    forces.append(force_vectors)

# Write to FORCE_SETS
with open(output_file, "w") as f_out:
    f_out.write(f"{len(displacements)}\n")  # Number of displacements
    f_out.write(f"{len(forces[0])}\n")      # Number of atoms

    for i, (disp, f_vecs) in enumerate(zip(displacements, forces)):
        f_out.write(f"{i + 1}\n")  # Displacement index
        f_out.write(f"{disp[0]} {disp[1]} {disp[2]}\n")  # Displacement vector
        for f_vec in f_vecs:
            f_out.write(f"{f_vec[0]} {f_vec[1]} {f_vec[2]}\n")  # Forces
