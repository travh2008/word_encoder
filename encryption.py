from base64 import encode


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount = shift_amount * -1
    for char in start_text:
        if char in alphabet:
            start_position = alphabet.index(char)
            end_position = start_position + shift_amount
            end_text += alphabet[end_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text has been changed to {end_text}")



should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
    
    ask = input("Type 'y' if you want to go again. Otherwise press any key to close the program.")
    if ask != 'y':
        should_continue = False
        print("Goodbye!")