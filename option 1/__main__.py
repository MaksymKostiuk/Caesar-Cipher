#With help of https://medium.com/@Operaho/make-a-caesars-cipher-with-python-8958ffa1e90d

alphabet, get_letter, keyword = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", 0, []
text = None
key = None

print ("You will be asked to enter the text you'd like to encrypt. It may have wharever you like, but only letters\n" \
"Key is responsible for the shift that will be made to replace one letter of the text")

def data():
    global text 
    text = str(input ("Insert the text you'd like to encrypt: ")).strip().lower()
    global key 
    key = int (input ("\nNow the key: " + "\n"))
    return ()





if __name__ == "__main__":
    while True:
        data()
        if 0 < key <= 26:
            for letter in text:
                get_letter = alphabet.index(letter) + key
                keyword.append(alphabet[get_letter])
            break
        else:
            print("Key must be at least 1 digit long, but not more than 26")
    print ("".join(keyword) + " is the keyword")