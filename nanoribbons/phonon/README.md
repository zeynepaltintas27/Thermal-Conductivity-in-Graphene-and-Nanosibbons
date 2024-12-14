The phonon dispersion relation for nanoribbons, comprising four basis atoms, was calculated incrementally utilizing
LAMMPS, following a systematic approach as outlined below:
1) I created nanoribbons with 4 basis vectors with input file named in.nanoribbons I created nanoribbons.data with write_data code.
2) Since the unit cell is not slanted, I added "0 0 0 xy xz yz" line to the created data file and
saved it.
3) I converted nanoribbons.data file to POSCAR file with python. You can find the code in
"lammps_to_poscar.py" file.
4) "phonopy --lammps -d --dim="3 3 1" -c nanoribbons.data" is runned and yaml and supercell files have been created.
5) POSCAR-001 and POSCAR-002 were created with "phonopy --dim="4 1 1" -d --amplitude=0.01".
6) Since Lammps could not read POSCAR-001 and POSCAR-002 files, I converted the files to POSCAR-001.data and POSCAR-002.data files with python.
7) I created a new input file named in.nanoribbons.read so that Lammps could read the necessary data.
8) With "lmp_mpi -in in.nanoribbons.read", I obtained the forces_POSCAR-002.dump file by replacing the necessary places in the forces_POSCAR-001.dump and in.nanoribbons.read files with 002 in the first round.
10) Using the data we obtained, I plotted the phonon dispersion relation of unitcell graphene
using python.