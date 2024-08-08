#!/bin/bash

# File paths
file_diff_path="file_diff.txt"
added_file_path="added.txt"
removed_file_path="removed.txt"
deploy_package_path="deployPackage"

# Create the deployPackage/added and deployPackage/removed directories if they don't exist
mkdir -p "${deploy_package_path}/added"
mkdir -p "${deploy_package_path}/removed"

# Initialize added.txt and removed.txt
> "$added_file_path"
> "$removed_file_path"

# Process each line in file_diff.txt
while IFS= read -r line; do
    status=$(echo "$line" | awk '{print $1}')
    file_path=$(echo "$line" | awk '{print $2}')
    file_name=$(basename "$file_path")
    
    if [[ "$status" == "M" || "$status" == "A" ]]; then
        echo "$file_name" >> "$added_file_path"
        cp "$file_path" "${deploy_package_path}/added/" 2>/dev/null
    elif [[ "$status" == "R" || "$status" == "D" ]]; then
        echo "$file_name" >> "$removed_file_path"
        cp "$file_path" "${deploy_package_path}/removed/" 2>/dev/null
    fi
done < "$file_diff_path"


