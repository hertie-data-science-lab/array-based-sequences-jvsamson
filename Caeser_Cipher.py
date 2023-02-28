#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 17:44:59 2023

@author: Justus v. Samson-Himmelstjerna
"""
# Define a class for encrypting and decrypting messages using a Caesar cipher.
class Caesar_Cipher:
  
  # Define a Class Constructor for creating a new Caesar cipher with a given shift amount.
  def __init__(self, shift):
    # Create temporary arrays for encoding and decoding characters.
    encoder = [None] * 26
    decoder = [None] * 26
    # Iterate over each letter in the alphabet and shift it by the given amount.
    # The built-in Python functions chr() and ord() converts a specified integer into the corresponding ASCII characters and vice versa.
    for r in range(26):
      encoder[r] = chr((r + shift) % 26 + ord('A'))
      decoder[r] = chr((r - shift) % 26 + ord('A'))
    # Join the arrays of encoded and decoded characters into strings.
        # self.encoder shifts each character to the right.
    self.encoder = ''.join(encoder)
            # This is the alphabet that is used to decrypt the message.
    self.decoder = ''.join(decoder)
    # Store the shift as an attribute of the object in order to be called
    self.shift = shift 


  # Method for encrypting a message using the current Caesar cipher.
  def encrypt(self, message):
    # Call the transform method with the encoder string to encrypt the message.
    return self.transform(message, self.encoder)

  # Method for decrypting a message using the current Caesar cipher.
  def decrypt(self, secret):
    # Call the transform method with the decoder string to decrypt the message.
    return self.transform(secret, self.decoder)

  # Define the transform method
  def transform(self, message, code):
    # Create a list of characters from the original message
    msg = list(message)
    
    # Iterate over each character in the list
    for i in range(len(msg)):
        # Convert the character to uppercase and get the index in the alphabet
        if msg[i].isalpha():
            j = ord(msg[i].upper()) - ord('A')
            
            # Replace the character with its corresponding code from the code string
            msg[i] = code[j]
    
    # Join the list of characters back into a string and return it.
    return ''.join(msg)

#Ask the user for the desired shift amount
shift = int(input("Choose your shift amount : "))
print()

#Create a new Caesar cipher with the given shift amount.
cipher = Caesar_Cipher(shift)

def run_methods(shift):
    while True:
        choice = int(input("Enter 1 to encrypt, 2 to decrypt or any number to exit: "))
        print()
        if choice == 1:
            message = input("Input message to encrypt : ")
            print()
            coded = cipher.encrypt(message)
            print("Encrypted Message : {}".format(coded))
            # Print the encryption method used and the number of shifts undertaken
            print("Encryption Method: " + type(cipher).__name__ + " with a shift of", cipher.shift)
        elif choice == 2:
            secret = input("Input secret to decrypt : ")
            answer = cipher.decrypt(secret)
            print("Decrypted Message : {}".format(answer), end="\n")
        else:
            break
        

#Run the encryption or decryption methods based on the choice of the user
run_methods(shift)