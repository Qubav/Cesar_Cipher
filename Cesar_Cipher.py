import string

# function encrypts message by changing letters in message based on position in alphabet adjusted by cipher direction and shift amount(how many letters)
def cipher(start_text: str, shift_amount: int, cipher_direction: str):
    # variable definition
    alphabet = list(string.ascii_lowercase)
    cipher_text = ""

    #adjusting shift amount
    if shift_amount > len(alphabet):
        shift_amount = shift_amount % len(alphabet)

    # adjusting alphabet used to determine letter corresponding to the position of letter in classic alphabet
    # adjusting is based on direction and shift amount
    if cipher_direction == "encode":
        shifted_alphabet = alphabet[shift_amount :] + alphabet[0: shift_amount]
    elif cipher_direction == "decode":
        shifted_alphabet = alphabet[- shift_amount::] + alphabet[0: len(alphabet) - shift_amount]

    # creating cipher text
    for char in start_text:
        # if char is letter it will be in alphabet and will be replaced
        if char in alphabet:
            position = alphabet.index(char)
            cipher_text += shifted_alphabet[position]
        # if char is not letter it will not be replaced
        else:
            cipher_text += char
        
    return cipher_text

# function works as Cesar Cipher. It allows user to enter message, encryption direction and shift amount, and then performs encryption on message.
def cesar_cipher():
    # variable that determines if loop continues
    again = True

    # main loop that allows to encrypt or decrypt without runing code again
    while again:

        # communication with user
        direction = input("Type \"encode\" to encrypt, type \"decode\" to decrypt:\n")
        while direction != "encode" and direction != "decode":
            print(f"You wrote wrong word - {direction}!")
            direction = input("Please type \"encode\" to encrypt, type \"decode\" to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        # message encryption
        cipher_text = cipher(start_text=text, shift_amount=shift, cipher_direction=direction)

        # communication with used
        print(f"The {direction}d text is {cipher_text}.")

        decision = input("Type:\n\"yes\" if You want to use Cesar Cipher again\n\"no\" if You don't want to\n")
        while decision != "no" and decision != "yes":
            print(f"You wrote wrong word - {decision}!")
            decision = input("Please type:\n\"yes\" if You want to use Cesar Cipher again\n\"no\" if You don't want to\n")
        
        if decision == "no":
            again = False

if __name__ == "__main__":
    cesar_cipher()