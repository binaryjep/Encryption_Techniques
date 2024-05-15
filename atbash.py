atbash_cipher = {
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u',
    'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o',
    'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i',
    's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
    'y': 'b', 'z': 'a'
}

def atbashCipher(message): 

    ciphered_text = ""

    for letter in message:
        
        if letter != ' ': 

            ciphered_text += atbash_cipher[letter]
        else: 
            ciphered_text = ciphered_text + ''

    return ciphered_text 

def main(): 

    # encode
    message= input("Enter message: ")
    ciphered_text = atbashCipher(message)
    print(ciphered_text)

    # decode 
    plaintext = atbashCipher(ciphered_text)
    print(plaintext)

if __name__ ==  '__main__': 
    main()

