Square = lambda No: (No * No)

def main():
    value = int(input("Enter a number : "))

    Square(value)

    print("Square is : ", Square(value))

if __name__ == "__main__":
    main()