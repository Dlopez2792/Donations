def login(database, username, password):
    # database = dict username and password = string
    if username in database:
        if password == database[username]:
            print("Welcome back", username + "!\n")
            return username
        print("Incorrect password for", username)
        return ""

    print("Failure to login. Please try again.")
    return ""


def register(database, username):
    if username in database:
        print("\nUsername already registered.")
        return ""
    print("\nUsername", username, "registered")
    return username


def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    donation_string = print("\n" + username, "donated $" + donation_amt)
    print("Thank you!")
    return donation_string
