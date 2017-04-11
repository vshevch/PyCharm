import csv
import mysql.connector
from datetime import datetime

# Declare Variables

wk = str(datetime.now().isocalendar()[1])
list = [] #Define list variable

# MySQL Database Connection Settings

db = mysql.connector.connect(user ='root', passwd = 'tester1', database='TEST')
cur = db.cursor() #invoke cursor function

# Get items off Shopping List

raw_file = open('Shopping List.csv', 'rU')
for line in raw_file:
    split_line = line.split(",")
    #Ensure you have only unique items in the list
    if split_line[0] not in list:
        list.append(split_line[0].strip())
print(list)

# --- DATA OUTPUT ---

# # WAY 1: Number of discounts per item
# for item in list:
#     query = "SELECT * FROM db_march_6 WHERE UPPER(display_name) LIKE '%" + item + "%'"
#     cur.execute(query)
#     results = cur.fetchall()
#
#     # print(cur.rowcount)
#     print('%s %d' % (item,cur.rowcount)) #%s - string, %d - integer

# WAY 2: Shows the discount

# Declare Output Notebook
write_to = open('Shopping List Output.csv', "w", newline="")
FileWriter = csv.writer(write_to)
FileWriter.writerow(('Item','Merchant','Description','Price','Pre-Price Text','Price Text'))
write_to.close()

# Look-up items against the MySQL Database

for item in list:
    # print(item)
    query = ("""select t1.merchant, t2.display_name, t2.current_price, t2.pre_price_text, t2.price_text \
    from stores t1 INNER JOIN db_wk_%s t2 ON t1.merchant_id = t2.merchant_id WHERE UPPER(display_name) LIKE '%%%s%%'"""
    % (wk, item))

    cur.execute(query)
    cur_list = cur.fetchall()

# Write Items to Output Notebook

    if(len(cur_list)) == 0:
        with open('Shopping List Output.csv', "a", newline="") as File:
            FileWriter = csv.writer(File)
            None_String = [item,'---','No Discounts']
            FileWriter.writerow(None_String)
    else:
        for each in cur_list:
            input_line = [item]
            input_line.extend(each)
            with open('Shopping List Output.csv', "a", newline="") as File:
                FileWriter = csv.writer(File)
                FileWriter.writerow(input_line)