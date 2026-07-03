FindMinimum = lambda No1, No2: No1 if No1 < No2 else No2

def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    result = FindMinimum(value1, value2)

    print("Minimum number is:", result)

if __name__ == "__main__":
    main()