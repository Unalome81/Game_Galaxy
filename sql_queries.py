import mysql.connector
connection = mysql.connector.connect(host="localhost", user='root', database='game_galaxy', password='fortune')
mycursor = connection.cursor()

# Return status ->
# 0 for success , 1 for user already exists , else something wrong 
def Registration_SQL(first_name, last_name, mobile, dob, email, password):
    query = "select customer_id from customer order by customer_id desc limit 1"
    mycursor.execute(query)
    z=mycursor.fetchall()
    for i in z:
        string=i[0]
        conv_string=string[0]
        conv_integer=int(string[1:])
    cust_id=conv_string+'0'+str(conv_integer+1)
    mycursor.execute('select email from customer')
    check_email=mycursor.fetchall()
    for i in check_email:
        if email in i:
            return 1
        
        elif email not in i:
            values1=(cust_id,first_name,last_name,mobile,email,dob)
            query="insert into customer (customer_id,firstname,lastname,phoneno,email,dob) values(%s,%s,%s,%s,%s,%s)"
            mycursor.execute(query,values1)
            values2=cust_id,email,password
            query2="insert into authentication(customer_id,emaill,customer_password) values(%s,%s,%s)"
            mycursor.execute(query2,values2)
            return 0
    

# Return three things -> status, customerid, user_first_name (if found)
# 0 for success , 1 for email doesn't exist, 2 for wrong password, or else retry
def Find_Customer_SQL(email, password):
    # q=find email in authentication
    # if len(q)==0:
    # return 1, Nonw, None
    # else:
    # if(passsword==q[password]):
    # q= find customer_id, firstname in customer where email = email
    # return 0 , q[customer_id], q[firstname]
    # else:
    # return 2 ,none, none
    
    email_query = "select 1 from authentication where email = %s"
    mycursor.execute(email_query, (email,))
    results = mycursor.fetchone()

    password_query="select 1 from authentication where email= %s and customer_password = HEX(AES_ENCRYPT(%s, 'project'))"
    mycursor.execute(password_query, (email,password,))
    results2=mycursor.fetchone()

    que = "select customer_id,firstname from customer where email = %s"
    mycursor.execute(que, (email,))
    results3 = mycursor.fetchall()
    
    for j in results3:
        customer_id=j[0]
        first_name=j[1]

    if results and results2:
        return 0, customer_id, first_name

    elif results is None:
        return 1 , None, None

    elif results2 is None:
        return 2 , None, None

    else:
        return -1, None, None
     
# Return max_price, min_price of available stock  (all possible games)
def Price_Range_SQL():
    query = "SELECT MIN(price) AS min_price, MAX(price) AS max_price FROM game"
    mycursor.execute(query)
    result = mycursor.fetchone()
    mn = result[0]
    mx = result[1]
    return mn, mx


# Return a list of dictionary where each entry is an avilable games which satisfies these filters, rating_filter: 1-10, price_filter_min: min price, price_filter_max: max price, genre_filter = "*" for all
# Note that dictionary is nothing but record-> d['game']=(game name), d['game_id']= (game id of the entry), etc d{atribute}->value 
# Print games with these filters: min_rating_filter: rating should be above this, price_filter: min ,max, genre_filter: = "*" for all list of things user likes
def Show_Games_SQL(rating_filter, price_filter_min, price_filter_max, genre_filter):
    mycursor=connection.cursor()
    query = "select * from game where rating >= %s and price <= %s and price >=%s"
    params = [rating_filter, price_filter_min,price_filter_max]
    if genre_filter != "*":
        query += " and genre = %s"
        params.append(genre_filter)
    mycursor.execute(query, tuple(params))
    results = mycursor.fetchall()
    games = []
    for row in results:
        game = {'game_id': row[0], 'title': row[1],'genre': row[2],'price': row[3],'rating': row[4],'release_date': row[5],'game_description': row[6],'developer': row[7]}
        games.append(row)
    return games


# cart is  a list of tuples ->(gid, gname, quantity)
def Load_cart_SQL(cid):
    mycursor = connection.cursor()
    query = 'select cart.game_id, game.title, cart.quantity from cart join game on cart.game_id = game.game_id where cart.customer_id = %s'
    mycursor.execute(query, (cid,))
    results = mycursor.fetchall()
    for i in results:
        return i
        
# cart is  a list of tuples ->(gid, gname, quantity)
def Dump_cart_SQL(cid, cart):  #NOT CHECKED
    # Delete all entries from the cart (data bas )where cutomer _id =cid
    mycursor = connection.cursor()
    mycursor.execute("delete FROM cart WHERE customer_id = %s", (cid,))
    ex = mycursor.fetchall()
    
    # Add all entries from the cart (cart) to the cart (data base) with customer_id = cid
    for i in cart:
        values=cid, i[0], i[2]
        query="INSERT INTO cart (customer_id, game_id, quantity) VALUES (%s, %s, %s)"
        mycursor.execute(query,values)
    
    connection.commit()

def Check_Wallet_Balance_SQL(cid,wid):
    mycursor = connection.cursor()
    query = "SELECT balance FROM wallet WHERE Customer_ID = %s"
    mycursor.execute(query, (cid,))
    result = mycursor.fetchone()
    return result

# check if bought
def checkbought(cid,game_id):

# if found overwrite it -> reclculate overall rating ,else add ,  rev_count ++ and recalculate overall rating 
def modifyRating(cid,game_id,rating_filter,rvw):

# if rating found remove it , if found recalculate overall rating 
def RemnoveRating(cid,game_id):


# find ratings in this form list of -> (cname_first+" "+c_name_last,game rating given, game reviwe)
def findRatings_bygid_SQL(game_id):


# fid ratings in this form list of -> (gid, game-name,game rating given, game reviw) of cid
def findRatings_bycid_SQL(cid):

def remove_adress(cid,adr_id):

def remove_wallet(cid,walet_id):

# Returns -> (order_id,order_status,total_price,transaction_id,w_id,addr_id,item_list)
# item_list -> list of (game_id, quantity)
def Get_Customer_Orders(cid):

# return (Game Name, found) found-> bool yes or no
def findgame_SQL(game_id):

# returns nothing
# item_list -> list of (game_id, quantity)
    # Node this should update bought relation as well
def log_order(cid,order_status,total_price,transaction_id,item_list,w_id,addr_id):

# return total of cart
def Calculate_Total_Price_SQL(cid, cart):
    p=0
    for i in cart:
        query = "SELECT price FROM game WHERE game_id = %s"
        mycursor.execute(query, (i[0],))
        result = mycursor.fetchone()
        p += result[0] * i[2]
    return p

# return balance of wid
def Check_Wallet_Balance_SQL(cid,wid):
    


    # add money to wallet wid of cid ->+ amt to add
def Payment_SQL(cid, wid, amount_to_add):

# Returns the transaction id and log a transaction 
    # a success transaction
    # does entry to table and cuts the amt from wallet
def Transaction_SQL(cid, wid, total_price):

# Returns the transaction id and log a transaction 
    # a un-success transaction bad boy
def log_unsuccessfull_transaction(cid, wid, total_price):
    


#  Return a list of (addr_id,Address_Line1,Address_Line2,City,State,Postal_Code,Country)
def Load_addresses(cid):
    mycursor = connection.cursor()
    query = "SELECT * FROM address WHERE customer_id = %s"
    mycursor.execute(query, (cid,))
    results = mycursor.fetchall()
    addresses = []
    for i in results:
        i.pop(1)
        addresses.append(i)
        
# return a list of wallet ids
def Load_wallets(cid):
    mycursor = connection.cursor()
    query = "SELECT wallet_id FROM wallet WHERE customer_id = %s"
    mycursor.execute(query, (cid,))
    results = mycursor.fetchall()
    wallets = []
    for i in results:
        wallets.append(i[0])
    return wallets

# return addr id 
def Register_address(cid,Address_Line1,Address_Line2,City,State,Postal_Code,Country):
    mycursor=connection.cursor()
    query1 = "select address_id from address order by address_id desc limit 1"
    mycursor.execute(query1)
    z=mycursor.fetchall()
    aid=0
    for i in z:
        aid=i[0]+1
    query='insert into addreess values(%s,%s,%s,%s,%s,%s,%s)'
    values=(aid,cid,Address_Line1,Address_Line2,City,State,Postal_Code,Country)
    mycursor.execute(query,values)
    connection.commit()
    return aid

def Register_wallet(cid,balance):
    mycursor=connection.cursor()
    query = "select wallet_id from wallet order by wallet_id desc limit 1"
    mycursor.execute(query)
    z=mycursor.fetchall()
    wid=0
    for i in z:
        wid=i[0]+1
    query='insert into wallet values(%s,%s,%s)'
    values=(wid,cid,balance)
    mycursor.execute(query,values)
    connection.commit()
    return wid

# Return status ->
# 0 for success , 1 for user already exists , else something wrong
def update_mail(cid,email):
    mycursor=connection.cursor()
    query1='select 1 from customer where email=%s'
    mycursor.execute(query1,(email,))
    result=mycursor.fetchone()
    if result:
        return 1
    else:
        values2=email,cid
        query2='update customer set email=%s where customer_id=%s'
        mycursor.execute(query2,values2)
        connection.commit()
        return 0

def update_name(cid,first_name,last_name):
    mycursor=connection.cursor()
    values=first_name,last_name,cid
    query='update Customer set FirstName=%s,LastName=%s where Customer_ID=%s'
    mycursor.execute(query,values)
    connection.commit()
    print("Name updated successfully")

def update_mobile(cid,mobile):
    mycursor=connection.cursor()
    values=mobile,cid
    query='update customer set phoneno=%s where customer_id=%s'
    mycursor.execute(query,values)
    connection.commit()
    print("PhoneNo updated successfully")

def update_dob(cid,dob):
    mycursor=connection.cursor()
    values=dob,cid
    query='update customer set dob=%s where customer_id=%s'
    mycursor.execute(query,values)
    connection.commit()
    print("DOB updated successfully")

# status -> 0 for success, 1 for wrong password
def update_pass(cid,old_password,new_password): 
    mycursor = connection.cursor()
    query1 = "select HEX(AES_ENCRYPT(%s, 'project'))"
    mycursor.execute(query1, (old_password,))
    result = mycursor.fetchone()[0]
    query2 = "select 1 from authentication where customer_id = %s AND customer_password = %s"
    value2 = (cid, result)
    mycursor.execute(query2, value2)
    check2 = mycursor.fetchone()
    if check2:
        print("Authentication successful")
        query3 = "update authentication set customer_password = %s where customer_id = %s"
        value3 = (new_password, cid)
        mycursor.execute(query3, value3)
        return 0
    else:
        return 1


def Get_Customer_Details_SQL(cid):
    mycursor = connection.cursor()
    query = "SELECT firstname, lastname, phoneno, email, dob FROM customer WHERE customer_id = %s"
    mycursor.execute(query, (cid,))
    result = mycursor.fetchone()
    for i in result:
        customer = {"FirstName": i[0],"LastName": i[1],"PhoneNo": i[2],"Email": i[3],"DOB": i[4]}
    return customer
