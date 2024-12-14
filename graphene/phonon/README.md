I initially constructed a unit cell for graphene to facilitate the calculations.
The structure was subsequently verified using OVITO for accuracy. The phonon dispersion
relation for graphene, comprising four basis atoms, was calculated incrementally utilizing
LAMMPS, following a systematic approach as outlined below:
1) I created graphene with 4 basis unit cell with input file named in.graphene.phonopy. I
created graphene.data with write_data code.
2) Since the unit cell is not slanted, I added "0 0 0 xy xz yz" line to the created data file and
saved it.
3) I converted graphene.data file to POSCAR file with python. You can find the code in "lammps_to_poscar.py" file.
4) "phonopy --lammps -d --dim="2 4 1" -c graphene.data" is runned and yaml and supercell files have been created.
5) POSCAR-001 and POSCAR-002 were created with "phonopy --dim="4 2 1" -d --
amplitude=0.01".
6) Since Lammps could not read POSCAR-001 and POSCAR-002 files, I converted the files
to POSCAR-001.data and POSCAR-002.data files with python.
7) I created a new input file named in.graphene.read so that Lammps could read the
necessary data.
8) With "lmp_mpi -in in.graphene.read", I obtained the forces_POSCAR-002.dump file by
replacing the necessary places in the forces_POSCAR-001.dump and in.graphene.read files
with 002 in the first round.
9) The band.cof file was created and with the code "phonopy --lammps -f forces_POSCAR-*.dump", FORCE_SETS and phonopy.yaml and band.yaml files were created.
10) Using the data we obtained, I plotted the phonon dispersion relation of unitcell graphene
using python.