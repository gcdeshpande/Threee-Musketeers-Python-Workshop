# Step-by-Step Instructions to Solve the Crime Puzzle Using Numpy:

# Import the Necessary Libraries
```python
import numpy as np
```

# Load the Call Records Data
```python
records = np.array([
    ["A", "123-4567", "23:55", "2:15"],
    ["B", "999-9999", "23:57", "1:30"],
    ["C", "234-5678", "00:02", "5:00"],
    ["D", "345-6789", "00:01", "0:45"],
    ["A", "999-9999", "00:03", "3:30"],
    ["C", "D", "00:10", "1:00"]
])
```

# Filter and Analyze the Records
Use boolean indexing to filter out calls made to the external agent's number (999-9999) before the midnight meeting.
```python
# Find calls made to the external agent's number
suspects_calls = records[(records[:, 1] == '999-9999') & (records[:, 2] < '00:00')]
```

# Display the Result
```python
if len(suspects_calls) > 0:
    for call in suspects_calls:
        print(f"Suspect {call[0]} called the external agent at {call[2]} for a duration of {call[3]}.")
else:
    print("No suspect called the external agent before the midnight meeting.")
```

When you run the above code, you'll find that suspect B called the external agent just before the secret midnight meeting.

