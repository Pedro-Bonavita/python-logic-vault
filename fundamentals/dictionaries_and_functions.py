import getpass

# Initialize an empty dictionary for our users
users = {}

def register():
    new_username = input('Enter new username: ')
    new_password = input('Enter password: ')

    #Adding to the dictionary
    users[new_username] = new_password
    print('User registered successfully!')

def admin_panel():
    print ('\n--- Admin Panel ---')
    print ('1 - View registered usernames')
    print ('2 - View registered passwords')
    print ('3 - View all users and passwords')
    print('4 - Return to ogin menu')

    admin_choice = input('Select an option: ')
    if admin_choice =='1':
        print(users.keys())
    elif admin_choice =='2':
        print(users.values())
    elif admin_choice =='3':
        print(users.items())
    elif admin_choice =='4':
        return
    else:
        print('Option not found.')

def login():
    username = input('Username: ')
    password = getpass.getpass('Password: ')

    if username in users and users[username] == password:
        print('Login successful!')
        if username =='admin':
            admin_panel()
    elif username =='admin' and password == 'admin123':
        admin_panel()
    else:
        print('Invalid username or password')

#System Excecution
while True:
    print('\n1 - Register new user')
    print('2 - Login')
    print('0 - Exit system')

    choice = input('Select an option: ')

    if choice =='1':
        register()
    elif choice =='2':
        login()
    elif choice == '0':
        print ("System closed.")
    else:
        print("Invalid choice.")
