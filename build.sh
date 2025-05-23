#!/bin/bash

# Default behavior: cleanup after build
CLEANUP=true
OUTPUT_DIR="outputs"

# Parse flags
while getopts "v" option; do
    case $option in
        v) CLEANUP=false ;; # Disable cleanup when -v is passed
        *) echo "Usage: $0 [-v]" && exit 1 ;; # Handle invalid flags
    esac
done

# Create outputs directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Run pdflatex and save logs to the outputs directory
echo "Compiling LaTeX document..."
# Run LaTeX build steps
pdflatex book.tex 2>&1 | tee build.log
bibtex book 2>&1 | tee -a build.log
pdflatex book.tex 2>&1 | tee -a build.log
pdflatex book.tex 2>&1 | tee -a build.log

# Check for errors during compilation
if [ $? -ne 0 ]; then
    echo "Error: LaTeX compilation failed! See $OUTPUT_DIR/build.log for details."
    exit 1
fi

# Handle cleanup behavior
if [ "$CLEANUP" = true ]; then
    echo "Cleaning up temporary files..."
    find "$OUTPUT_DIR" -type f \( -name "*.aux" -o -name "*.toc" -o -name "*.out" \) -delete
else
    echo "Skipping cleanup (temporary files retained)."
fi

echo "Build completed successfully. Outputs and logs are in the $OUTPUT_DIR directory."
