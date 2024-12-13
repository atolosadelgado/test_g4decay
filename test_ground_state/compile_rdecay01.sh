cp -r $G4INSTALL/share/Geant4/examples/extended/radioactivedecay/rdecay01 .
cmake -S rdecay01 -B build_rdecay01
cmake --build build_rdecay01 -- -j 8
