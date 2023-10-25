def encode(password):
    global encoded
    encoded = ""
    for digit in password:
        encoded += str(int(digit) + 3)


def decode(encrypted_password):
    # TODO: decode implementation for Mr. Squires
    pass


password = None
encoded = None
while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

    option = input("Please enter an option: ")

    if option == 1:
        password = input("Please enter your password to encode: ")
        encode(password)
        print("Your password has been encoded and stored!")
    elif option == 2:
        # TODO: decode implementation for Mr. Squires
        print(f"The encoded password is {encoded}, and the original password is {password}")
    else:
        break
