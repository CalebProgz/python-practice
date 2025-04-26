#Factorial function
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)
    
def main():
    # User input for factorial calculation
    n2 = int(input("Enter a value to find the factorials: "))
    result = factorial(n2)

    # Print the result
    print(f"The factorial of {n2} is {result}")

if __name__ == "__main__":
    main()

