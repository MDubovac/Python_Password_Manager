from tkinter import *
from cipher import *
from db import *

root = Tk()
root.geometry('300x300')
root.title("Password Manager")

# User Data
user_label = Label(root, text="Username")
user_label.pack()

user_entry = Entry(root)
user_entry.pack()

# Password Data
pass_label = Label(root, text="Password")
pass_label.pack()

pass_entry = Entry(root, show="*")
pass_entry.pack()

# Login Function
def login():
    sql = f"SELECT * FROM master_user WHERE username='{user_entry.get()}' AND password='{encrypt(pass_entry.get(), 4)}'"
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    
    placeholder_msg = ''
    success = Label(root, text="Credentials are correct!", fg="green")
    err = Label(root, text="Credentials not correct", fg="red")
    
    if len(result) > 0:
        top = Toplevel(root)
        top.title("Actions")
        top.geometry('300x150')
        placeholder_msg = success

        # Actions window
        variable = StringVar(top)
        variable.set("Select Action") # default value
        
        e1 = OptionMenu(top, variable, 'Read Password', 'Create New Password', 'Update Password', 'Delete Password')
        e1.pack()

        def action():
            if variable.get() == 'Read Password':
                 # Selected Action Window
                read_win = Toplevel(top)
                read_win.title("Read Password")
                read_win.geometry('300x150')

                # Inside od the window
                website_to_read_lab = Label(read_win, text="Website to read the password for:")
                website_to_read_lab.pack()

                website_to_read_inp = Entry(read_win)
                website_to_read_inp.pack() 

                def read():
                    sql = f"SELECT password FROM passwords WHERE website='{website_to_read_inp.get()}'"
                    my_cursor.execute(sql)
                    result = my_cursor.fetchall()
                    if len(result) > 0:
                        for r in result:
                            r = decrypt(r[0], 4)
                            result_lab = Label(read_win, text=r, fg="blue")
                            result_lab.pack()
                    
                    else:
                        err_read = Label(read_win, text="That password does not exist.", fg="red")
                        err_read.pack()

                btn_read = Button(read_win, text="Read", command=read)
                btn_read.pack()


            elif variable.get() == "Create New Password":
                # Selected Action Window
                create_win = Toplevel(top)
                create_win.title("Create Password")
                create_win.geometry('300x200')
                
                # Inside the window
                website_to_create_lab = Label(create_win, text="Website To create the password for:")
                website_to_create_lab.pack()

                website_to_create_inp = Entry(create_win)
                website_to_create_inp.pack()

                password_to_create_lab = Label(create_win, text="Password:")
                password_to_create_lab.pack()

                password_to_create_inp = Entry(create_win, show="*")
                password_to_create_inp.pack()

                success_create = Label(create_win, text="Created Successfully.", fg="green")
                err_create = Label(create_win, text="You already have a password for this website.", fg="red")
                
                def create():
                    check_website = f"SELECT website FROM passwords WHERE website='{ website_to_create_inp.get()}'"
                    my_cursor.execute(check_website)
                    result_check_website = my_cursor.fetchall()

                    if len(result_check_website) > 0:
                        placeholder_msg_create = err_create
                        print("You already have a password for this website.")
                    else:
                        sql = f"INSERT INTO passwords (website, password) VALUES ('{website_to_create_inp.get()}', '{encrypt(password_to_create_inp.get(), 4)}')"
                        my_cursor.execute(sql)
                        db.commit()
                        placeholder_msg_create = success_create
                        print("Password created successfully.")
                    placeholder_msg_create.pack()

                btn_create = Button(create_win, text="Create", command=create)
                btn_create.pack()

            elif variable.get() == "Update Password":
                # Selected Action Window
                update_win = Toplevel(top)
                update_win.title("Update Password")
                update_win.geometry('300x200')

                # Inside the widnow
                website_to_update_lab = Label(update_win, text="Website to update the password for:")
                website_to_update_lab.pack()
                
                website_to_update_inp = Entry(update_win)
                website_to_update_inp.pack()

                password_to_update_lab = Label(update_win, text="New Password:")
                password_to_update_lab.pack()

                password_to_update_inp = Entry(update_win, show="*")
                password_to_update_inp.pack()

                success_update = Label(update_win, text="Password Updated Successfully.", fg="green")
                err_update = Label(update_win, text="Password doesn't exist.", fg="red")

                def update():
                    check_website = f"SELECT website FROM passwords WHERE website='{website_to_update_inp.get()}'"
                    my_cursor.execute(check_website)
                    result = my_cursor.fetchall()
                    if len(result) > 0:
                        sql = f"UPDATE passwords SET password='{encrypt(password_to_update_inp.get(), 4)}' WHERE website='{website_to_update_inp.get()}'"
                        my_cursor.execute(sql)
                        db.commit()
                        placeholder_msg_update = success_update
                    else:
                        placeholder_msg_update = err_update

                    placeholder_msg_update.pack()

                btn_update = Button(update_win, text="Update", command=update)
                btn_update.pack()

            elif variable.get() == "Delete Password":
                # Selected Action Window
                delete_win = Toplevel(top)
                delete_win.title("Delete Password")
                delete_win.geometry('300x150')

                # Inside the window
                website_to_delete_lab = Label(delete_win, text="Website to delete the password for:")
                website_to_delete_lab.pack()

                website_to_delete_inp = Entry(delete_win) 
                website_to_delete_inp.pack() 
                
                success_delete = Label(delete_win, text="Password deleted Successfully.", fg="green")
                err_delete = Label(delete_win, text="Password doesn't exist.", fg="red")

                def delete():
                    check_website = f"SELECT website FROM passwords WHERE website='{website_to_delete_inp.get()}'"
                    my_cursor.execute(check_website)
                    result = my_cursor.fetchall()
                    if len(result) > 0:
                        sql = f"DELETE FROM passwords WHERE website='{website_to_delete_inp.get()}'"
                        my_cursor.execute(sql)
                        db.commit()
                        placeholde_msg_delete = success_delete
                    else:
                        placeholde_msg_delete = err_delete

                    placeholde_msg_delete.pack()

                btn_delete = Button(delete_win, text="Delete", command=delete)
                btn_delete.pack()
            else:
                label_else = Label(top, text="Please select a valid action.")
                label_else.pack()
        
        b1 = Button(top, text="Confirm", command=action)
        b1.pack()


    else:
        placeholder_msg = err

    placeholder_msg.pack()

submit_button = Button(root, text="Submit", command=login)
submit_button.pack()

root.mainloop()