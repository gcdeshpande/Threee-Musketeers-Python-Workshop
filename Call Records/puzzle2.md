Detective Parker is working on an enigmatic case involving a secret corporate deal. There was a confidential meeting scheduled at midnight, and only a handful of individuals knew about it. But news leaked, and the deal went south. Someone had betrayed the company, and Detective Parker was sure that the betrayer had contacted an external agent via phone just before the meeting.

From the telecom company, Detective Parker managed to obtain a data dump of call records around the time of the meeting for the suspects. The data is vast, and manual inspection would be time-consuming. Detective Parker decides to use numpy for faster analysis.

The call records contain the following data for each call: caller, receiver, time, and duration.

Detective Parker has a list of four suspects: A, B, C, and D. The external agent's number is 999-9999.

# Given:

You have a numpy array with the call records around the time of the secret meeting:
```python
import numpy as np

records = np.array([
    ["A", "123-4567", "23:55", "2:15"],
    ["B", "999-9999", "23:57", "1:30"],
    ["C", "234-5678", "00:02", "5:00"],
    ["D", "345-6789", "00:01", "0:45"],
    ["A", "999-9999", "00:03", "3:30"],
    ["C", "D", "00:10", "1:00"]
])
```

# Task:
Using the numpy library, determine which suspect(s) called the external agent (999-9999) just before the secret midnight meeting.


