#creating a caesar cipher
def caesar(direction, message, move):
    cipher_text = ""
    if direction == "decode":
        move*=-1
    if move > len(alphabet):
        move = move % len(alphabet)    
    for i in range(0,len(message)):
            if message[i] in alphabet:
                index = alphabet.index(message[i]) #.index() will you give you the first index it finds
                try:
                    cipher_text+=alphabet[index+move]
                except IndexError:
                    cipher_text+=alphabet[index-move]
            elif message[i] not in alphabet:
                cipher_text+=message[i]
    print(f"The {direction}d text is {cipher_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

go = True
while go is not False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n").lower()
    move = int(input("Type the shift number:\n"))

    caesar(direction,message,move)
    again = str(input("Would you like to go again? y or n\n"))
    if again == 'n':
        go = False

