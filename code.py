import csv
import mysql.connector as mysql

con = mysql.connect(host='localhost', user='root', password='123@123', database='Inventory')
cur = con.cursor()

cur.execute('''create table if not exists Product_List
(Product_ID int primary key, Product_Name varchar(90),
Category varchar(90), Qty int, Price int); ''')

cur.execute('''create table if not exists Supplier_List
(Supplier_ID int primary key, Supplier_Name varchar(90),
Address varchar(90), Contact_no int); ''')

cur.execute('''create table if not exists Pending_orders
(Product_Name varchar(90), Qty int); ''')

cur.execute('''create table if not exists Sales_report
(Sales_id int primary key, P_date date,
Item varchar(90), sales_date date,
sales int, Stock_left int, purchaseAmt int, SalesAmt int ); ''')


def prod_listadd():
    n = int(input('Enter the no of items would like to add: '))
    for i in range(n):
        f = open('F:\\Product_list.csv', 'a', newline='')
        writeitems = csv.writer(f)
        a = int(input("Product_ID:"))
        b = input("Product_Name:")
        c = input("Category:")
        d = int(input("Qty:"))
        e = int(input("Price:"))
        l = [a, b, c, d, e]
        writeitems.writerow(l)
        cur.execute('insert into Product_List values(%s,%s,%s,%s,%s)', (a, b, c, d, e))
        con.commit()
        f.close()
    print("Record added successfully")


def view_list():
    f = open('F:\\Product_list.csv', 'r')
    r = csv.reader(f)
    for i in r:
        print(i)
    cur.execute("select * from Product_List")
    data = cur.fetchall()
    for i in data:
        print(i)


def search_item():
    n = input("Enter Product Name or Price to search: ")
    cur.execute("select * from Product_List where Product_Name=%s or Price=%s", (n, n))
    data = cur.fetchall()
    for i in data:
        print(i)


def place_order():
    name = input("Enter Product Name to order: ")
    qty = int(input("Enter Quantity: "))
    cur.execute('insert into Pending_orders values(%s,%s)', (name, qty))
    con.commit()
    print("Order placed successfully")


def supplier():
    n = int(input('Enter number of suppliers to add: '))
    for i in range(n):
        a = int(input('Supplier_ID: '))
        b = input('Supplier_Name: ')
        c = input('Address: ')
        d = int(input('Contact_no: '))
        cur.execute('insert into Supplier_List values(%s,%s,%s,%s)', (a, b, c, d))
        con.commit()
    print("Supplier details added successfully")


def sales_report():
    sid = int(input('Sales_id: '))
    pdate = input('P_date (YYYY-MM-DD): ')
    item = input('Item: ')
    sdate = input('Sales_date (YYYY-MM-DD): ')
    sales = int(input('Sales: '))
    stock = int(input('Stock_left: '))
    pamt = int(input('PurchaseAmt: '))
    samt = int(input('SalesAmt: '))
    cur.execute('insert into Sales_report values(%s,%s,%s,%s,%s,%s,%s,%s)',
                (sid, pdate, item, sdate, sales, stock, pamt, samt))
    con.commit()
    print("Sales record added successfully")


# ---- Main Menu ----
while True:
    print('''
    ===== INVENTORY MANAGEMENT SYSTEM =====
    1. Add Product List
    2. View Product List
    3. Search Product
    4. Place Order
    5. Add Supplier Details
    6. Add Sales Report
    7. Exit
    ''')
    ch = int(input('Enter your choice: '))

    if ch == 1:
        prod_listadd()
    elif ch == 2:
        view_list()
    elif ch == 3:
        search_item()
    elif ch == 4:
        place_order()
    elif ch == 5:
        supplier()
    elif ch == 6:
        sales_report()
    elif ch == 7:
        print('Exiting...')
        break
    else:
        print('Invalid Choice, Try Again!')
