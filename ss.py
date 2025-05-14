import numpy as np
from bitarray import bitarray

# Initial Permutation Table (IP)
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Expansion Permutation (E/P)
E = [32, 1, 2, 3, 4, 5, 4, 5,
     6, 7, 8, 9, 8, 9, 10, 11,
     12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27,
     28, 29, 28, 29, 30, 31, 32, 1]

# Permutation P4 (final permutation after S-box substitution)
P4 = [16, 7, 20, 21, 29, 12, 28, 17,
      1, 15, 23, 26, 5, 18, 31, 10,
      2, 8, 24, 14, 32, 27, 3, 9,
      19, 13, 30, 6, 22, 11, 4, 25]

# Sample S-Box (S1 for simplicity)
S1 = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
       [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
       [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
       [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]]

def permute(block, table):
    return bitarray([block[i - 1] for i in table])

def sbox_substitution(bits):
    row = int(str(bits[0]) + str(bits[5]), 2)
    col = int(bits[1:5].to01(), 2)
    return bitarray(format(S1[0][row][col], '04b'))

def des_first_round(plaintext, key):
    # Convert plaintext to binary
    binary_plaintext = bitarray()
    binary_plaintext.frombytes(plaintext.encode('utf-8'))
    
    # Apply initial permutation
    permuted_plaintext = permute(binary_plaintext, IP)
    L, R = permuted_plaintext[:32], permuted_plaintext[32:]
    
    # Expand R using E
    expanded_R = permute(R, E)
    
    # Generate round key (dummy round key for demonstration)
    round_key = bitarray(key[:48])  # Use first 48 bits as round key
    
    # XOR with round key
    xor_result = expanded_R ^ round_key
    
    # Apply S-box substitution (using only S1 for demonstration)
    sbox_result = sbox_substitution(xor_result[:6])
    
    # Permute using P4
    permuted_sbox = permute(sbox_result, P4)
    
    # XOR with L and swap halves
    new_R = L ^ permuted_sbox
    new_L = R
    
    # Combine L and R
    final_result = new_L + new_R
    return final_result

# Dynamic input
plaintext = input("Enter 8-character plaintext: ")[:8]
key = input("Enter 64-bit binary key: ")[:64]
ciphertext = des_first_round(plaintext, key)

print("Ciphertext after first round:", ciphertext)
