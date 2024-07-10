create database game_galaxy;
use game_galaxy;

CREATE TABLE Customer (
  Customer_ID varchar(50),
  FirstName varchar(100),
  LastName varchar(100),
  PhoneNo int,
  Email varchar(100),
  DOB date,
  PRIMARY KEY (Customer_ID)
);

CREATE TABLE Game (
  Game_ID int,
  Title varchar(100),
  Genre varchar(50),
  Release_Date date,
  Game_Desc varchar(100),
  Rating float,
  Developer varchar(100),
  Price int,
  PRIMARY KEY (Game_ID)
);

CREATE TABLE Orders (
  Order_ID int,
  Customer_ID varchar(50),
  Order_Amount int,
  Order_Status bool,
  Transaction_ID int,
  Address_ID int,
  Game_ID int,
  Quantity int not null default 0,
  PRIMARY KEY (Order_ID)
);

CREATE TABLE Cart (
  Customer_ID varchar(50),
  Game_ID int,
  Quantity int,
  PRIMARY KEY (Customer_ID, Game_ID)
);

CREATE TABLE Authentication (
  Customer_ID varchar(50),
  Email varchar(100),
  Customer_Password varchar(100),
  PRIMARY KEY (Customer_ID)
);

CREATE TABLE Address (
  Address_ID int,
  Customer_ID varchar(50),
  Address_Line1 varchar(50),
  Address_Line2 varchar(50),
  City varchar(30),
  State varchar(30),
  Postal_Code varchar(6),
  Country varchar(10),
  PRIMARY KEY (Address_ID)
);

CREATE TABLE Game_Review (
  Customer_ID varchar(50),
  Game_ID int,
  Review varchar(1000),
  Rating int,
  PRIMARY KEY (Customer_ID, Game_ID)
);

CREATE TABLE Payment (
  Transaction_ID int,
  Payment_Amount int,
  Payment_Status bool
);

CREATE TABLE Wallet (
  Wallet_ID int,
  Customer_ID varchar(50),
  Balance int,
  PRIMARY KEY (Wallet_ID)
);

CREATE TABLE Transaction (
  Trans_ID int,
  Wallet_ID int,
  Trans_Type bool,
  Trans_Date date,
  Trans_Amount int,
  PRIMARY KEY (Trans_ID)
);
