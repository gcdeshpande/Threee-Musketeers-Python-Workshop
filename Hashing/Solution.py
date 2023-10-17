import hashlib
import itertools

# A basic list of English words for the demonstration.
# For a better solution, you might want to expand this list or use an English dictionary.
words = ["I", "you", "will", "find", "am", "hello", "a", "the", "this", "is", "test", "message"]

# Intercepted hashes
hashes = ["2347bb0ac593a4d184bb73eeb4a3589a", "d41d8cd98f00b204e9800998ecf8427e"]

def compute_md5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def generate_sentences():
    for sentence_length in range(1, 6):  # Sentences from 1 to 5 words
        for sentence in itertools.product(words, repeat=sentence_length):
            yield ' '.join(sentence)

def solve_puzzle():
    found_sentences = []
    
    for sentence in generate_sentences():
        if compute_md5(sentence) in hashes:
            print(f"Found: '{sentence}'")
            found_sentences.append(sentence)
    
    return found_sentences

solve_puzzle()
