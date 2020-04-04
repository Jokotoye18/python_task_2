import random
first_name = input("Enter your first name :: ")
first_name = first_name.capitalize()
last_name = input("Enter your last name :: ")
last_name = last_name.capitalize()
email = input("Enter your email address here, e.g janedove@gmail.com :: ")

def get_first_two_char(name):
    char = first_name[:2]
    return str(char)
def get_last_two_char(name):
    reverse = last_name[::-1]
    char = reverse[:2]
    return str(char)

random_str = []
string = list("abcdefghijklmnopqrstvwxyz")
for i in range(0,5):
    char = random.choice(string)
    random_str.append(char)


random_str = ''.join(random_str)
first_two_char = get_first_two_char(first_name)
last_two_chr = get_last_two_char(last_name)

user_password = (first_two_char + last_two_chr + random_str)
user_password = list(user_password)
random.shuffle(user_password)
user_password = ''.join(user_password)

print("Hello %s %s your password is '%s'." % (first_name, last_name, user_password))
prompt = input("Are you satisfy with the password generated? Enter 'yes' to accecpt and 'no' to reject and set one for yourself :: ")
prompt = prompt.lower()
user_data = {}

if prompt == "yes":
    user_data[last_name] = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": user_password,
    }
    print(user_data)
else:
    def get_new_password():
        character = input("Enter your new password! Ensure it has up to '7' characters :: ")
        if len(character) < 7:
            print("Your new password should be greater than or equal to '7' characters")
            return get_new_password()
        else:
            return character

    new_password = get_new_password()
    user_data[last_name] = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": new_password,
    }
    print(user_data)