
#Lucas de Melo


def main():
    check = True
    while check:
        menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!")
        elif option==2:
            print("The encoded password is "+encoded+", and the original "
                                                      "password is " +password)
        elif option==3:
            check = False
        else:
            print("Enter an option from 1-3")

def encode(password):
    arr = []
    for val in password:
        if int(val) == 7:
            arr.append(0)
        elif int(val) == 8:
            arr.append(1)
        elif int(val) == 9:
            arr.append(2)
        else:
            arr.append(int(val)+3)

    encoded = ""
    for val in arr:
        encoded += str(val)
    return encoded

def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")

if __name__ == "__main__":
    main()



