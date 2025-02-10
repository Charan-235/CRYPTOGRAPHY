import string

def generate_cipher_alphabet(keyword):
    keyword = "".join(dict.fromkeys(keyword.upper()))  # Remove duplicates
    alphabet = string.ascii_uppercase.replace("J", "")  # Playfair-style alphabet
    cipher_alphabet = keyword + "".join(c for c in alphabet if c not in keyword)
    return dict(zip(string.ascii_uppercase, cipher_alphabet))

def monoalphabetic_encrypt(plaintext, keyword):
    cipher_map = generate_cipher_alphabet(keyword)
    return "".join(cipher_map.get(c, c) for c in plaintext.upper())

def monoalphabetic_decrypt(ciphertext, keyword):
    cipher_map = generate_cipher_alphabet(keyword)
    reverse_map = {v: k for k, v in cipher_map.items()}  # Reverse the cipher mapping
    return "".join(reverse_map.get(c, c) for c in ciphertext.upper())

# Example usage
keyword = "CIPHER"
plaintext = "HELLO WORLD"
ciphertext = monoalphabetic_encrypt(plaintext, keyword)
decrypted_text = monoalphabetic_decrypt(ciphertext, keyword)

print("Monoalphabetic Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)

Output:
Monoalphabetic Ciphertext: BEKKN XNSKH
Decrypted Text: HELLO WORLD
