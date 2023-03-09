class Cipher:
    def __init__(self):
        self.alphabet = [chr(i) for i in range(65, 91)]

    def encrypt_message(self, message):
        message = message.upper()
        encrypted_message = ''
        for char in message:
            if char.isalpha():
                encrypted_message += self._encrypt_letter(char)
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt_message(self, message):
        message = message.upper()
        decrypted_message = ''
        for char in message:
            if char.isalpha():
                decrypted_message += self._decrypt_letter(char)
            else:
                decrypted_message += char
        return decrypted_message

    def _encrypt_letter(self, letter):
        if letter == ' ':
            return letter
        elif letter.isalpha():
            location = self.alphabet.index(letter)
            encrypted_location = 25 - location
            encrypted_letter = self.alphabet[encrypted_location]
            return encrypted_letter
        else:
            return letter

    def _decrypt_letter(self, letter):
        if letter.isalpha():
            location = self.alphabet.index(letter)
            decrypted_location = 25 - location
            decrypted_letter = self.alphabet[decrypted_location]
            return decrypted_letter
        else:
            return letter

    def encrypt_letter(self, letter):
        if letter.isalpha():
            return self._encrypt_letter(letter.upper())
        else:
            return letter

    def decrypt_letter(self, letter):
        if letter.isalpha():
            return self._decrypt_letter(letter.upper())
        else:
            return letter
