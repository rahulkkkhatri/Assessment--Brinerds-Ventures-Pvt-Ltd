import datetime
import random
import string

product = {
    1: {
    "product_id" : "2441",
    "product_name": "Levis_pant",
    "product_price": 3500
    },
    2: {
    "product_id" : "2442",
    "product_name": "Levis_shirt",
    "product_price": 2500
    },
    3: {
    "product_id" : "2443",
    "product_name": "Nike_tshirt",
    "product_price": 2000
    },
    4: {
    "product_id" : "2444",
    "product_name": "Puma_shoes",
    "product_price": 3800
    },
    5: {
    "product_id" : "2445",
    "product_name": "Adidas_shoes",
    "product_price": 3700
    },
    6: {
    "product_id" : "2446",
    "product_name": "Nike_shoes",
    "product_price": 4500
    },
    7: {
    "product_id" : "2447",
    "product_name": "Fossil_watch",
    "product_price": 5200
    },
    8: {
    "product_id" : "2448",
    "product_name": "Tommy_watch",
    "product_price": 3499
    },
    9: {
    "product_id" : "2449",
    "product_name": "DW_watch",
    "product_price": 3000
    },
    10: {
    "product_id" : "2450",
    "product_name": "Titan_watch",
    "product_price": 2500
    }
}

Customer_id = []
for i in range(50):
    Customer_id.append(''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=7)))

ref_date = datetime.datetime(2022, 3, 16)

files = ["test1.csv","test2.csv","test3.csv"]

for file in files:
    
 
    f = open(file,'a')
    f.write("order_id,customer_id,order_date,product_id,product_name,product_price,quantity")
    for i in range(1,101):
        order_id = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=7))
        num = random.randint(0,len(Customer_id)-1)
        random_day_diff = random.randint(1,365)
        product_num = random.randint(1,4)
        order_date = ref_date+datetime.timedelta(random_day_diff)
        date_str = order_date.strftime('%m/%d/%Y')
        record_str = "\n"+order_id+",cust_"+Customer_id[num]+","+date_str+","+product[product_num]['product_id']+","+product[product_num]['product_name']+","+str(product[product_num]['product_price'])+","+str(product_num)
        f.write(record_str)

    f.close()

f1 = open("order.csv",'a')
f1.write("order_id,customer_id,order_date,product_id,product_name,product_price,quantity")
for i in range(1,1000001):
    order_id = ''.join(random.choices(string.ascii_lowercase +
                            string.digits, k=7))
    num = random.randint(0,len(Customer_id)-1)
    random_day_diff = random.randint(1,365)
    product_num = random.randint(1,4)
    order_date = ref_date+datetime.timedelta(random_day_diff)
    date_str = order_date.strftime('%m/%d/%Y')
    record_str = "\n"+order_id+",cust_"+Customer_id[num]+","+date_str+","+product[product_num]['product_id']+","+product[product_num]['product_name']+","+str(product[product_num]['product_price'])+","+str(product_num)
    f1.write(record_str)

f1.close()

