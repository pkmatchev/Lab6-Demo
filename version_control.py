def encode(password):
    global encoded
    encoded = ""
    for digit in password:
        encoded += str(int(digit) + 3)


def decode(encrypted_password):
    # TODO: decode implementation for Mr. Squires
    decoded = ""
    for char in encrypted_password:
        new = int(char) - 3
        if new < 0:
            decoded += str(new)[1]
        else:
            decoded += str(new)
    return decoded


password = None
encoded = None
while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

    option = input("Please enter an option: ")

    if int(option) == 1:
        password = input("Please enter your password to encode: ")
        encode(password)
        print("Your password has been encoded and stored!")
    elif int(option) == 2:
        # TODO: decode implementation for Mr. Squires
        password = decode(encoded)
        print(f"The encoded password is {encoded}, and the original password is {password}")
    else:
        break
