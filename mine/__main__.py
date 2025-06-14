#values

#CHAR_DIFFERENCE is used to return the count to the beginning of ASCII alphabet. +1 is used due to Z - A being 64 which is @ in ASCII

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
FIRST_CHAR = ord("A")
LAST_CHAR = ord("Z")
CHAR_DIFFERENCE = LAST_CHAR - FIRST_CHAR + 1
result = ""

#DONE
#Receive message and key values to operate with them later.
def user_info():
    print("You are about to be asked to provide the message you'd like to use along with the key(an integer)")
    message = input("Enter the message you'd like to operate with: ")
    key = int(input("Enter the key(shift) you'd like to try the message with: "))
    return (message, key)

#todo
#Encryption function.
def encrypt_func(message, key):
    global result
    for index in range(0, len(message)):
        if message[index] == " ":
            result += " "
        for index in range(0, )


    pass
#todo
#Decryption function
def decrypt_func(message, key):
    pass

#Main part
if __name__ == "__main__":
    while True:
        action = input("1 - (E)ncrypt or 2 - (D)ecrypt or 3 - (Q) to finish the program\n>> ")
        ui = user_info()
        if action.lower() == "e" or action == str(1):
            encrypt_func(ui[0], ui[1])
            print(result)
        elif action.lower() == "d" or action == str(2):
            decrypt_func(ui[0], ui[1])
        elif action.lower() == "q" or action == str(3):
            break



