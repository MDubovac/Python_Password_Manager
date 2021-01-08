from crud import create, read, update, delete
from db import my_cursor

# Master username and password
check_username = input("Enter username: ")
check_password = input("Enter the master password: ")

# Check if user exists
sql = f"SELECT * FROM master_user WHERE username='{check_username}' AND password='{check_password}'"
my_cursor.execute(sql)
result = my_cursor.fetchall()

# If user Exists, Print Welcome message and star the app
if len(result) > 0:
    print("____________________________")
    print("----------- Menu -----------")   
    print("1.Create a new password.")    
    print("2.Read a specific password.")     
    print("3.Update a password.")    
    print("4.Delete a password.")    
    print("5.Quit.\n") 

    # User enters wanted action
    # 1 - To Create a new Password
    # 2 - To Read selected Password
    # 3 - To Update selected Password
    # 4 - To Delete selected Password
    # 5 - To Exit The Application
    
    choice = input("Enter the number of the operation you would like to perform: ")   

    if choice == "1":
        website_to_create = input("\nEnter the website for which you want the password to be created: ")
        password_to_create = input("Enter the password: ")
        create(website_to_create, password_to_create)
    elif choice == "2":
        website_to_read = input("\nEnter the name of the website: ")
        read(website_to_read)
    elif choice == "3":
        website_to_update = input("\nEnter the website for which you want the password to be updated: ")
        password_to_update = input("Enter the new password: ")
        update(website_to_update, password_to_update)
    elif choice == "4":
         website_to_delete = input("\nEnter the website for which you want the password to be deleted: ")
         delete(website_to_delete)
    elif choice == "5":
        print("Goodbye!")
        quit()
else:
    print("Wrong username or password.")
    quit()
