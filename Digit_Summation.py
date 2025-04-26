# Digit summation function.
def sum_of_digits(x):
    total = 0

    while x > 0:
        digit = x % 10 # Find the last digit of the number.
        total += digit # Add the number to the total
        x = x//10 # remove the last digit 
    return total

def main():
    #User input
    x = int(input("Enter a number: "))

    #Call the function and print the result
    result = sum_of_digits(x)
    print(f"The sum of the {x} is {result}")

if __name__ == "__main__":
    main()