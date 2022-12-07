#!/bin/bash

# This script takes a txt file which contains a list and prints them 
# with a comma and a space between each item.

# Prompt user for text file name
echo -n "Please enter the name of the text file: "
read fileName

# Read in contents of text file
listItems=$(cat $fileName)

# Loop through each item in the list
for item in $listItems
do
    # Print the item followed by a comma and a space
    echo -n "$item, "
done

# Check if output file already exists
if [ -f output.txt ]
then
    # Output file already exists
    echo "Output file already exists."
else
    # Output file does not exist
    # Create new output file
    touch output.txt
    # Loop through each item in the list
    for item in $listItems
    do
        # Append item to output file, followed by a comma and a space
        echo -n "$item, " >> output.txt
    done
fi
