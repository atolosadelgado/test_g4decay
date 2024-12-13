# Create macro files for each isotope

This step creates around 28k macro file, which can be used in the next step.

```
chmod +x create_input_rdecay01_excited.py
python3 create_input_rdecay01_excited.py -i /usr/local/geant4/data/G4ENSDFSTATE3.0/ENSDFSTATE.dat
```

# Copy and compile rdecay01 example

```
chmod +x compile_rdecay01.sh
./compile_rdecay01.sh 
```

# Create list of files

```
ls mymacros/* > mylist.txt
```

# Use GNU parallel to run the tests

```
parallel -a mylist.txt ./run_one_decay.sh {} \; > out_parallel
```

# Disclaimer 

Each decay will simulate 1M events and full decay chain, for 78Ni takes around 6 minutes to run.
