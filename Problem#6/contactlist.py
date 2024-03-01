def process_user_contacts(user_input):
    user_contacts = {}

    tokens = user_input.split()

    for i in range(0, len(tokens), 2):
        name, phone_number = tokens[i], tokens[i + 1]
        user_contacts[name] = phone_number

    contact_name = input("Enter the contact name: ")
    if contact_name in user_contacts:
        print(f"Phone number for {contact_name}: {user_contacts[contact_name]}")
    else:
        print(f"{contact_name} not found in the contact list.")

if __name__ == '__main__':
    user_input = input("Enter word pairs (name, phone number): ")

    process_user_contacts(user_input)
