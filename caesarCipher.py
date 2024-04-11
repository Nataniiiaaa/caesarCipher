def caesar_decrypt(ciphertext, shift):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

ciphertext = "BQQOT	MZPFT	AGSTF	UZAIO	AZRQE	EABQZ	XKMZP	RGXXK"
for shift in range(1, 26):
    decrypted_text = caesar_decrypt(ciphertext, shift)
    print(f"Shift {shift}: {decrypted_text}")
