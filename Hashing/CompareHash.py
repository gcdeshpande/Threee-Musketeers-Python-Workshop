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
    # Taking input messages
    message1 = input("Enter the first message: ")
    message2 = input("Enter the second message: ")
    
    hash1, hash2 = compare_hashes(message1, message2)
    
    print(f"Hash of the first message: {hash1}")
    print(f"Hash of the second message: {hash2}")
    
    if hash1 == hash2:
        print("Both messages have the same hash.")
    else:
        print("The messages have different hashes.")

