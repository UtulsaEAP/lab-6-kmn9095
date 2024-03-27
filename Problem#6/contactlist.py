'''
Kelsey Nocck
3/27/24
'''

def process_user_contacts(user_input):
    current_contact = []
    user_input = user_input.split(" ")
    dictionary = {}

    for i in range(0, len(user_input), 1):
        current_contact = user_input[i].split(",")
        dictionary.update({current_contact[0]:current_contact[1]})
    
    search_name = input("Enter contact name: ")
    print(dictionary.get(search_name))
   

if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")
    # Call the function to process user contacts
    process_user_contacts(user_input)