def check_palindrome(user_input):
    # Remove spaces and punctuation marks, and convert input to lowercase
    cleaned_input = ''.join(char.lower() for char in user_input if char.isalnum())

    # Check if the cleaned input is equal to its reverse
    if cleaned_input == cleaned_input[::-1]:
        print(f"palindrome: {user_input}")
    else:
        print(f"not a palindrome: {user_input}")

if __name__ == "__main__":
    user_input = input("Enter a word or phrase: ")
    check_palindrome(user_input)
