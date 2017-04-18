cur_list = [('Freshco', 'Compliments Dozen Large Grade A Eggs', Decimal('1.97'), '', ''), ('Freshco', 'Eggo Waffles or Pancakes 244-310 g Selected Varieties', Decimal('2.49'), '', ''), ('Freshco', 'Olivieri Filled Pasta 600-700 g Tre Stelle Parmigiano Reggiano, Grana Padano or Pecorino Romano 200 g', Decimal('5.99'), '', ''), ('Freshco', 'Cadbury Single Eggs 33-39 g', Decimal('0.88'), '', ''), ('Freshco', 'Cadbury Mini Eggs 200 g', Decimal('2.99'), '', ''), ('Loblaws', 'GRADE A LARGE WHITE EGGS', Decimal('1.97'), '', ''), ('Loblaws', 'KINDER SURPRISE EASTER PLUSH, EGG HUNT KIT OR MAXI SURPRISE, 116 -186 g', Decimal('10.99'), '', ''), ('Loblaws', "REESE OR HERSHEY'S PASTEL KISSES CHOCOLATE POUCH OR EGGS, 185-340 g", Decimal('3.99'), '', ''), ('Loblaws', "M&M'S MILK CHOCOLATE EGGS, 900 g", Decimal('15.99'), '', ''), ('Loblaws', 'TWIX OR SNICKERS SINGLE EGGS, 30-31 g', Decimal('1.29'), '', ''), ('Loblaws', 'CADBURY MINI EGGS, 745/943 g', Decimal('15.99'), '', ''), ('Loblaws', 'CARNABY SWEET CHOCOLATE SOLID EGGS, 300 G', Decimal('5.00'), '2/', 'less than 2 $2.99 ea.'), ('Loblaws', 'PC® FREE-RUN LARGE SIZE EGGS, dozen', Decimal('4.49'), '', ''), ('Loblaws', 'PARMIGIANO REGGIANO', Decimal('2.99'), '', '/100 g'), ('Loblaws', 'CINNAMON RAISIN, POPPY SEED OR SESAME EGG BREAD, 450-725 g', Decimal('2.99'), '', ''), ('Loblaws', 'T. MARZETTI VEGGIE DIPS, 340 g', Decimal('8.00'), '2/', 'or $4.39 ea.'), ('Loblaws', 'DARE BRETON, VINTA CRACKERS, VEGGIE CRISPS, 120-250 g OR GRISSOL CRISPY BAGUETTE SNACKS, 100-235 g', Decimal('5.00'), '2/', 'less than 2 $2.99 ea.'), ('Loblaws', "KELLOGG'S EGGO WAFFLES, 244-330 g OR SPECIAL K FLATBREAD SANDWICH, 190-232 g, KELLOGG'S RICE KRISPIES BARS, 160-200 g, POP-TARTS, 400 g OR NUTRI-GRAIN BARS, 175-295 g", Decimal('2.49'), '', ''), ('Bulkbarn', 'Foil Wrapped Eggs', Decimal('4.49'), '', 'lb. | 0.99/100g'), ('Bulkbarn', 'Jelly Bean Eggs', Decimal('2.15'), '', 'lb. | .48/100g'), ('Bulkbarn', "M&M's Speckled Eggs", Decimal('7.89'), '', 'lb. | 1.74/100g'), ('Bulkbarn', 'Peanut Butter or Caramel Eggs', Decimal('4.99'), '', 'lb. | 1.10/100g'), ('Bulkbarn', "Hershey's Eggies", Decimal('4.99'), '', 'lb. | 1.10/100g'), ('Bulkbarn', "Hershey's Reese's Peanut Butter Eggs", Decimal('7.79'), '', 'lb. | 1.72/100g'), ('Bulkbarn', "Hershey's Reese's Pieces Eggs", Decimal('6.49'), '', 'lb. | 1.43/100g'), ('Shoppers Drugmart', 'KINDER (110g), CADBURY (200g) MINI EGGS or HERSHEY EASTER CELLOS', Decimal('3.99'), '', 'each'), ('Shoppers Drugmart', 'CADBURY MINI CREME EGGS', Decimal('9.99'), '', 'each'), ('Shoppers Drugmart', 'KINDER SURPRISE EGG HUNT KIT (186g) or MAXI EASTER EGG', Decimal('9.99'), '', 'each'), ('Shoppers Drugmart', 'FERRERO ROCHER, FERRERO COLLECTION EGG or RABBIT CHOCOLATES', Decimal('8.99'), '', 'each'), ('Shoppers Drugmart', 'LINDT GOLD BUNNY (200g), EASTER EGGS (198g) or MINI EGGS (300g)', Decimal('9.99'), '', 'each'), ('Shoppers Drugmart', "CADBURY L'IL SCOOPS (136g) or KINDER MINI EGGS (110g)", Decimal('4.99'), '', 'each'), ('Shoppers Drugmart', 'PC MINI EGGS 200g', Decimal('2.49'), '', 'each'), ('Shoppers Drugmart', "LINDT EGGS (6's) or EASTER GIFT BOX", Decimal('7.99'), '', 'each'), ('Shoppers Drugmart', 'CADBURY CREME EGGS', Decimal('3.49'), '', 'each')]
brand_list = ['EGGO', 'KINDER', 'PC®', 'KELLOGG\'S', 'HERSHEY\'S', 'NEILSON', 'IÖGO', 'LIBERTÉ', 'YOPLAIT', 'SEALTEST', 'TRUTASTE', 'DANONE', 'ACTIVIA', 'LINDT']


for each in cur_list:
    keywords = each[1].upper()
    for brand in brand_list:
        keywords = keywords.replace(brand,"")
    # print(keywords)
    keywords = " ".join(keywords.split())
    print(each[1])
    print(keywords)

## --- EXPERIMENTAL ZONE ---

# from datetime import date, datetime
# # from datetime import datetime
#
# text1 = date.today().isocalendar() [1]
# text2 = date.today()
# print(text2)
#
# text3 = '2017-01-02'
# print(text3)
#
# print(type(text2))
# print(type(text3))
#
# text4 = datetime.strptime(text3, '%Y-%m-%d')
# print(text4)
# print(type(text4))
#
# result1 = text4.isocalendar() [1]
# result2 = text4.isocalendar() [0]
# print(text1)
# print(result1)
# print(result2)

## -- For Loops Test --

# import requests
# import json
#
# for i in range(1,10):
#
#     # print(i)
#
#     y = "http://ca.flipp.com/d/flyer_data/shoppersdrugmart-flyer?flyer_run_id=21089"+str(i)+"&p=caflipp"
#     # print(y)
#
#     Input_File = requests.get(y).content.decode('ASCII')  # Get JSON off the website
#     JSON_Data = json.loads(Input_File)  # Load JSON into Python
#
#     # print(type(JSON_Data))
#
#     with open("NoFrillsTest"+str(i)+".csv", 'w') as fp:
#         json.dump(JSON_Data, fp)

## -- For Normal URLs --

# import requests
# import json
#
# y = "http://ca.flipp.com/d/flyer_data/shoppersdrugmart-flyer?flyer_run_id=210896&p=caflipp"
#
# Input_File = requests.get(y).content.decode('ASCII')  # Get JSON off the website
# Items_Data = json.loads(Input_File)  # Load JSON into Python
# JSON_Data = Items_Data.get("items")
#
# # print(type(JSON_Data))
#
# with open("JSON Test Shoppers.csv",'w') as fp:
#     json.dump(JSON_Data, fp)



# y = "this is good you know, you know what I mean"
# x = ["is good" , "what I", ","]
#
# for words in x:
#     y = y.replace(words,'')
# v = " ".join(y.split())
# print(v)
#
#
#
# # new = y.replace(x,"")
# # newer = new.replace("  "," ")
#
