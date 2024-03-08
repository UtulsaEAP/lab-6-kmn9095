def process_user_contacts(user_input):
    user_contacts = {}

    # Split the input by commas to get name-phone number pairs
    tokens = user_input.split(',')

    # Remove any leading/trailing whitespace from each token
    tokens = [token.strip() for token in tokens]

    # Iterate over the tokens to populate the dictionary
    for i in range(0, len(tokens), 2):
        name, phone_number = tokens[i], tokens[i + 1]
        user_contacts[name] = phone_number

    # Input the name to search for
    contact_name = input("Enter the contact name: ")

    # Output the corresponding phone number if found
    if contact_name in user_contacts:
        print(f"Phone number for {contact_name}: {user_contacts[contact_name]}")
    else:
        print(f"{contact_name} not found in the contact list.")

if __name__ == '__main__':
    user_input = input("Enter word pairs (name, phone number): ")

    process_user_contacts(user_input)
