# AMFI NAV Data Extractor

## Overview
This script downloads the latest Net Asset Value (NAV) data from the Association of Mutual Funds in India (AMFI) website and extracts the Scheme Name and Asset Value into two formats:
1. Tab-Separated Values (TSV)
2. JSON

## Prerequisites
- bash
- wget
- awk
- jq (JSON processor)

## Installation
```bash
# Install dependencies on Ubuntu/Debian
sudo apt-get update
sudo apt-get install wget gawk jq

# Install dependencies on macOS (using Homebrew)
brew install wget gawk jq
```

## Usage
```bash
chmod +x amfi_nav_extractor.sh
./amfi_nav_extractor.sh
```

## Output Files
- `amfi_nav_data.tsv`: Tab-separated file with Scheme Name and Asset Value
- `amfi_nav_data.json`: JSON array of scheme objects

## Data Format
### TSV Format
```
Scheme Name    Asset Value
Scheme 1       10.5
Scheme 2       15.75
```

### JSON Format
```json
[
  {
    "scheme_name": "Scheme 1",
    "asset_value": "10.5"
  },
  {
    "scheme_name": "Scheme 2", 
    "asset_value": "15.75"
  }
]
```

## Notes
- The script downloads data from https://www.amfiindia.com/spages/NAVAll.txt
- Data is extracted daily, reflecting the latest NAV information
- Some error handling is included for download failures

## Pros and Cons of Formats

### TSV Pros:
- Lightweight
- Easy to read
- Compatible with spreadsheet software
- Minimal overhead

### TSV Cons:
- Less structured
- No nested data support
- Limited type information

### JSON Pros:
- Structured data
- Supports complex nested objects
- Easy to parse in most programming languages
- Can include additional metadata

### JSON Cons:
- Larger file size
- Slightly more complex to read manually

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss proposed changes.

## License
[MIT](https://choosealicense.com/licenses/mit/)
