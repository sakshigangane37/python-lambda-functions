FindEven = lambda No1 : "True" if No1 % 2 == 0 else "False" 

def main():
    value = int(input("Enter a Number : "))

    FindEven(value)

    print(FindEven(value))

if __name__ == "__main__":
    main()