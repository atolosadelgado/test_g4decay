#!/bin/python3

def read_ensdfstate(file_path):
    """
    Reads an ENSDFState file and creates macro files based on the template provided.

    Parameters:
        file_path (str): Path to the ENSDFState file.

    Returns:
        None
    """
    
    
    import os
    macrodir="./mymacros"
    if not os.path.exists(macrodir):
      os.makedirs(macrodir)
    template = """
# macro for rdecay01
#
/control/cout/ignoreThreadsExcept 0
/control/verbose 2
/run/verbose 1
#
/gun/particle ion
/gun/ion {input_z} {input_a} 0 {input_excitation_energy} {floating_level_char}

/process/had/rdm/nucleusLimits {input_a} {input_a} {input_z} {input_z}
#
/tracking/verbose 2
/run/beamOn 1
/tracking/verbose 0
#
/analysis/setFileName {output_basename}
/analysis/h1/set 1  1500  0. 1500 keV	#e+ e-
/analysis/h1/set 2  1500  0. 1500 keV	#neutrino
/analysis/h1/set 3  1500  0. 1500 keV	#gamma
/analysis/h1/set 6  1000  0. 2500 keV	#EkinTot (Q)
/analysis/h1/set 7  1500  0. 15e3 keV	#P balance
/analysis/h1/set 8  1000  0. 100. year	#time of life
/analysis/h1/set 9  1000  1. 3. MeV  	#EvisTot
#

# After 11.2, https://geant4.web.cern.ch/download/release-notes/notes-v11.2.0.html
/process/had/rdm/thresholdForVeryLongDecayTime 1.0e+60 year
 
/run/printProgress 1000000  
/run/beamOn 1000000
"""

    with open(file_path, 'r') as file:
        for line in file:
            # Skip empty lines
            if not line.strip():
                continue

            try:
                # Tokenize the line using spaces
                tokens = line.split()

                # Parse each field based on the tokenized format
                z = int(tokens[0])
                a = int(tokens[1])
                excitation_energy = float(tokens[2])
                floating_level = tokens[3]
                # strip initial symbol, - or +
                #   symbol - is not followed by anything
                #   symbol + is followed by floating level character, X,Y,Z...
                flb = floating_level[1:]
                halflife = float(tokens[4])
                spin = int(tokens[5])
                dipole_moment = float(tokens[6])

                # Generate output filename
                output_basename = f"macro_Z{z}_A{a}_E{excitation_energy}keV_flb{flb}"
                output_filename = f"{macrodir}/{output_basename}.mac"
                check_file = os.path.isfile(output_filename)
                if check_file:
                  print(f"Output file {output_filename} already exist, skipping...")
                  continue

                # Fill the template
                macro_content = template.format(
                    input_z=z,
                    input_a=a,
                    input_excitation_energy=excitation_energy,
                    floating_level_char=flb,
                    output_basename=output_basename
                )

                # Write to a file
                with open(output_filename, 'w') as output_file:
                    output_file.write(macro_content)

            except (ValueError, IndexError) as e:
                print(f"Error parsing line: {line.strip()}\n{e}")


import argparse, os
from argparse import ArgumentParser

def validate_file(f):
    if not os.path.exists(f):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} does not exist".format(f))
    return f

if __name__ == "__main__":

    parser = ArgumentParser(description="ENSDFSTATE file path")
    parser.add_argument("-i", "--input", dest="ENSDFSTATEfilename", required=True, type=validate_file,
                        help="input file", metavar="FILE")
    args = parser.parse_args()
    print(f"Processing file {args.ENSDFSTATEfilename} ...")
    read_ensdfstate(args.ENSDFSTATEfilename)
    
