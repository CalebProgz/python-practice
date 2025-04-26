# Function for reversing a String
def string_reversal(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

def main():
    # User input for string reversal
    input_string = input("Enter a string to reverse: ")
    reversed_string = string_reversal(input_string)
    print(f"\nOriginal String: {input_string}")
    print(f"Reversed String: {reversed_string}")

if __name__ == "__main__":
    main()

