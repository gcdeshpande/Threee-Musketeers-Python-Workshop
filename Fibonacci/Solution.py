from datetime import date, timedelta

def find_next_target(days_sequence, n):
  """
  Finds the next target day based on Fibo's number sequence.

  Parameters:
  - days_sequence: List of integers, the known sequence of days.
  - n: Integer, the total length of sequence to be returned.

  Returns:
  List of integers, the extended sequence of days.
  """
  while len(days_sequence) < n:
      # Add the last two numbers to get the next one
      days_sequence.append(days_sequence[-1] + days_sequence[-2])
  return days_sequence

# Fibo's sequence found at the crime scene
fibo_days = [5, 5, 10, 15, 25, 40]

# Predicting the next few numbers in Fibo's sequence
extended_days = find_next_target(fibo_days, 10)

# Display the result
print(f"Fibo's extended sequence: {extended_days}")

def daynumber_to_date(daynumber, year):
    """
    Convert a day number and year to a date.

    Parameters:
    - daynumber: Integer, the day number (e.g., 105).
    - year: Integer, the reference year (e.g., 2023).

    Returns:
    Date, the corresponding date for the given day number in the specified year.
    """
    return date(year, 1, 1) + timedelta(daynumber - 1)

# Example usage:
day_num = 105
year_reference = 2023
converted_date = daynumber_to_date(day_num, year_reference)
print(f"The date for day number {day_num} in the year {year_reference} is {converted_date}.")

