import mysql.connector
import requests
import json

# Connecting to the MySQL
db = mysql.connector.connect(user ='root', passwd = 'tester1', database='TEST')
cur = db.cursor() #invoke cursor function

# Queries' Definitions
qry_select = """select valid_to from stores where merchant = '%s';""" # Get date query
qry_update = "update stores set valid_to='%s' where merchant='%s'" # Update date query

# Extract URL and Store data from the CSV
raw_file = open('Test_URL.csv', 'rU')
for each in raw_file:
    line = each.split(",")
    store = line[0]
    URL = line[1].strip()

    print(store) # FOR DEBUGGING
    print(URL) # FOR DEBUGGING

    Input_File = requests.get(URL).content.decode('ASCII')  # Get JSON off the website

    if len(Input_File) > 40:

# PART I - JSON Date
        Valid_To_Data = json.loads(Input_File).get("valid_to")  # Load JSON into Python
        JSON_Date = Valid_To_Data[0:Valid_To_Data.index("T")]

# PART II - SQL Date
        cur.execute(qry_select % store)  # Executing date SQL query
        fet = cur.fetchone()
        SQL_Date = str(fet[0])

# Compare Results
        print(JSON_Date)
        print(SQL_Date) # FOR DEBUGGING

        if JSON_Date > SQL_Date:
            cur.execute(qry_update % (JSON_Date, store))
            db.commit()
            print('Updated')
        else:
            print('Data is up-to-date')

    else:
        print("Error")