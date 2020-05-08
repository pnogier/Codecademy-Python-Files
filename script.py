# Are you there? We’ve opened up a communications link to The Fender‘s
# secret computer. We need you to write a program that will read in the
# compromised usernames and passwords that are stored in a file called
# "passwords.csv".

import csv  # Import the csv module to work with csv files
import json  # Import the json module to work with json files

compromised_users = []  # New list to stock compromised users

# Open password.csv file in read mode as password_file file object
with open("passwords.csv") as password_file:
    # Parse the file object using the csv.DictReader() method
    password_csv = csv.DictReader(password_file)
    for row in password_csv:  # Loop through each lines of the csv file
        password_row = row  # Setting row to temporary variable password_row
        # Add each compromised username to our compromised_users list
        compromised_users.append(password_row["Username"])
    # We could also have used a list comprehension :
    # compromised_users = [row["Username"] for row in password_csv]

# Open compromised_users.txt file in write mode as compromised_users_file
with open("compromised_users.txt", "w") as compromised_users_file:
    for user in compromised_users:  # Loop through users in compromised_users
        # Add each user to our txt file
        compromised_users_file.write(user + '\n')


# Your boss needs to know that you were successful in retrieving that
# compromised data. We’ll need to send him an encoded message over the
# internet.
# Let’s use JSON to do that.

# Open boss_message.json file in write mode as boss_message
with open("boss_message.json", "w") as boss_message:
    boss_message_dict = {  # Create a dictionnary that relays a Boss message
        "recipient": "The Boss",
        "message": "Mission Success"
    }
    # Use the json.dump() method to write in our json file
    json.dump(boss_message_dict, boss_message)

# Now that we’ve safely recovered the compromised users
# we’ll want to removethe "passwords.csv" file completely.

# Open new_passwords.csv file in write mode as new_passwords file object
with open("new_passwords.csv", "w") as new_passwords_obj:
    # Enemy of the people, Slash Null, is who we want The Fender to think was
    # behind this attack. He has a signature, whenever he hacks someone he adds
    # this signature to one of the files he touches.
    slash_null_sign = """
         _  _     ___   __  ____             
        / )( \   / __) /  \(_  _)            
        ) \/ (  ( (_ \(  O ) )(              
        \____/   \___/ \__/ (__)             
        _  _   __    ___  __ _  ____  ____  
        / )( \ / _\  / __)(  / )(  __)(    \ 
        ) __ (/    \( (__  )  (  ) _)  ) D ( 
        \_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \`
(___)  \___ \/ (_/\/    \\\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
        __ _  _  _  __    __                
        (  ( \/ )( \(  )  (  )               
        /    /) \/ (/ (_/\/ (_/\             
        \_)__)\____/\____/\____/
    """
    new_passwords_obj.write(slash_null_sign)
    print(slash_null_sign)
