logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""

print(logo)

# List of alphabets
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shifted_amount, encode_or_decode):

    # Store final result
    output_text = ""

    # For decode move backward
    if encode_or_decode == "decode":
        shifted_amount *= -1

    # Check every letter
    for letter in original_text:

        # Keep symbols and spaces same
        if letter not in alphabet:
            output_text += letter

        else:
            # Find new position
            shifted_position = alphabet.index(letter) + shifted_amount

            # Handle large numbers
            shifted_position %= len(alphabet)

            # Add new shifted letter
            output_text += alphabet[shifted_position]

    # Final output
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Run again and again
should_continue = True

while should_continue:

    # User inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    # Call function
    caesar(original_text=text,
           shifted_amount=shift,
           encode_or_decode=direction)

    # Continue or stop
    restart = input("Type 'yes' to continue or 'no' to stop:\n").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye")




    

    