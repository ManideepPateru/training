# a=input()
# etext=""
# dtext=""
# for i in a:
#     etext+=chr(ord(i)+2)
# print(etext)
# for i in etext:
#     dtext+=chr(ord(i)-2)
# print(dtext)
import string
from collections import Counter
def encrypt(message: str, key: int) -> str:
    encrypted_message = []
    for char in message:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                encrypted_message.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            elif char.isupper():
                encrypted_message.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            encrypted_message.append(char)
    return ''.join(encrypted_message)

def decrypt(message: str, key: int) -> str:
    decrypted_message = []
    for char in message:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                decrypted_message.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            elif char.isupper():
                decrypted_message.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
        else:
            decrypted_message.append(char)
    return ''.join(decrypted_message)
    
def get_letter_frequencies(text: str) -> dict:
    """ Returns the frequency of letters in the text. """
    text = [char.lower() for char in text if char.isalpha()]
    frequencies = Counter(text)
    return frequencies

def crack_caesar_cipher(ciphertext: str) -> int:
    """ Returns the most likely key for the Caesar cipher based on frequency analysis. """
    letter_frequencies = get_letter_frequencies(ciphertext)
    total_letters = sum(letter_frequencies.values())
    
    english_frequency = {
        'e': 0.127, 't': 0.090, 'a': 0.081, 'o': 0.075, 'i': 0.070,
        'n': 0.067, 's': 0.063, 'h': 0.061, 'r': 0.060, 'd': 0.043,
        'l': 0.040, 'u': 0.028, 'c': 0.027, 'm': 0.024, 'f': 0.022,
        'y': 0.021, 'p': 0.019, 'b': 0.015, 'g': 0.014, 'v': 0.010,
        'k': 0.008, 'x': 0.002, 'j': 0.002, 'q': 0.001, 'z': 0.001
    }
    
    sorted_cipher_freq = sorted(letter_frequencies.items(), key=lambda x: x[1], reverse=True)
    most_common_cipher_letter = sorted_cipher_freq[0][0]  
    
    most_common_letter = 'e'
    
    key = (ord(most_common_cipher_letter) - ord(most_common_letter)) % 26
    return key

def main():

    print("Welcome to Caesar Cipher Encryption and Decryption System")
    operation = input("Enter the operation (encrypt/decrypt/crack): ").strip().lower()

    if operation == "encrypt":
        
        message = input("Enter the message to encrypt: ").strip()
        key = int(input("Enter the key (0-25): ").strip())
        encrypted_message = encrypt(message, key)
        print(f"Encrypted Message: {encrypted_message}")

    elif operation == "decrypt":
       
        encrypted_message = input("Enter the encrypted message: ").strip()
        key = int(input("Enter the key used for encryption (0-25): ").strip())
        decrypted_message = decrypt(encrypted_message, key)
        print(f"Decrypted Message: {decrypted_message}")

    elif operation == "crack":
        
        intercepted_encrypted_message = input("Enter the intercepted encrypted message: ").strip()
        key_found = crack_caesar_cipher(intercepted_encrypted_message)
        print(f"Cracked Key: {key_found}")
        
        decrypted_message_from_crack = decrypt(intercepted_encrypted_message, key_found)
        print(f"Decrypted Message from Cracked Key: {decrypted_message_from_crack}")

    else:
        print("Invalid operation! Please choose either 'encrypt', 'decrypt', or 'crack'.")

if __name__ == "__main__":
    main()