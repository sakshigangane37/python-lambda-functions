ChkDivisible = lambda Num : "True" if Num % 5 == 0 else "False"

def main():
    value = int(input("Enter a Number : "))

    ChkDivisible(value)

    print("Given Number is divisible by 5 : ", ChkDivisible(value))

if __name__ == "__main__":
    main()