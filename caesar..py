alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesarCipher(message, shift_value: int): 

    ciphered_text = ""

    for letter in message: 

        if letter in message: 

            index = alphabet.index(letter)
            index = (index + shift_value) % len(alphabet)
            ciphered_text = ciphered_text + alphabet[index]
        else: 
            ciphered_text += letter
    
    return ciphered_text

message = input("Enter message: ")
shift_value = int(input("Enter shift value: "))

encode = caesarCipher(message,shift_value)
print(encode)