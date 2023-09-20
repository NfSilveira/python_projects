def caesar():

    data = input("Enter the text that you want to encrypt or decrypt: ").upper()
    key = int(input("Enter the value of the key(displacement): "))
    mode = input("Enter the mode(E for encryption, D for decryption): ").upper()

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_data = ''

    for c in data:

        index = alphabet.find(c)

        if index == -1:

            new_data += c

        else:

            if mode == "E":

                new_index = index + key

            else:

                new_index = index - key

            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]

    if mode == "E":
        print(f"The encrypted message is {new_data}")
    else:
        print(f"The decrypted message is {new_data}")


if __name__ == "__main__":

    caesar()