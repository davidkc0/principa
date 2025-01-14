#!/bin/bash

# Directory containing the Python files
SOURCE_DIR="/Users/gnb/Projects/principa-master-localcomp/rendering"

# Generate the list of \inputminted lines
find "$SOURCE_DIR" -type f -name "*.py" | while read -r file; do
    # Remove the base directory prefix
    relative_path=${file#$SOURCE_DIR/}
    # Print the \inputminted line with the relative path
    echo "\\inputminted{python}{rendering/$relative_path}"
done
