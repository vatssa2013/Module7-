"""
Args:
    user-menu driven: 1-6
Returns:
    Gives the user,the option to
     - delete an entry from the dictionary using name or username
     - lookup a username by name
     - Add a user information to the dictionary


Raises:
    ValueError : Raises an exception if the name/username is empty.


"""

from sortedcontainers import SortedDict


def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User based on name')
    print('4. Lookup a Phone Number')
    print('5. Quit')
    print('6. Remove a User based on username')
    print()


# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

# display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user
    try:
        menu_choice = int(input("Type in a number (1-5): "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        for x, y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x, y))

    # add an entry
    elif menu_choice == 2:
        print("Add User")
        try:
            name = input("Name: ")
            username = input("User Name: ")
            if not name:
                raise ValueError('empty string')
            elif not username:
                raise ValueError('empty sting')

        except ValueError:
            print("\n It cannot be empty")
        usernames[name] = username

    # remove an entry
    elif menu_choice == 3:
        print("Remove User based on name")
        name = input("Name: ")

        if name in usernames:
            del usernames[name]

    # view user name
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name: ")
        name = name.lower()
        s = list(name)
        s[0] = s[0].upper()
        print("list with first upper case letter for string with first letter as uppercase:", s)
        name = "".join(s)
        print("Converting the list back to string:", name)

        if name in usernames:
            x = name
            y = usernames[name]
            print("Lookup result is shown below".format())
            print("Name: {} \tUser Name: {} \n".format(x, y))
            # pass  # print the username
        else:
            # print username not found
            print("\n", "Username not found")

    # is user enters something strange, show them the menu
    elif menu_choice != 5:
        print_menu()
    elif menu_choice == 6:
        print("Remove User based on username")
        username = input("Username:")
        if username in usernames:
            # find the key
            print("key is:", name)
            # use that key to delete the dictionary entry
            del usernames[name]
