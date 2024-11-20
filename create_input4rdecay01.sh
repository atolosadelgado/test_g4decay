#!/bin/bash

# Directory containing the files
input_dir="$G4INSTALL/share/Geant4/data/RadioactiveDecay5.6"
# Path to the template macro file
template_macro="./template_macro_rdecay01.mac"
# Output directory for specific macro files
output_dir="./mymacros"

# Create output directory if it doesn't exist
mkdir -p "$output_dir"

# Loop over the files with the pattern z*.a*
for file in "$input_dir"/z*.a*; do
    # Extract the filename without the directory path
    filename=$(basename "$file")
    
    # Tokenize the filename into parts
    IFS='.' read -r z_part a_part <<< "$filename"
    
    # Remove the 'z' and 'a' letters and extract the numbers
    input_z=${z_part#z}
    input_a=${a_part#a}
    
    # Define the output macro file name
    output_macro="$output_dir/macro_z${input_z}_a${input_a}.mac"
    output_filename=ofile_z${input_z}_a${input_a}
    
    # Use sed to replace placeholders in the template and save to the new file
    sed -e "s/input_z/$input_z/g" \
        -e "s/input_a/$input_a/g" \
        -e "s/output_filename/$output_filename/g" \
        "$template_macro" > "$output_macro"
    
    # Output the created macro file name
    echo "Created macro file: $output_macro"
done
