#With help of https://www.youtube.com/watch?v=x71kJyNvB5o&list=PLCo_DyL8xVlINZxUI0jGgOgXVemMXiSnh&index=18&ab_channel=pixegami

message = "Hello, World!"
shift = 7

FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

result = ""

def caesar_shift(message, shift):
    # char is 1 symbol of the message
    for char in message.upper():
        if char.isalpha():
            # this is the character's ascii representation
            char_code = ord(char)
            # the symbol's new ascii representation
            new_char_code = char_code + shift

            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE

            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE

            # converting it into a human readable character
            new_char = chr(new_char_code)
            global result
            result += new_char
        else:
            result += char
    print(result)

user_message = input("Enter the message to encrypt: ")
user_key_shift = int(input("Enter the key: "))

caesar_shift(user_message, user_key_shift)