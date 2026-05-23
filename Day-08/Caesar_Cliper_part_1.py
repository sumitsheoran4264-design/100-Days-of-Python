
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Hello, 2
def encrypt(orginial_text, shift_amount):
    cipher_text = ""
                   
    for letter in orginial_text:
        shifted_position = alphabet.index(letter) + shift_amount # letter + shifted_amount = shift_position
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encode result: {cipher_text}")




encrypt(orginial_text=text, shift_amount=shift)
    
 