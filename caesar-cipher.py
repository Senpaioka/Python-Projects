
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'w', 'x', 
'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'w', 'x', 
'y', 'z']

should_continue = True




def caesar(start_text, shift_amount, cipher_direction) :
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet :
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else :
            end_text += char
    print(f"the {cipher_direction}d text is {end_text}")


while should_continue :
    direction = input("type 'encode' to encrypt, type 'decode' to decrypt : \n").lower()
    text = input("type your message: \n").lower()
    shift = int(input("type the shift number: \n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    asking = input("do you want to continue? type 'yes' or 'no' : \n").lower()

    if asking == "no" :
        should_continue = False
        print("Goodbye")






