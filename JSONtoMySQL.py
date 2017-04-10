import requests
import json
import mysql.connector

Line_Num = 0

#Connecting to the MySQL
db = mysql.connector.connect(user ='root', passwd = 'tester1', database='TEST')
cur = db.cursor() #invoke cursor function

#The SQL query we are applying to work with our DB
query = """INSERT INTO db_april_3 (flyer_item_id, flyer_id, flyer_type_id, merchant_id, brand, display_name, description,\
current_price, pre_price_text, price_text, run_item_id, discount_percent, display_type, in_store_only, large_image_url,\
x_large_image_url, dist_coupon_image_url, sku, valid_to, valid_from, disclaimer_text, flyer_type_name_identifier,\
flyer_run_id, sale_story) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
%s, %s, %s, %s)"""

#Read from the list of website to connect to
raw_file = open('Test_URL.csv', 'rU')
for each in raw_file:
    line = each.split(",")
    store = line[0]
    URL = line[1].strip()

    if URL != "<END>":

        ###DEBUGGING##
        # print(URL)
        # print(type(URL))

        # input_file = open("output/Sample.json", 'r').read()   #Get JSON off HDD
        Input_File = requests.get(URL).content.decode('ASCII') #Get JSON off the website
        JSON_Data = json.loads(Input_File)                     #Load JSON into Python
        Items_Data = JSON_Data.get("items")                    #Select only Items dictionary

        # #To find out what type of data it is - Dictionary or List
        # print(type(JSON_Data))

        ## CODE FOR KEEPING TRACK OF THE SOURCES ##
        qry = "INSERT INTO db_april_3 (brand) VALUES (\""+URL+"\")"
        cur.execute(qry) #Keeping track of the source
        db.commit()

        for each in Items_Data:
            # Line_Num += 1 #IMPORT CONTROL LINE (1 out of 3)
            if Line_Num != 345 or Line_Num != 346 or Line_Num != 347: #IMPORT CONTROL LINE (2 out of 3) #You want to import only specific lines

                # ##DEBUGGING## - Best when used with Line Num
                # print(Line_Num)
                # print(each)

                values = (each.get('flyer_item_id'), each.get('flyer_id'), each.get('flyer_type_id'),\
                    each.get('merchant_id'), each.get('brand'), each.get('display_name'), each.get('description'),\
                    each.get('current_price'), each.get('pre_price_text'), each.get('price_text'), each.get('run_item_id'), \
                    # Problem: it cannot run each.get('category_ids')
                    each.get('discount_percent'), each.get('display_type'), each.get('in_store_only'), \
                    each.get('large_image_url'), each.get('x_large_image_url'), each.get('dist_coupon_image_url'), \
                    each.get('sku'), each.get('valid_to'), each.get('valid_from'), each.get('disclaimer_text'), \
                    each.get('flyer_type_name_identifier'), each.get('flyer_run_id'), each.get('sale_story'))
                cur.execute(query, values)
                db.commit()  # commits the result
        # Line_Num = 0 #IMPORT CONTROL LINE (3 out of 3) # Reset the counter to work with the new URL
    else:
        break