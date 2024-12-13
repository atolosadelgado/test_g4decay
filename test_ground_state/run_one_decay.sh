sleep 0.25

# take the macro file name as first argument
macro_file=$1

# Path to the Geant4 application binary
geant4_app="build_rdecay01/rdecay01"

# Directory containing the macro files
macro_dir="./mymacros"

# Output directory for logs
log_dir="./mymacros"

# Extract the macro file name without the path
macro_name=$(basename "$macro_file")
   
# Define the log file name
log_file="$log_dir/${macro_name%.mac}.log"
  
# Run the Geant4 application with the macro file, saving the output to the log file
#echo "Running $macro_file..."
"$geant4_app" "$macro_file" > "$log_file" 2>&1
    
# Check for the keywords "exception" or "error" in the log file
if grep -iE "exception|error" "$log_file" > /dev/null; then
    echo "Issue detected in $macro_file. Check the log: $log_file"
else
    echo "$macro_file executed successfully without errors."
fi
