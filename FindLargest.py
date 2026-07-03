FindLargest = lambda No1, No2, No3 : No1 if No1 > No2 and No1 > No3 else(No2 if No2 > No3 else No3)

def main():
    value1 = int(input("Enter First Number : "))
    value2 = int(input("Enter Second Number : "))
    value3 = int(input("Enter Third Number : "))

    FindLargest(value1, value2, value3)

    print("The Largest Number is : ",FindLargest(value1, value2, value3))

if __name__ == "__main__":
    main()
