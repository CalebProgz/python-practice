
def main():
    #User input
    n = int(input("Enter a number: "))
    factorial = 1

    #For loop statement
    for i in range (1, n + 1):
        factorial *=i

    #Print the Value
    print (f"The factorial of {n} is {factorial}")

if __name__ == "__main__":
    main()