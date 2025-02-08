import random
import string
# Function to generate a random substitution key
def generate_key():
    letters = list(string.ascii_lowercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))

# Function to encrypt using the monoalphabetic substitution cipher
def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext.lower():
        if char in key:
            ciphertext += key[char]
        else:
            ciphertext += char  # Keep non-alphabetic characters unchanged
    return ciphertext

# Function to decrypt using the monoalphabetic substitution cipher
def decrypt(ciphertext, key):
    reverse_key = {v: k for k, v in key.items()}  # Reverse the key mapping
    plaintext = ""
    for char in ciphertext.lower():
        if char in reverse_key:
            plaintext += reverse_key[char]
        else:
            plaintext += char  # Keep non-alphabetic characters unchanged
    return plaintext

# Generate a random substitution key
key = generate_key()

# Example plaintext
plaintext = "hello world"
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

# Output results
print("Substitution Key:", key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)

#Output
Substitution Key: {'a': 'c', 'b': 'z', 'c': 'w', 'd': 's', 'e': 'n', 'f': 'g', 'g': 'o', 'h': 'x', 'i': 'd', 'j': 'a', 'k': 'u', 'l': 'b', 'm': 'j', 'n': 'l', 'o': 'p', 'p': 'e', 'q': 'i', 'r': 'f', 's': 'r', 't': 'q', 'u': 'h', 'v': 'k', 'w': 'v', 'x': 'y', 'y': 'm', 'z': 't'}
Plaintext: hello world
Ciphertext: xnbbp vpfbs
Decrypted Text: hello world
