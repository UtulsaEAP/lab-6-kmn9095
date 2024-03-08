def filter_and_print_range(input_list, min_val, max_val):
    # Initialize an empty list to store filtered integers
    filtered_numbers = []

    # Iterate through each number in the input list
    for number in input_list:
        # Check if the number is within the specified range
        if min_val <= number <= max_val:
            # Append the number to the filtered list
            filtered_numbers.append(number)

    # Print the filtered numbers separated by commas
    print(','.join(map(str, filtered_numbers)), end=',')

if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = [int(num) for num in user_input.split()]

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    min_val, max_val = map(int, user_input.split())

    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(integer_list, min_val, max_val)
