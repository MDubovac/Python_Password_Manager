from db import *
from cipher import *

# Create a new record in the database
def create(website, password):
    check_website = f"SELECT website FROM passwords WHERE website='{website}'"
    my_cursor.execute(check_website)
    result_check_website = my_cursor.fetchall()

    if len(result_check_website) > 0:
        print("You already have a password for this website.")
    else:
        sql = f"INSERT INTO passwords (website, password) VALUES ('{website}', '{encrypt(password, 4)}')"
        my_cursor.execute(sql)
        db.commit()
        print("Password created successfully.")

# Read the database record
def read(website):
    sql = f"SELECT password FROM passwords WHERE website='{website}'"
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    for r in result:
        print(decrypt(r[0], 4))

# Update a record in database
def update(website, password):
    check_website = f"SELECT website FROM passwords WHERE website='{website}'"
    my_cursor.execute(check_website)
    result = my_cursor.fetchall()
    if len(result) > 0:
        sql = f"UPDATE passwords SET password='{encrypt(password, 4)}' WHERE website='{website}'"
        my_cursor.execute(sql)
        db.commit()
        print("Password updated successfully.")
    else:
        print("Record not found in database.")

# Delete a record in database
def delete(website):
    check_website = f"SELECT website FROM passwords WHERE website='{website}'"
    my_cursor.execute(check_website)
    result = my_cursor.fetchall()
    if len(result) > 0:
        sql = f"DELETE FROM passwords WHERE website='{website}'"
        my_cursor.execute(sql)
        db.commit()
        print("Password deleted succesfully.")
    else:
        print("Record not found in database.")