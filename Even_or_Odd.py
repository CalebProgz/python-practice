# Even/Odd function
def even_or_odd(n1):
    if n1 % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# User input
def main():
    n1 = int(input("Enter a number: "))
    result = even_or_odd(n1)
    print(f"The number {n1} is {result}.")
    
if __name__ == "__main__":
    main()

