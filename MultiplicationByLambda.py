Multiplication = lambda No1, No2 : No1 * No2 

def main():
    value1 = int(input("Enter first Number : "))
    value2 = int(input("Ener second Number : "))

    Multiplication(value1, value2)

    print("Multiplication is : ",Multiplication(value1, value2))

if __name__ == "__main__":
    main()