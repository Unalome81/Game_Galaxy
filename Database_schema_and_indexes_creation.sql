use game_galaxy;

INSERT INTO Address (Address_ID, Customer_ID, Address_Line1, Address_Line2, City, State, Postal_Code, Country) VALUES
(1, 101, '123 Maple St', 'Apt 4B', 'Springfield', 'IL', '62704', 'USA'),
(2, 102, '456 Elm St', NULL, 'Salem', 'OR', '97301', 'USA'),
(3, 103, '789 Oak St', 'Suite 200', 'Columbus', 'OH', '43215', 'USA'),
(4, 104, '101 Pine St', NULL, 'Austin', 'TX', '73301', 'USA'),
(5, 105, '202 Birch St', NULL, 'Madison', 'WI', '53703', 'USA'),
(6, 106, '303 Cedar St', 'Unit 5', 'Denver', 'CO', '80202', 'USA'),
(7, 107, '404 Aspen St', NULL, 'Seattle', 'WA', '98101', 'USA'),
(8, 108, '505 Redwood St', 'Apt 7C', 'Boston', 'MA', '02108', 'USA'),
(9, 109, '606 Fir St', NULL, 'Miami', 'FL', '33101', 'USA'),
(10, 110, '707 Spruce St', 'Apt 9A', 'Phoenix', 'AZ', '85001', 'USA');

create index idx_addr_state on Address(State);

INSERT INTO authenication (Customer_ID, Email, user_password) VALUES
('C001', 'john.doe@example.com', HEX(AES_ENCRYPT('password123', 'project'))),
('C002', 'jane.smith@example.com', HEX(AES_ENCRYPT('qwertyuiop', 'project'))),
('C003', 'alice.jones@example.com', HEX(AES_ENCRYPT('letmein123', 'project'))),
('C004', 'bob.brown@example.com', HEX(AES_ENCRYPT('adminpass', 'project'))),
('C005', 'carol.white@example.com',HEX(AES_ENCRYPT( '12345678', 'project'))),
('C006', 'david.clark@example.com',HEX(AES_ENCRYPT( 'password1', 'project'))),
('C007', 'eve.martin@example.com', HEX(AES_ENCRYPT('mypassword', 'project'))),
('C008', 'frank.thomas@example.com',HEX(AES_ENCRYPT( 'welcome123', 'project'))),
('C009', 'grace.harris@example.com',HEX(AES_ENCRYPT( 'ilovecoding', 'project'))),
('C010', 'henry.lewis@example.com',HEX(AES_ENCRYPT( 'testpassword', 'project')));

INSERT INTO cart (Customer_ID, Game_ID, Quantity) VALUES
(101, 201, 1),
(102, 202, 2),
(103, 203, 1),
(104, 204, 3),
(105, 205, 1),
(106, 206, 2),
(107, 207, 1),
(108, 208, 4),
(109, 209, 1),
(110, 210, 2);

INSERT INTO customer (Customer_ID, FirstName, LastName, PhoneNo, Email, DOB) VALUES
(101, 'John', 'Doe', 1234567890, 'john.doe@example.com', '1980-01-01'),
(102, 'Jane', 'Smith', 1345678901, 'jane.smith@example.com', '1985-02-14'),
(103, 'Michael', 'Johnson', 1456789012, 'michael.johnson@example.com', '1990-03-20'),
(104, 'Emily', 'Davis', 1567890123, 'emily.davis@example.com', '1992-04-25'),
(105, 'Daniel', 'Brown', 1678901234, 'daniel.brown@example.com', '1988-05-30'),
(106, 'Jessica', 'Williams', 1789012345, 'jessica.williams@example.com', '1995-06-10'),
(107, 'David', 'Miller', 1890123456, 'david.miller@example.com', '1978-07-15'),
(108, 'Sarah', 'Wilson', 1901234567, 'sarah.wilson@example.com', '1983-08-20'),
(109, 'James', 'Moore', 1012345678, 'james.moore@example.com', '1999-09-05'),
(110, 'Laura', 'Taylor', 1234509876, 'laura.taylor@example.com', '1982-10-30');

create index idx_custom_email on customer(Email);

INSERT INTO game (Game_ID, Title, Genre, Release_Date, Game_Desc, Rating, Developer, Price) VALUES
(1, 'The Adventure Quest', 'RPG', '2024-05-15', 'An epic adventure through a fantastical world.', 9.5, 'Epic Studios', 59),
(2, 'Space Invaders Reborn', 'Shooter', '2023-10-30', 'A modern take on the classic space shooter.', 8.0, 'Galactic Games', 39),
(3, 'Mystery Manor', 'Puzzle', '2024-01-20', 'Solve intricate puzzles in a mysterious mansion.', 8.8, 'Puzzle Masters', 29),
(4, 'Racing Rivals', 'Racing', '2023-11-05', 'High-speed racing with customizable cars.', 9.2, 'Speedy Creations', 49),
(5, 'Fantasy Battle Arena', 'MOBA', '2024-03-12', 'Team-based battles in a magical arena.', 8.5, 'Battle Realm', 44),
(6, 'Survival Island', 'Survival', '2023-09-10', 'Survive on a deserted island with limited resources.', 7.9, 'Island Ventures', 34),
(7, 'City Builder Tycoon', 'Simulation', '2024-02-25', 'Build and manage your own city from the ground up.', 8.7, 'CityScape', 39),
(8, 'Legend of the Dragon', 'Action', '2023-12-01', 'Fight epic battles against legendary dragons.', 9.0, 'Dragon Forge', 54),
(9, 'Haunted House Mystery', 'Horror', '2023-08-14', 'Uncover the dark secrets of a haunted house.', 7.5, 'Spooky Creations', 29),
(10, 'Sports Champions', 'Sports', '2024-06-18', 'Compete in various sports events to become a champion.', 8.2, 'Champion Games', 42);

create index idx_game_title on game(Title);
create index idx_game_genre on game(Genre);

INSERT INTO game_review (Customer_ID, Game_ID, Review, Rating) VALUES
(1, 101, 'Great game with an immersive storyline and excellent graphics. Highly recommend!', 5),
(2, 102, 'The gameplay was enjoyable, but the controls were a bit clunky. Still worth playing.', 3),
(3, 103, 'An average game with some interesting concepts, but it lacks depth.', 2),
(4, 104, 'Amazing experience! The multiplayer mode is fantastic and keeps you hooked for hours.', 4),
(5, 105, 'Disappointing. The game had numerous bugs and the story was unoriginal.', 1),
(6, 106, 'Good graphics and sound, but the game is very repetitive. Could be improved.', 3),
(7, 107, 'Fantastic game with a lot of content. The developers did a great job!', 5),
(8, 108, 'It was okay, but I expected more from the sequel. A bit underwhelming.', 2),
(9, 109, 'A fun game with a lot of potential, but it needs more polish and updates.', 3),
(10, 110, 'A masterpiece! The best game I’ve played this year. Every aspect is well-designed.', 5);

create index idx_gamerev_rating on game_review(Rating);

INSERT INTO orders (Order_ID, Customer_ID, Order_Amount, Order_Status, Transaction_ID, Address_ID) VALUES
(1, 101, 250, 1, 5001, 1),
(2, 102, 150, 0, 5002, 2),
(3, 103, 300, 1, 5003, 3),
(4, 104, 120, 1, 5004, 4),
(5, 105, 200, 0, 5005, 5),
(6, 106, 180, 1, 5006, 6),
(7, 107, 220, 1, 5007, 7),
(8, 108, 175, 0, 5008, 8),
(9, 109, 260, 1, 5009, 9),
(10, 110, 140, 1, 5010, 10);

create index idx_orders_ordstat on orders(Order_Status);
create index idx_orders_customid on orders(Customer_ID);

INSERT INTO payment (Transaction_ID, Payment_Amount, Payment_Status) VALUES
(1, 150, 1),
(2, 200, 0),
(3, 75, 1),
(4, 300, 1),
(5, 120, 0),
(6, 250, 1),
(7, 90, 1),
(8, 180, 0),
(9, 60, 1),
(10, 500, 0);

create index idx_pay_transid on payment(Transaction_ID);
create index idx_pay_paystat on payment(Payment_Status);

INSERT INTO transaction (Transaction_ID, Wallet_ID, Type, Date, Transaction_Amount) VALUES
(1, 201, 1, '2024-07-01', 1500),
(2, 202, 2, '2024-07-02', 500),
(3, 203, 1, '2024-07-03', 750),
(4, 204, 3, '2024-07-04', 1200),
(5, 205, 2, '2024-07-05', 300),
(6, 206, 1, '2024-07-06', 600),
(7, 207, 3, '2024-07-07', 1800),
(8, 208, 2, '2024-07-08', 450),
(9, 209, 1, '2024-07-09', 700),
(10, 210, 3, '2024-07-10', 1300);

create index idx_trans_walletid on transaction(Wallet_ID);
create index idx_trans_date on transaction(Date);

INSERT INTO wallet (Wallet_ID, Customer_ID, Balance) VALUES
(1, 101, 500),
(2, 102, 1500),
(3, 103, 200),
(4, 104, 750),
(5, 105, 300),
(6, 106, 1000),
(7, 107, 450),
(8, 108, 1200),
(9, 109, 600),
(10, 110, 900);
