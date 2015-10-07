#!/bin/bash
#command to find the files named NOTES and delete them
find . -name NOTES -exec rm -rf {} \;
#creating cleaned_data directory
mkdir cleaned_data
#command to move all the files from data's subdirectories to cleaned_files
mv data/alexander/* data/Bert/* data/Frank_Richard/* data/gerdal/* data/jamesm/* data/Lawrence/* data/THOMAS/* cleaned_data/
#change directory to claeaned_data
cd cleaned_data
#command to rename all files in cleaned_files with .txt extension 
for filename in *; do mv $filename $filename.txt; done