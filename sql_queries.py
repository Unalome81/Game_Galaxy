import mysql.connector
connection = mysql.connector.connect(host="localhost", user='root', database='game_galaxy', password='fortune')
mycursor = connection.cursor()

# Return status ->
# 0 for success , 1 for user already exists , else something wrong 
#  also create a wallet
def Registration_SQL(first_name,last_name,mobile,email,dob):
    query = "select customer_id from customer order by customer_id desc limit 1"
    mycursor.execute(query)
    z=mycursor.fetchall()
    for i in z:
        string=i[0]
    conv_string=string[0]
    conv_integer=int(string[1:])
    cust_id=conv_string+'0'+str(conv_integer+1)

    values=(cust_id,first_name,last_name,mobile,email,dob)
    query="insert into customer (customer_id,firstname,lastname,phoneno,email,dob) values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query,values)

    cid = (mycursor.execute("Select customer_id from customer where email = %s", email)).fetchone()

    query="insert into wallet () values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query,values)
    connection.commit()


# Return three things -> status, customerid, user_first_name (if found)
# 0 for success , 1 for email doesn't exist, 2 for wrong password, or else retry
def Find_Customer_SQL(email, password):
    email_query = "select 1 from authentication where email = %s"
    mycursor.execute(email_query, (email,))
    results = mycursor.fetchone()

    password_query="select 1 from authentication where customer_password = HEX(AES_ENCRYPT(%s, 'project'))"
    mycursor.execute(password_query, (password,))
    results2=mycursor.fetchone()

    que = "select customer_id,firstname from customer where email = %s"
    mycursor.execute(que, (email,))
    results3 = mycursor.fetchall()
    for j in results3:
        customer_id=j[0]
        first_name=j[1]

    if results and results2:
        status=0
    elif results is None:
        status=1
    elif results2 is None:
        status=2
    else:
        status=-1


        
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
def Show_Games_SQL(rating_filter, price_filter, genre_filter):
    query = "SELECT game_id, title, genre, price, rating, release_date, game_description, developer FROM game WHERE rating >= %s AND price <= %s"
    params = [rating_filter, price_filter]
    
    if genre_filter != "*":
        query += " AND genre = %s"
        params.append(genre_filter)
    
    mycursor.execute(query, tuple(params))
    results = mycursor.fetchall()

    games = []
    for row in results:
        game = {
            'game_id': row[0],
            'title': row[1],
            'genre': row[2],
            'price': row[3],
            'rating': row[4],
            'release_date': row[5],
            'game_description': row[6],
            'developer': row[7]
        }
        games.append(game)
    return games

# cart is  a list of tuples ->(gid, gname, quantity)
def Load_cart_SQL(cid):
    mycursor = connection.cursor()
    query = """
        SELECT cart.game_id, game.title, cart.quantity 
        FROM cart 
        JOIN game ON cart.game_id = game.game_id 
        WHERE cart.customer_id = %s
    """
    mycursor.execute(query, (cid,))
    results = mycursor.fetchall()

    cart_items = [(row[0], row[1], row[2]) for row in results]
    
    return cart_items

def Dump_cart_SQL(cid, cart):
    mycursor = connection.cursor()
    
    mycursor.execute("SELECT game_id, quantity FROM cart WHERE customer_id = %s", (cid,))
    existing_cart = mycursor.fetchall()
    
    existing_cart_dict = {item[0]: item[1] for item in existing_cart}
    
    new_cart_dict = {item[0]: item[1] for item in cart}
    
    for game_id, quantity in new_cart_dict.items():
        if game_id in existing_cart_dict:
            if quantity != existing_cart_dict[game_id]:
                mycursor.execute(
                    "UPDATE cart SET quantity = %s WHERE customer_id = %s AND game_id = %s",
                    (quantity, cid, game_id)
                )
        else:
            mycursor.execute(
                "INSERT INTO cart (customer_id, game_id, quantity) VALUES (%s, %s, %s)",
                (cid, game_id, quantity)
            )
    
    # Identify items to remove
    for game_id in existing_cart_dict:
        if game_id not in new_cart_dict:
            mycursor.execute(
                "DELETE FROM cart WHERE customer_id = %s AND game_id = %s",
                (cid, game_id)
            )
    
    # Commit the transaction
    connection.commit()
    
    print("Cart updated successfully.")

def Check_Wallet_Balance_SQL(cid):
    mycursor = connection.cursor()
    query = "SELECT balance FROM wallet WHERE Customer_ID = %s"
    mycursor.execute(query, (cid,))
    result = mycursor.fetchone()
    
    if result:
        balance = result[0]
    else:
        balance = 0     
    return balance
# check if bought
def checkbought(cid,game_id):

# if found overwrite it -> reclculate overall rating ,else add ,  rev_count ++ and reclculate overall rating 
def modifyRating(cid,game_id,rating_filter,rvw):

# if rating found remove it , if found reclculate overall rating 
def RemnoveRating(cid,game_id):


# fid ratings in this form list of -> (cname_first+" "+c_name_last,game rating given, game reviwe)
def findRatings_bygid_SQL(game_id):


# fid ratings in this form list of -> (gid, game-name,game rating given, game reviw) of cid
def findRatings_bycid_SQL(cid):

def remove_adress(cid,adr_id):

def remove_wallet(cid,walet_id)

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


# return balance of wid
def Check_Wallet_Balance_SQL(cid,wid):

# return list of wallet ids only
def Load_wallets(cid):

    # add money to wallet
def Payment_SQL(cid, amount_to_add):

# Returns the transaction id and log a transaction 
    # a success transaction
    # does entry to table and cuts the amt from wallet
def Transaction_SQL(cid, wid, total_price):

# Returns the transaction id and log a transaction 
    # a un-success transaction bad boy
def log_unsuccessfull_transaction(cid, wid, total_price):


#  Return a list of (addr_id,Address_Line1,Address_Line2,City,State,Postal_Code,Country)
def Load_addresses(cid):

# return a list of wallet ids
def Load_wallets(cid):

# return addr id  
#  do check if complete copy this table should be a set
def Register_address(Customer_ID,Address_Line1,Address_Line2,City,State,Postal_Code,Country):

# return wallet id
def Register_wallet(Customer_ID,Balence):

# Return status ->
# 0 for success , 1 for user already exists , else something wrong
def update_mail(cid,email):

def update_name(cid,first_name,last_name):

def update_mobile(cid,mobile):

def update_dob(cid,dob):

def update_pass(cid,password):

def Get_Customer_Details_SQL(cid):
    mycursor = connection.cursor()
    query = """
        SELECT firstname, lastname, phoneno, email, dob 
        FROM customer 
        WHERE customer_id = %s
    """
    mycursor.execute(query, (cid,))
    result = mycursor.fetchone()

    if result:
        customer = {
            "FirstName": result[0],
            "LastName": result[1],
            "PhoneNo": result[2],
            "Email": result[3],
            "DOB": result[4]
        }
    return customer

