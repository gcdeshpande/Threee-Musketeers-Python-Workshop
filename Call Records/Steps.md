To solve the crime puzzle based on the call records of Amelia and the three suspects, we'll use Python to match the time and duration of the calls. Here's a step-by-step solution:

Step-by-Step Instructions to Solve the Crime Puzzle Using Python:

## Define the Call Record Data
Begin by defining the call records for Amelia and each suspect in a structured way, using lists or dictionaries.
```python
# Amelia's call record
amelia_call = {
    'time': '7:23 PM',
    'duration': '3:42'
}

# Suspects' call records
suspects_records = {
    'Marcus': [
        {'time': '7:20 PM', 'duration': '2:00', 'type': 'Received'},
        {'time': '7:24 PM', 'duration': '3:00', 'type': 'Made'},
        {'time': '8:10 PM', 'duration': '5:00', 'type': 'Received'}
    ],
    'Elena': [
        {'time': '7:15 PM', 'duration': '7:00', 'type': 'Made'},
        {'time': '7:23 PM', 'duration': '3:42', 'type': 'Received'},
        {'time': '8:30 PM', 'duration': '4:00', 'type': 'Made'}
    ],
    'Vincent': [
        {'time': '6:50 PM', 'duration': '15:00', 'type': 'Received'},
        {'time': '7:50 PM', 'duration': '10:00', 'type': 'Made'}
    ]
}
```

# Match Call Records
Loop through the call records of each suspect to see if any of them matches Amelia's call in terms of time and duration.
```python
# Function to find the match
def find_matching_call(amelia_call, suspects_records):
    for suspect, calls in suspects_records.items():
        for call in calls:
            if call['time'] == amelia_call['time'] and call['duration'] == amelia_call['duration'] and call['type'] == 'Received':
                return suspect
    return None

# Find the matching suspect
matching_suspect = find_matching_call(amelia_call, suspects_records)
```

# Display the Result
Print out the result to reveal which suspect Amelia called.
```python
if matching_suspect:
    print(f"Amelia called {matching_suspect} before her disappearance.")
else:
    print("No matching call record found among the suspects.")
```
When you run the above code, the program will reveal that Amelia called Elena before her disappearance.
