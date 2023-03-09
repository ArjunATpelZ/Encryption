from cipher import Cipher
from caesar_cipher import CaesarCipher

# Prompt the user to choose encryption or decryption
print("Select Decoder Ring:")
print("1.Encrypt")
print("2.Decrypt")
choice = input()

# Prompt the user to choose a cipher
print("Enter Encryption Type:")
print("1.Atbash")
print("2.Casesar")
cipher_choice = input()

# Create the appropriate cipher object based on user choice
if cipher_choice.lower() == "1":
    cipher = Cipher()
elif cipher_choice.lower() == "2":
    # Prompt the user to enter a shift value
    shift = int(input("Enter a shift value (0-25): "))
    cipher = CaesarCipher(shift)
else:
    print("Invalid cipher choice. Please choose either '1.Atbash or '2.Caesar'.")
    exit()

# Perform encryption or decryption based on user choice
if choice.lower() == "1":
    # Prompt the user to enter a message to encrypt
    message = input("Enter a message to encrypt: ")
    encrypted_message = ''

    # Encrypt each letter in the message using the appropriate cipher method
    for letter in message:
        if cipher_choice.lower() == "1":
            encrypted_message += cipher.encrypt_letter(letter)
        elif cipher_choice.lower() == "2":
            encrypted_message += cipher.encrypt_letter(letter)

    # Write the encrypted message to the file message.txt
    with open("message.txt", "w") as file:
        file.write(encrypted_message)

    print("Message encrypted and written to message.txt:\n", encrypted_message)
elif choice.lower() == "2":
    # Read the encrypted message from the file message.txt
    with open("message.txt", "r") as file:
        encrypted_message = file.read()

    decrypted_message = ''

    # Decrypt each letter in the message using the appropriate cipher method
    for letter in encrypted_message:
        if cipher_choice.lower() == "1":
            decrypted_message += cipher.decrypt_letter(letter)
        elif cipher_choice.lower() == "2":
            decrypted_message += cipher.decrypt_letter(letter)

    print("Encrypted message From File:", encrypted_message)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid choice. Please choose either 'encrypt' or 'decrypt'.")
