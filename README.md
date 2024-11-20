# Create macro files for each isotope

```
chmod +x create_input4rdecay01.sh
./create_input4rdecay01.sh 
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
