from base64 import encode


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount = shift_amount * -1
    for letter in start_text:
        start_position = alphabet.index(letter)
        end_position = start_position + shift_amount
        end_text += alphabet[end_position]
    print(f"The {cipher_direction}d text has been changed to {end_text}")

caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
# def encrypt(plain_text,shift_amount):
#     cipher_text = ""

#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")


# def decrypt(cipher_text,shift_amount):
#     plain_text=""

#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         original_position = position - shift_amount
#         original_letter = alphabet[original_position]
#         plain_text += original_letter
#     print(f"the decoded text is {plain_text}")
            


        

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

# if direction == "encode":
#     encrypt(plain_text=text,shift_amount=shift)
# if direction == "decode":
#     decrypt(cipher_text=text,shift_amount=shift)
#decrypt(cipher_text=text,shift_amount=shift)