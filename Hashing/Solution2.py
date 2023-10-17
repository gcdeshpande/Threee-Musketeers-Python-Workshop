import hashlib

def compute_hash(message):
    """Compute the SHA-256 hash of a given message."""
    return hashlib.sha256(message.encode()).hexdigest()

def compare_hashes(message1, message2):
    """Compare the hashes of two messages."""
    hash1 = compute_hash(message1)
    hash2 = compute_hash(message2)
    
    return hash1, hash2

if __name__ == "__main__":
    # Message from the suspect
    suspect_message = "Stayed in and watched a movie. Talk tomorrow!"
    
    # Message from the friend's phone
    friend_message = "Stayed in and watched a film. Talk tomorrow!"
    
    hash1, hash2 = compare_hashes(suspect_message, friend_message)
    
    print(f"Hash of the suspect's message: {hash1}")
    print(f"Hash of the friend's message: {hash2}")
    
    if hash1 == hash2:
        print("The messages have the same hash. The suspect's claim might be true.")
    else:
        print("The messages have different hashes. The suspect's claim is false.")

