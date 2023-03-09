from cipher import Cipher


class CaesarCipher(Cipher):
    def __init__(self, shift):
        super().__init__()
        if isinstance(shift, int):
            self.shift = shift
        else:
            raise TypeError("Shift value must be an integer.")

    def encrypt_letter(self, letter):
        if letter.upper() not in self.alphabet:
            return letter
        index = self.alphabet.index(letter.upper())
        encrypted_index = (index + self.shift) % len(self.alphabet)
        return self.alphabet[encrypted_index]

    def decrypt_letter(self, letter):
        if letter.upper() not in self.alphabet:
            return letter
        index = self.alphabet.index(letter.upper())
        decrypted_index = (index - self.shift) % len(self.alphabet)
        return self.alphabet[decrypted_index]
