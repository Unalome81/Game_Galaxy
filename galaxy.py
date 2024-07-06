import time
import platform
import os
import sql_queries as sql

wt_time = 5

class User():
    cart=[]
    f_name=""
    cid=-1
    def __init__(self, cid, f_name):
        self.cid = cid
        self.f_name = f_name
    def start_session(self):
        self.cart=sql.Load_cart_SQL(self.cid)
    def end_session(self):
        sql.Dump_cart_SQL(self.cid,self.cart)
    def add_to_cart(self,item,name,quantity):
        if(not self.change_item_quant(item,quantity,False)):
            self.cart.append((item,name,quantity))
    def change_item_quant(self,item,new_q,f):
        for i in self.cart:
            if(i[0]==item):
                i[2]=new_q if f else i[2]+new_q
                return True
        return False
    def remove_item_quant(self,item,q):
        for i in self.cart:
            if(i[0]==item):
                i[2]=max(0,i[2]-q)

def clearscreen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def Login():
    ch = 0
    while ch != 2:
        clearscreen()
        print("======================================================================================")
        print("Login to access our services !!")
        print("======================================================================================")
        email = input("Login Page: Enter Email: ")
        password = input("Login Page: Enter Password: ")  
        # 0 for ok, 1 for email doesn't exist, 2 for wrong password
        c, cid, f_name = sql.Find_Customer_SQL(email, password)
        if c == 0:
            print("Login: Successful")
            time.sleep(wt_time)
            return Home(User(cid, f_name))
        elif c == 1:
            print("Login: User with given email not found! Please register !!")
            time.sleep(wt_time)
            return Register()
        elif c == 2:
            print("Login: Wrong Password!")
        time.sleep(wt_time)
        ch = input("Login: \n\t1. Continue on this page \n\t2. Go back to Authentication Page: ")

    Authentication()

def Register():
    while True:
        clearscreen()
        print("======================================================================================")
        print("Register yourself with us !!")
        print("======================================================================================")
        back = input("Do you wish to go back? (y for yes): ")
        if back.lower() == 'y':
            return main()
        first_name = input("Register: Enter your First Name: ")
        last_name = input("Register: Enter your Last Name: ")
        mobile = input("Register: Enter your phone number: ")
        dob = input("Register: Enter your date of birth (yyyy-mm-dd): ")
        email = input("Register: Enter your Email: ")
        password = input("Register: Choose a Password: ")
        confpassword = input("Register: Confirm the Password: ")
        while password != confpassword:
            print("ERROR: Passwords don't match")
            retry = input("Do you wish to retry? (y for yes): ")
            if retry.lower() != 'y':
                return main()
            time.sleep(wt_time)
            clearscreen()
            password = input("Register: Choose a Password: ")
            confpassword = input("Register: Confirm the Password: ")
        c = sql.Registration_SQL(first_name, last_name, mobile, dob, email, password)
        if c == 0:
            print("Registration done Successfully! Now Please Log in")
            time.sleep(wt_time)
            return Login()
        elif c == 1:
            print("You are already Registered to our Galaxy! Please Log in")
            time.sleep(wt_time)
            return Login()
        else:
            print("Registration Failed :( Please Retry!!")
            time.sleep(wt_time)

def Game_Review(c_user):
    c = 0
    while c != 4:
        clearscreen()
        print("======================================================================================")
        print(f"{c_user.f_name}'s Reviews")
        print()
        print("======================================================================================")
        print("Game_Review: \n\t Enter 1 to view your Reviews \n\t Enter 2 to give a new Review \n\t Enter 3 to Remove a Review \n\tEnter 4 to go Back")
        c = int(input("Enter your choice : "))
        if(c==1):
            l=sql.findRatings_bycid_SQL(c_user.cid)
            if(len(l)==0):
                print("No Review found in your profie!! Rate a new Game")
            else:
                for i in l:
                    print(f"Game-ID - {i[0]}: Game Name - {i[1]} , Rating given - {i[2]}, Review - {i[3]}")
        elif(c==2):
            game_id = input("Enter the Game ID to Review")
            # check if bought
            if(sql.checkbought(c_user.cid,game_id)):
                rating_filter = -1
                while rating_filter < 0 or rating_filter > 10:
                    rating_filter = int(input("Games: Enter your rating threshold 0 - 10: "))
                    if rating_filter < 0 or rating_filter > 10:
                        print("Input is not in the specified limits, please enter the your rating again")
                rvw=input("Enter Your Review : ")
                sql.modifyRating(c_user.cid,game_id,rating_filter,rvw)
            else:
                print("Please Buy this game first!!")
        elif(c==3):
            game_id = input("Enter the Game ID whose Review is to be removed: ")
            sql.RemnoveRating(c_user.cid,game_id)
            print("Cart: Review removed successfully!")
        else:
            print("Home: Invalid Input")
    return
def Home(c_user):
    c = 0
    c_user.start_session()
    while c != 5:
        clearscreen()
        print("======================================================================================")
        print(f"Dear {c_user.f_name}, Welcome to Game Galaxy!")
        print("======================================================================================")
        c = int(input("Home: \n\t1. View our Games \n\t2. Go to cart \n\t3. Give a game review \n\t4. View your profile \n\t5. Log out: "))
        if c == 1:
            View_Games(c_user)
        elif c == 2:
            Cart(c_user)
        elif c == 3:
            Game_Review(c_user)
        elif c == 4:
            View_Profile(c_user)
        elif c == 5:
            c_user.end_session()
            return Login()
        else:
            print("Home: Invalid Input")
        time.sleep(wt_time)    

# add address: which one chose 1  or add new
# add wallet: which one chose 1  or add new
# rem addresses : if you dont want to save
# rem wallets : if you dont want to save
# change in particulars and password
# view profife
# view old orders
def View_Profile(c_user):
    clearscreen()
    
    while(True):
        print("Profile: \n\t Enter 1 to view your details \n\t Enter 2 to update your details \n\t Enter 3 to go back to home")
        ch = input()
        if(ch == "1"):
            Customer_Details = Get_Customer_Details_SQL(c_user.cid)
            for key, value in Customer_Details.items():
                print(f"{key}: {value}")
        elif(ch == "2"):
            print("You cannot change Ennter your new details: ")
        elif(ch == "3"):
            break
        else 
            print("Profile: Invalid Inpur")
    

def View_Games(c_user):
    clearscreen()
    rating_filter = -1
    while rating_filter < 0 or rating_filter > 10:
        rating_filter = int(input("Games: Enter your rating threshold 0 - 10: "))
        if rating_filter < 0 or rating_filter > 10:
            print("Games: Input is not in the specified limits, please enter the rating filter again")
    
    price_filter_max = -1
    price_filter_min = -1
    mx = 0
    while price_filter_max < 0 or price_filter_min > mx or price_filter_max <= price_filter_min:
        mn, mx = sql.Price_Range_SQL()
        print(f"Games: We have games in the price ranges {mn} to {mx}")
        price_filter_max = int(input("Games: Enter maximum price: "))
        price_filter_min = int(input("Games: Enter minimum price: "))
        if price_filter_max < 0 or price_filter_min > mx or price_filter_max <= price_filter_min:
            print("Games: Invalid Price!")
    
    chk = False
    genre_filter = "*"
    while not chk:
        available_genres = sql.Print_Genres_SQL()
        print(" ".join(available_genres))

        genre_filter = input("Games: Enter your preferred genre, if you want to see all genres enter ALL: ")
        if genre_filter == "ALL":
            break
        if genre_filter not in available_genres:
            print("Games: Sorry, we do not have this genre, please select from our existing list")
        else:
            chk = True

    # Print games with these filters: rating_filter: 1-10, price_filter: no constraint, genre_filter = "*" for all
    available_games = sql.Show_Games_SQL(rating_filter, price_filter_min, price_filter_max, genre_filter)
    if len(available_games) == 0:
        print("No games with the given constraints")
        return

    print("S.No.\t\t\t Name of the Game")
    for i in range(len(available_games)):
        print(f"({i+1})\t\t\t{available_games[i]['game']}")
    
    while True:
        clearscreen()
        for i in range(len(available_games)):
            print(f"({i+1})\t\t\t{available_games[i]['game']}")
        c = int(input("Enter S.No. to view a game else Enter 0 to go back to Homescreen: "))
        if c == 0:
            break
        if c > len(available_games):
            print("Error: Wrong input")
            continue
        for key, value in available_games[c-1].items():
            print(f"{key} : {value}")
        i = input("If you wish to see all ratings of this game press 'y': ")
        if i.lower() == "y":
            l=sql.findRatings_bygid_SQL(available_games[c-1]['game_id'])
            for i in l:
                print(f"Customer Name - {i[0]} : Rating given - {i[1]}, Review - {i[2]}")
        i = input("If you wish to buy this game press 'y': ")
        if i.lower() == "y":
            print("Please Enter Quantity to add")
            k=int(input("Enter a positive number : "))
            if(k<=0):
                raise Exception(f"{k} is not an positive integer")
            c_user.add_to_cart(available_games[c-1]['game_id'],available_games[c-1]['game'],k)
            print("GAME ADDED TO YOUR CART")
            time.sleep(wt_time)

def Cart(c_user):
    while True:
        clearscreen()
        print("======================================================================================")
        print(f"{c_user.f_name}'s Cart")
        print("======================================================================================")
        print("Cart: \n\t1. Add a game to the cart \n\t2. Remove game from cart \n\t3. View cart \n\t4. View available games \n\t5. Checkout \n\t6. Go back to Home")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            game_id = input("Cart: Enter the Game ID to add to cart: ")
            game,found=sql.findgame_SQL(game_id)
            if(found):
                quantity = int(input("Cart: Enter the quantity: "))
                c_user.add_to_cart(game_id,game,quantity)
                print("...")
                time.sleep(wt_time)
                print("Cart: Game added to cart successfully!")
            else:
                print("Cart: Game not found in our catlog!! Game id is invalid! Please Retry")
        elif ch == 2:
            game_id = input("Cart: Enter the Game ID to remove from cart: ")
            quantity = input("Cart: Enter the quantity to remove (ENTER \'*\' to remove all) : ")
            quantity= 100000000000 if(quantity=='*') else int(quantity)
            c_user.remove_item_quant(game_id,quantity)
            print("Cart: Game removed from cart successfully!")
            time.sleep(wt_time)
        elif ch == 3:
            clearscreen()
            print("======================================================================================")
            print(f"Cart: {c_user.f_name}'s Cart Items")
            print("======================================================================================")
            for item in c_user.cart_items:
                print(f"\tGame ID: {item[0]}, Game Name {item[1]} , Quantity: {item[2]}")
            input("Press Any Key to continue...")
        elif ch == 4:
            View_Games(c_user)
            time.sleep(wt_time)
        elif ch == 5:
            if len(c_user.cart) == 0:
                print("Cart is empty. Add items to cart before checkout.")
            else:
                if(Checkout(c_user)):
                    c_user.cart.clear()
            time.sleep(wt_time)
        elif ch == 6:
            return
        else:
            print("Invalid choice. Please try again.")
            time.sleep(wt_time)

# chose address: which one chose 1  or add new
# chose wallet: which one chose 1  or add new
# add to orders -> wallet ,time and date , items , bill
def Checkout(c_user):
    clearscreen()
    print("======================================================================================")
    print("Checkout")
    print("======================================================================================")
    
    # Calculate total price using SQL function
    total_price = sql.Calculate_Total_Price_SQL(c_user.cid, c_user.cart)
    print(f"Total price of items in cart: {total_price}")
    
    # Check the user's wallet balance using SQL function
    wallet_balance = sql.Check_Wallet_Balance_SQL(c_user.cid)
    print(f"Your current wallet balance: {wallet_balance}")

    while wallet_balance < total_price:
        print("Insufficient wallet balance.")
        add_money = input("Do you want to add money to your wallet? (yes/no): ")
        if add_money.lower() == 'yes':
            AddMoneyToWallet(c_user)
            wallet_balance = sql.Check_Wallet_Balance_SQL(c_user.cid)
            clearscreen()
            print("======================================================================================")
            print("Checkout")
            print("======================================================================================")
            print(f"Total price of items in cart: {total_price}")
            print(f"Your new wallet balance: {wallet_balance}")
        else:
            print("Payment cancelled.")
            input("Press Enter to continue...")
            return False

    confirm = input("Do you want to proceed with the payment? (yes/no): ")
    if confirm.lower() == 'yes':
        sql.Transaction_SQL(c_user.cid, total_price)
        print("Transaction successful! Thank you for your purchase.")
        return True
    else:
        print("Transaction cancelled.")
        return False
    
def AddMoneyToWallet(c_user):
    amount_to_add = -1
    while amount_to_add <= 0:
        try:
            amount_to_add = float(input("Enter the amount to add to your wallet: "))
            if amount_to_add <= 0:
                print("Invalid amount. Please enter a positive value.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    sql.Payment_SQL(c_user.cid, amount_to_add)
    print("...")
    time.sleep(wt_time)

def Authentication():
    clearscreen()
    ch = ""
    while ch != "3":
        clearscreen()
        print("======================================================================================")
        ch = input("Authentication: \n\t1. Login \n\t2. Register with us \n\t3. Exit\n======================================================================================\n")
        if ch == "1":
            return Login()
        elif ch == "2":
            return Register()
        elif ch == "3":
            print("Authentication: Exited Successfully")
        else:
            print("Authentication: Invalid Input")
        time.sleep(wt_time)
        
def main():
    clearscreen()
    print("======================================================================================")
    print("Welcome to Game Galaxy!")
    print("======================================================================================")
    time.sleep(wt_time)
    Authentication()
    print("Thank you for dropping by, visit Again!")
     
if __name__ == "__main__":
    main()
