import mysql.connector
import requests
import json

Line_Num = 0

# Connecting to the MySQL
db = mysql.connector.connect(user ='root', passwd = 'tester1', database='TEST')
cur = db.cursor() #invoke cursor function

# Queries' Definitions
qry_select = """select valid_to from stores where merchant = '%s';""" # Get date query
qry_update = "update stores set valid_to='%s' where merchant='%s'" # Update date query
qry_insert = """INSERT INTO db_april_9 (flyer_item_id, flyer_id, flyer_type_id, merchant_id, brand, display_name, description,\
current_price, pre_price_text, price_text, run_item_id, discount_percent, display_type, in_store_only, large_image_url,\
x_large_image_url, dist_coupon_image_url, sku, valid_to, valid_from, disclaimer_text, flyer_type_name_identifier,\
flyer_run_id, sale_story) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
%s, %s, %s, %s)"""

# Extract URL and Store data from the MySQL
cur.execute("select merchant, flier_url from stores")  # Executing date SQL query
URL_List = cur.fetchall()

for i in URL_List:
    store = (i[0])
    URL = (i[1])


# # Extract URL and Store data from the CSV
# raw_file = open('Test_URL.csv', 'rU')
# for each in raw_file:
#     line = each.split(",")
#     store = line[0]
#     URL = line[1].strip()

    # print(store) # FOR DEBUGGING
    # print(URL) # FOR DEBUGGING

    Input_File = requests.get(URL).content.decode('ASCII')  # Get JSON off the website
    if len(Input_File) > 40:
        Input_Data = json.loads(Input_File)  # Load JSON into Python


# PART I  - Getting JSON Date
        Valid_To_Data = Input_Data.get("valid_to")  # Load JSON into Python
        JSON_Date = Valid_To_Data[0:Valid_To_Data.index("T")]

# PART II - Getting SQL Date
        cur.execute(qry_select % store)  # Executing date SQL query
        fet = cur.fetchone()
        SQL_Date = str(fet[0])

# Compare Results
#         print(JSON_Date)
#         print(SQL_Date) # FOR DEBUGGING

        if JSON_Date > SQL_Date:
            cur.execute(qry_update % (JSON_Date, store))
            db.commit()
            print(store + ' updated')

            #! Writting Insert Code !
            ## CODE FOR KEEPING TRACK OF THE SOURCES ##
            qry = "INSERT INTO db_april_9 (brand) VALUES (\"" + URL + "\")"
            cur.execute(qry)  # Keeping track of the source
            db.commit()

            Items_Data = Input_Data.get("items")  # Select only Items dictionary

            for each in Items_Data:
                # Line_Num += 1 #IMPORT CONTROL LINE (1 out of 3)
                if Line_Num != 345 or Line_Num != 346 or Line_Num != 347:  # IMPORT CONTROL LINE (2 out of 3) #You want to import only specific lines

                    # ##DEBUGGING## - Best when used with Line Num
                    # print(Line_Num)
                    # print(each)

                    values = (each.get('flyer_item_id'), each.get('flyer_id'), each.get('flyer_type_id'), \
                              each.get('merchant_id'), each.get('brand'), each.get('display_name'),
                              each.get('description'), \
                              each.get('current_price'), each.get('pre_price_text'), each.get('price_text'),
                              each.get('run_item_id'), \
                              # Problem: it cannot run each.get('category_ids')
                              each.get('discount_percent'), each.get('display_type'), each.get('in_store_only'), \
                              each.get('large_image_url'), each.get('x_large_image_url'),
                              each.get('dist_coupon_image_url'), \
                              each.get('sku'), each.get('valid_to'), each.get('valid_from'),
                              each.get('disclaimer_text'), \
                              each.get('flyer_type_name_identifier'), each.get('flyer_run_id'), each.get('sale_story'))
                    cur.execute(qry_insert, values)
                    db.commit()  # commits the result
                    # Line_Num = 0 #IMPORT CONTROL LINE (3 out of 3) # Reset the counter to work with the new URL
                else:
                    break

        else:
            print(store + ' data is up-to-date')

    else:
        print("No data for "+store)

