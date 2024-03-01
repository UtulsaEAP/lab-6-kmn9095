def process_input(input_string):
    # Split the input string into separate strings
    tokens = input_string.split()

    # Convert strings to floats
    nums = [float(token) for token in tokens]

    # Get the max and average
    max_value = max(nums)
    average_value = sum(nums) / len(nums)

    return max_value, average_value

if __name__ == "__main__":
    # User inputs a space-separated string of numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
