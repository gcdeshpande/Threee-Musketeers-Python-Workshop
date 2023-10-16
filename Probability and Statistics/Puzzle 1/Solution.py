def find_next_number(sequence):
    differences = []
    for i in range(1, len(sequence)):
        differences.append(sequence[i] - sequence[i-1])
    
    # Check if the differences are the same
    if len(set(differences)) == 1:
        return sequence[-1] + differences[0]
    else:
        # If the differences are not the same, 
        # we cannot predict the next number in the sequence
        return None

# Example usage:
sequence = [12, 12, 6, 18, 8, 12, 4]     
#sequence = [4, 8, 12, 16, 20, 24]     

next_number = find_next_number(sequence)

if next_number is not None:
    print(f"The next number in the sequence is {next_number}.")
else:
    print("Cannot determine the next number in the sequence.")
