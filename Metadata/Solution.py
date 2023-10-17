import datetime

# Sample metadata from a suspicious document
metadata = {
    "Author Name": "John Doe",
    "Last Modified Date": "2023-10-17",
    "Software Version": "Word 2020",
    "Computer Name": "COMP-XY12"
}

# List of suspects and their computer names
suspects = {
    "Alice": "COMP-AB34",
    "Bob": "COMP-XY12",
    "Charlie": "COMP-ZZ09",
    "Daisy": "COMP-AA01"
}

def find_suspect(metadata, suspects):
    computer_name = metadata["Computer Name"]
    for suspect, comp in suspects.items():
        if comp == computer_name:
            return suspect
    return "Unknown"

suspect_found = find_suspect(metadata, suspects)
print(f"The potential inside accomplice is: {suspect_found}")
