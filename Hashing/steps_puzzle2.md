To help Detective Lara, you need to compute and compare the hashes of the two messages. Let's assume we are using the MD5 hashing algorithm (though in practice, a more secure algorithm would be preferable).

Here's a step-by-step guide:

# Initialization:
Import the necessary libraries and define the messages.
```python
import hashlib

suspect_message = "Stayed in and watched a movie. Talk tomorrow!"
friend_message = "Stayed in and watched a film. Talk tomorrow!"
```

# Hash Function:
Define a function that takes a message as input and returns its MD5 hash.
```python
def get_md5_hash(message):
    return hashlib.md5(message.encode('utf-8')).hexdigest()
```

# Compute Hashes:
Compute the hashes for both the suspect's message and the friend's message.
```python
if suspect_hash == friend_hash:
    print("The messages are identical.")
else:
    print("The messages are different.")
```

Running this program will help Detective Lara confirm whether the suspect's claim about the message content is true.
