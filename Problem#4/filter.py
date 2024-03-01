def process_and_print(input_string):
    # Split the input string into separate strings
    numbers = input_string.split()

    # Convert strings to integers and filter out negative values
    nums = [int(number) for number in numbers if int(number) < 0]

    # Sort integers in reverse order
    nums.sort(reverse=True)

    # Print sorted integers
    for x in nums:
        print(x, end=' ')

if __name__ == "__main__":
    # User inputs a space-separated string of numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
