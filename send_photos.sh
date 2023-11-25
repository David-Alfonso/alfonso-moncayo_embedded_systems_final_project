#!/bin/bash

# Set the source and destination folders
source_folder="/home/david/proyecto_final/images"
destination_folder="azureuser@20.163.223.33:/home/azureuser/images_plant"
key_file="~/Davidcito_key.pem"

# Iterate through each file in the source folder
for file_path in "$source_folder"/*; do
    # Get the filename from the path
    file_name=$(basename "$file_path")

    # Perform scp operation
    scp -i "$key_file" "$file_path" "$destination_folder"

    # Check the exit status of the scp operation
    if [ $? -eq 0 ]; then
        echo "SCP for $file_name executed successfully. Deleting file."
        # Delete the file
        rm "$file_path"
    else
        echo "Error: SCP for $file_name encountered an error. Exit status: $?"
    fi
done
