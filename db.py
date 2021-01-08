# In Order for this app to work, you will need to modify this file
# You should enter valid data here instead of the placeholders
# Example:
#  host = "localhost"
#  user = "root"
#  password = "123456"
#  database = "app_db"

import mysql.connector

db = mysql.connector.connect(
    host = "HOST_NAME",
    user = "USER_NAME",
    password = "PASSWORD",
    database = "DATABASE_NAME"
)

my_cursor = db.cursor()
