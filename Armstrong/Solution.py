def is_armstrong(num):
  """Check if a number is an Armstrong number."""
  num_str = str(num)
  num_digits = len(num_str)
  return num == sum(int(digit)**num_digits for digit in num_str)

# Find ZIP codes that are Armstrong numbers
armstrong_zip_codes = [num for num in range(10000, 100000) if is_armstrong(num)]

print(f"ZIP codes that are Armstrong numbers: {armstrong_zip_codes}")
