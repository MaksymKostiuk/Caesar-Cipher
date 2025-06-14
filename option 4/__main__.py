#https://www.youtube.com/watch?v=QYng_rXg5OQ&ab_channel=FabioMusanni-ProgrammingChannel

letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)

key = 3

def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        letter = letter.lower()
        if not letter == " ":
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                ciphertext += letters[new_index]
        else:
            ciphertext += " "
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == " ":
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters
                plaintext += letters[new_index]
        else:
            plaintext += " "
    return plaintext

def encrypt_decrypt(text, mode, key):
    result = ""
    if mode == "d":
        key = -key
    
    for letter in text:
        letter = letter.lower()
        if not letter == " ":
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]
        else:
            result += " "
    return result


print(encrypt_decrypt("Man, I want chucken", "d", 1))