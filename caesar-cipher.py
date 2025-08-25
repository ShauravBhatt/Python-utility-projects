"""
Building a Caesar Cipher

Challenge: Secret Message Encryptor & Decryptor

Create a Python script that helps you send secret messages to your friend using simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
   - Ask for a message and a numeric secret key.
   - Use a Caesar Cipher (shift letters by the key value).
   - Output the encrypted message.
3. If decrypting:
   - Ask for the encrypted message and key.
   - Reverse the encryption to get the original message.

Rules:
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 → 'a').

Bonus:
- Allow uppercase and lowercase letter handling
- Show a clean interface
"""

def encrypt_message(message, key):
    result = ""
    for ch in message:
        if ch.isalpha():    
            base = ord('A') if ch.isupper() else ord('a')
            shifted = (ord(ch) - base  + key ) % 26 + base
            result += chr(shifted)
        
        else:
            result += ch 
    return result 

def decrypt_message(message, key):
    return encrypt_message(message, -key)

print(f"\n{"-"*10}Secret message encoder/decoder Script{"-"*10}")
task = input("You want to (E)ncrypt or (D)ecrypt : ").strip().lower()

if task == "e" or task == "":
    try:
        message = input("\nEnter the secret message 💬 : ")
        key =  int(input("Enter the secret key (Any random number b/w 1 to 25 only !!) 🔑 : "))

        if not 1<= key <=25:
           raise ValueError("Invalid value of Key !!")

        encrypted_message = encrypt_message(message , key)
        print("\nYour encrypted secret message is 🔐 : ")
        print(encrypted_message)

    except ValueError as ve:
        print(f"Error:  {ve}")

elif task == "d":
    try:
        message = input("Enter the secret message 💬 : ")
        key =  int(input("Enter the secret key 🔑 : "))

        if not 1<= key <=25:
            raise ValueError("Invalid value of Key !!")

        decrypted_message = decrypt_message(message , key)
        print("\nYour decrypted secret message is 🔓 : ")
        print(decrypted_message)

    except ValueError as ve:
        print(f"Error:  {ve}")

else:
    print("Error: Please select valid option !!")

