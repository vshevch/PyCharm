import csv

import mysql.connector
db = mysql.connector.connect(user ='root', passwd = 'tester1', database='TEST')
cur = db.cursor() #invoke cursor function

list = [] #Define list variable
raw_file = open('Shopping List.csv', 'rU')
for line in raw_file:
    split_line = line.split(",")
    #Ensure you have only unique items in the list
    if split_line[0] not in list:
        list.append(split_line[0].strip())
print(list)

# #WAY 1: Number of discounts per item
# for item in list:
#     query = "SELECT * FROM db_march_6 WHERE UPPER(display_name) LIKE '%" + item + "%'"
#     cur.execute(query)
#     results = cur.fetchall()
#
#     # print(cur.rowcount)
#     print('%s %d' % (item,cur.rowcount)) #%s - string, %d - integer

#WAY 2: Shows the discount
# list = ['Eggs'] #FOR DEBUGGING

write_to = open('Shopping List Output.csv', "w", newline="")
FileWriter = csv.writer(write_to)
FileWriter.writerow(('Item','Merchant','Description','Price','Pre-Price Text','Price Text'))
write_to.close()

for item in list:
    # print(item)
    query =  """select stores.merchant, db_march_6.display_name, db_march_6.current_price, db_march_6.pre_price_text, \
    db_march_6.price_text from stores INNER JOIN db_march_6 ON stores.merchant_id = db_march_6.merchant_id \
    WHERE UPPER(display_name) LIKE '%""" + item + "%';"

    cur.execute(query)

    for each in cur:
        input_line = [item]
        input_line.extend(each)
        # print(input_line)
        with open('Shopping List Output.csv', "a", newline="") as File:
            FileWriter = csv.writer(File)
            FileWriter.writerow(input_line)

    results = cur.fetchall()
    list_final.append(results)
# print(list_final)
#     # print(cur.rowcount)



