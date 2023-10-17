import math

# Possible locations, their features, and GPS coordinates
locations = {
    "Beach House": {
        "features": ["sunset", "beach", "waves"],
        "coordinates": (34.0521, -118.2480)
    },
    "Mountain Cabin": {
        "features": ["sunset", "hiking", "waterfall"],
        "coordinates": (34.0560, -118.2500)
    },
    "City Apartment": {
        "features": ["sunset", "urban", "fountain"],
        "coordinates": (34.0500, -118.2400)
    }
}

# Hints from the victim
hints = ["sunset", "hiking", "waterfall"]

# Victim's last known GPS location
victim_gps = (34.0522, -118.2437)

def calculate_distance(coord1, coord2):
    """Calculate Euclidean distance between two GPS coordinates."""
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def match_location(hints, locations, victim_gps):
    best_match = None
    min_distance = float('inf')
    
    for location, attributes in locations.items():
        features = attributes["features"]
        coordinates = attributes["coordinates"]
        
        # Check how many hints match the features of each location
        match_count = sum([1 for hint in hints if hint in features])
        
        # Calculate the distance from the victim's GPS to the location's GPS
        distance = calculate_distance(victim_gps, coordinates)
        
        # If all hints match a location and the distance is less than the min_distance
        if match_count == len(hints) and distance < min_distance:
            best_match = location
            min_distance = distance
            
    return best_match

victim_location = match_location(hints, locations, victim_gps)
print(f"The most likely location of the victim is: {victim_location}")
