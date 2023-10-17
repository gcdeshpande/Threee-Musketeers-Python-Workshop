import math

# Given Values
AB = 5  # Length AB in cm
AC = 7  # Length AC in cm
angle_A_deg = 40  # Angle A in degrees

# Convert angle A to radians as math.sin function expects the angle in radians
angle_A_rad = math.radians(angle_A_deg)

# Calculate sin(C) using sin rule
sin_C = (AC/AB) * math.sin(angle_A_rad)

# If sin(C) > 1, print an error message since it's mathematically invalid
if sin_C > 1:
    print("The given data does not form a valid triangle.")
else:
    # Find angle C in radians
    angle_C_rad = math.asin(sin_C)

    # Calculate angle B in radians
    angle_B_rad = math.pi - angle_A_rad - angle_C_rad

    # Calculate length BC using sin rule
    BC = AB * math.sin(angle_C_rad) / math.sin(angle_B_rad)

    # Display the result
    print(f"The treasure is buried {round(BC, 2)} cm away from point C in the direction of point B.")
