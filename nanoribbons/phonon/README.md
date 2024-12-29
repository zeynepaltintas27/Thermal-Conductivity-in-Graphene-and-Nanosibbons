To visualize the phonon dispersion relation, all necessary files must be prepared. The results can be obtained directly by executing `dispersion.py`. Alternatively, the files can be generated manually by following the procedure described below.

The phonon dispersion relation for nanoribbons, comprising four basis atoms, was calculated incrementally utilizing
LAMMPS, following a systematic approach as outlined below:
1) I created nanoribbons with 4 basis vectors with input file named in.nanoribbons, I created nanoribbons.data with write_data code and nanoribbons_forces_*.lammpstrsj files. (lmp_serial < in.nanoribbons).
2) Since the unit cell is not slanted, I added "0 0 0 xy xz yz" line to the created data file and
saved it.
3) I converted nanoribbons.data file to POSCAR file with python. You can find the code in
"lammps_to_poscar.py" file.
4) "phonopy --lammps -d --dim="1 5 1" -c nanoribbons.data" is runned and yaml and supercell files have been created.
5) POSCAR-001-POSCAR-1008 and phonopy_disp.yaml were created with "phonopy --dim="1 5 1" -d --amplitude=0.01".
6) Since Lammps could not read POSCAR-### files, I converted the all files to POSCAR-###.data files with python (convert_poscar_to_lammps.py).
7) I created a new input file named "run_all_split.sh" so that Lammps could read the necessary data.
8) Firstly with "chmod +x run_all_split.sh" to run the following command in the terminal to make the script executable. Secondly to execute the script: "./run_all_split.sh", I obtained the forces_POSCAR-***.dump files.

9) The band.conf file was created and with the code "phonopy --lammps -f forces_POSCAR-*.dump", FORCE_SETS and phonopy.yaml and band.yaml files were created. ???
phonopy --dim="6 48 2" --fc-symmetry
phonopy --band band.conf
(Phonopy relies on the FORCE_SETS file to proceed. If it is not generated correctly, then phonopy.yaml and band.yaml files will also not be created.)
10) Using the data we obtained, I plotted the phonon dispersion relation of graphene-nanoribbons using python.


2 region oluşturacaksın, ilki büyük ve içi boş simülasyon regionı, 2. küçük olana atomlar yerleşecek. y eksenine bakacaksın. y_spacing
dim 1 5 1, 1 * 1 ilk önce.
