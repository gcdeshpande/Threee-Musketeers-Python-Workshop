import math

def can_artifact_fit(length, height, width, artifact_length):
    """
    Checks if the artifact can fit inside the briefcase.
    """
    # Calculate the diagonal of the briefcase using Pythagoras theorem
    diagonal = math.sqrt(length**2 + height**2 + width**2)

    # Check if artifact can fit inside
    if diagonal >= artifact_length:
        return True
    else:
        return False

briefcase_length = 20  # inches
briefcase_height = 16  # inches
briefcase_width = 3    # inches
artifact_length = 24   # inches

if can_artifact_fit(briefcase_length, briefcase_height, briefcase_width, artifact_length):
    print("The artifact could possibly fit inside the suspect's briefcase.")
else:
    print("The artifact could not fit inside the suspect's briefcase.")

