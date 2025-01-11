To visualize the phonon dispersion relation, all necessary files must be prepared. The results can be obtained directly by executing `dispersion.py`. Alternatively, the files can be generated manually by following the procedure described below.

The phonon dispersion relation for nanoribbons, comprising four basis atoms, was calculated incrementally utilizing
LAMMPS, following a systematic approach as outlined below:

1) I created nanoribbons with 4 basis vectors with input file named in.nanoribbons, I created nanoribbons.data with write_data code (lmp_serial < in.nanoribbons). +
2) Since the unit cell is not slanted, I added "0 0 0 xy xz yz" line to the created data file and
saved it. +
3) I converted nanoribbons.data file to POSCAR file with python. You can find the code in
"convert_lammps_to_poscar.py" file. +
------- "phonopy --lammps -d --dim="1 5 1" -c nanoribbons.data" is runned. "phonopy_disp.yaml" and supercells have been created.
4) POSCAR-001-POSCAR-050 and phonopy_disp.yaml were created with "phonopy --dim="1 5 1" -d --amplitude=0.01". +
5) Since Lammps could not read POSCAR-### files, I converted the all files to POSCAR-###.data files with python (convert_poscar_to_lammps.py). +
6) I created a new input file named "run_all_POSCAR.sh" so that Lammps could read and convert them as forces.POSCAR-*.dump +
7) Firstly with "chmod +x run_all_POSCAR.sh" to run the following command in the terminal to make the script executable. Secondly to execute the script: "./run_all_POSCAR.sh", I obtained the forces.POSCAR-*.dump files. +
8) FORCE_SETS is generated with "phonopy --lammps -f forces_POSCAR-*.dump". +
9) The band.conf file is created manuelly and then frequency graph is occured with the code "phonopy -p band.conf". +

10) Using the data we obtained, I plotted the phonon dispersion relation of nanoribbons using python.

