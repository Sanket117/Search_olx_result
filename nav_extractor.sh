#!/bin/bash

# AMFI NAV Data Extractor Script

# Set output files
TSV_OUTPUT="amfi_nav_data.tsv"
JSON_OUTPUT="amfi_nav_data.json"

# Create temporary file
TEMP_FILE=$(mktemp)

# Download the NAV data
wget -q https://www.amfiindia.com/spages/NAVAll.txt -O "$TEMP_FILE"

# Check if download was successful
if [ ! -s "$TEMP_FILE" ]; then
    echo "Failed to download NAV data"
    exit 1
fi

# Extract Scheme Name and Asset Value to TSV
echo -e "Scheme Name\tAsset Value" > "$TSV_OUTPUT"
tail -n +2 "$TEMP_FILE" | awk -F';' '{if ($3 != "") print $3 "\t" $4}' >> "$TSV_OUTPUT"

# Convert TSV to JSON using jq
tail -n +2 "$TEMP_FILE" | awk -F';' '{if ($3 != "") print "{\"scheme_name\": \""$3"\", \"asset_value\": \""$4"\"}"}' | jq -s '.' > "$JSON_OUTPUT"

# Clean up temporary file
rm "$TEMP_FILE"

# Print output file paths
echo "TSV data saved to: $TSV_OUTPUT"
echo "JSON data saved to: $JSON_OUTPUT"

# Optional: Display first few lines of each file
echo -e "\nFirst 5 lines of TSV:"
head -n 5 "$TSV_OUTPUT"

echo -e "\nFirst 5 lines of JSON:"
head -n 5 "$JSON_OUTPUT"
