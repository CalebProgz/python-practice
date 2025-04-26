# sum_of_list fuction
def sum_of_list(lst):
    """
    This function takes a list of numbers as input and returns the sum of the numbers in the list.
    
    :param lst: List of numbers
    :return: Sum of the numbers in the list
    """
    total = 0
    for num in lst:
        total += num
    return total

# User input
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]  # Convert input strings to floats

if __name__ == "__main__":
    # Call the function and print the result
    result = sum_of_list(numbers)
    print(f"The sum of the list is: {result}")

