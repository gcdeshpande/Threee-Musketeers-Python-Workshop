import math

def solve_mystery(height, distance, launch_angle):
    # Using the kinematic equations, considering launch angle:
    # distance = initial_velocity * time * cos(launch_angle)
    # height = initial_velocity * time * sin(launch_angle) - 0.5 * 9.8 * time^2
    
    # Estimations:
    # An accidental fall or suicide won't have much initial velocity, maybe around 1 m/s.
    # A push might have an initial velocity of around 5 m/s.
    
    g = 9.8  # gravitational acceleration in m/s^2
    angle_rad = math.radians(launch_angle)  # convert angle to radians
    
    # Calculating time from the height and launch angle, assuming a push (higher initial velocity)
    time_pushed = (-5 * math.sin(angle_rad) + (25 * (math.sin(angle_rad)**2) + 2 * g * height)**0.5) / g
    
    # Predicted distance if pushed
    distance_pushed = 5 * time_pushed * math.cos(angle_rad)
    
    # If the actual distance is close to the distance_pushed, it's likely a murder.
    if abs(distance - distance_pushed) < 2:  # a threshold of 2 meters for some error margin
        return "Murder"
    # If the body is very close to the building, it's an accidental fall or suicide.
    elif distance < 2:
        return "Accidental Fall or Suicide"
    else:
        return "Inconclusive"

if __name__ == "__main__":
    height = float(input("Enter the height from which the body fell (in meters): "))
    distance = float(input("Enter the horizontal distance from the building where the body was found (in meters): "))
    launch_angle = float(input("Enter the estimated launch angle (in degrees): "))

    result = solve_mystery(height, distance, launch_angle)
    print(f"The case is likely a result of: {result}")

#input 20,8,30
