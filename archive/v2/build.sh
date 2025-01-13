#!/bin/bash

# Attempt to delete auxiliary files and handle errors
echo "Cleaning up auxiliary files..."

try_cleanup() {
    # List of auxiliary file extensions to delete
    AUX_FILES=("*.aux" "*.bbl" "*.bcf" "*.blg" "*.out" "*.log" "*.toc" "*.run.xml")

    for ext in "${AUX_FILES[@]}"; do
        if ls $ext 1> /dev/null 2>&1; then
            rm $ext
            if [ $? -eq 0 ]; then
                echo "Deleted $ext files successfully."
            else
                echo "Failed to delete $ext files."
            fi
        else
            echo "No $ext files found."
        fi
    done
}

try_cleanup || echo "An error occurred during cleanup."

# Continue the build process

# Clean up LaTeX files with dos2unix
echo "Linting files with dos2unix..."
find . -name "*.tex" -exec dos2unix {} \;

# Compile the LaTeX document
echo "Compiling LaTeX document..."
pdflatex book_fixed_v2.tex

# Check for errors in the LaTeX log
if grep -i "error" book_fixed.log; then
  echo "Errors found in LaTeX log. Please fix them."
  exit 1
else
  echo "Build completed successfully!"
fi
