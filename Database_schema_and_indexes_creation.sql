INSERT INTO Address (Address_ID, Customer_ID, Address_Line1, Address_Line2, City, State, Postal_Code, Country) VALUES
(1, 'C001', '123 Maple St', 'Apt 4B', 'Springfield', 'IL', '62704', 'USA'),
(2, 'C002', '456 Elm St', NULL, 'Salem', 'OR', '97301', 'USA'),
(3, 'C003', '789 Oak St', 'Suite 200', 'Columbus', 'OH', '43215', 'USA'),
(4, 'C004', '101 Pine St', NULL, 'Austin', 'TX', '73301', 'USA'),
(5, 'C005', '202 Birch St', NULL, 'Madison', 'WI', '53703', 'USA'),
(6, 'C006', '303 Cedar St', 'Unit 5', 'Denver', 'CO', '80202', 'USA'),
(7, 'C007', '404 Aspen St', NULL, 'Seattle', 'WA', '98101', 'USA'),
(8, 'C008', '505 Redwood St', 'Apt 7C', 'Boston', 'MA', '02108', 'USA'),
(9, 'C009', '606 Fir St', NULL, 'Miami', 'FL', '33101', 'USA'),
(10, 'C010', '707 Spruce St', 'Apt 9A', 'Phoenix', 'AZ', '85001', 'USA');

create index idx_addr_state on Address(State);

INSERT INTO authentication (Customer_ID, Email, customer_password) VALUES
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
('C001', 201, 1),
('C002', 202, 2),
('C003', 203, 1),
('C004', 204, 3),
('C005', 205, 1),
('C006', 206, 2),	
('C007', 207, 1),
('C008', 208, 4),
('C009', 209, 1),
('C010', 210, 2);

INSERT INTO customer (Customer_ID, FirstName, LastName, PhoneNo, Email, DOB) VALUES
('C001', 'John', 'Doe', 1234567890, 'john.doe@example.com', '1980-01-01'),
('C002', 'Jane', 'Smith', 1345678901, 'jane.smith@example.com', '1985-02-14'),
('C003', 'Michael', 'Johnson', 1456789012, 'michael.johnson@example.com', '1990-03-20'),
('C004', 'Emily', 'Davis', 1567890123, 'emily.davis@example.com', '1992-04-25'),
('C005', 'Daniel', 'Brown', 1678901234, 'daniel.brown@example.com', '1988-05-30'),
('C006', 'Jessica', 'Williams', 1789012345, 'jessica.williams@example.com', '1995-06-10'),
('C007', 'David', 'Miller', 1890123456, 'david.miller@example.com', '1978-07-15'),
('C008', 'Sarah', 'Wilson', 1901234567, 'sarah.wilson@example.com', '1983-08-20'),
('C009', 'James', 'Moore', 1012345678, 'james.moore@example.com', '1999-09-05'),
('C010', 'Laura', 'Taylor', 1234509876, 'laura.taylor@example.com', '1982-10-30');

create index idx_custom_email on customer(Email);

INSERT INTO game (Game_ID, Title, Genre, Release_Date, Game_Desc, Rating, Developer, Price) VALUES
(201, 'The Adventure Quest', 'RPG', '2024-05-15', 'An epic adventure through a fantastical world.', 9.5, 'Epic Studios', 59),
(202, 'Space Invaders Reborn', 'Shooter', '2023-10-30', 'A modern take on the classic space shooter.', 8.0, 'Galactic Games', 39),
(203, 'Mystery Manor', 'Puzzle', '2024-01-20', 'Solve intricate puzzles in a mysterious mansion.', 8.8, 'Puzzle Masters', 29),
(204, 'Racing Rivals', 'Racing', '2023-11-05', 'High-speed racing with customizable cars.', 9.2, 'Speedy Creations', 49),
(205, 'Fantasy Battle Arena', 'MOBA', '2024-03-12', 'Team-based battles in a magical arena.', 8.5, 'Battle Realm', 44),
(206, 'Survival Island', 'Survival', '2023-09-10', 'Survive on a deserted island with limited resources.', 7.9, 'Island Ventures', 34),
(207, 'City Builder Tycoon', 'Simulation', '2024-02-25', 'Build and manage your own city from the ground up.', 8.7, 'CityScape', 39),
(208, 'Legend of the Dragon', 'Action', '2023-12-01', 'Fight epic battles against legendary dragons.', 9.0, 'Dragon Forge', 54),
(209, 'Haunted House Mystery', 'Horror', '2023-08-14', 'Uncover the dark secrets of a haunted house.', 7.5, 'Spooky Creations', 29),
(210, 'Sports Champions', 'Sports', '2024-06-18', 'Compete in various sports events to become a champion.', 8.2, 'Champion Games', 42);

create index idx_game_title on game(Title);
create index idx_game_genre on game(Genre);

INSERT INTO game_review (Customer_ID, Game_ID, Review, Rating) VALUES
('C001', 201, 'Great game with an immersive storyline and excellent graphics. Highly recommend!', 5),
('C002', 202, 'The gameplay was enjoyable, but the controls were a bit clunky. Still worth playing.', 3),
('C003', 203, 'An average game with some interesting concepts, but it lacks depth.', 2),
('C004', 204, 'Amazing experience! The multiplayer mode is fantastic and keeps you hooked for hours.', 4),
('C005', 205, 'Disappointing. The game had numerous bugs and the story was unoriginal.', 1),
('C006', 206, 'Good graphics and sound, but the game is very repetitive. Could be improved.', 3),
('C007', 207, 'Fantastic game with a lot of content. The developers did a great job!', 5),
('C008', 208, 'It was okay, but I expected more from the sequel. A bit underwhelming.', 2),
('C009', 209, 'A fun game with a lot of potential, but it needs more polish and updates.', 3),
('C010', 210, 'A masterpiece! The best game I’ve played this year. Every aspect is well-designed.', 5);

create index idx_gamerev_rating on game_review(Rating);

INSERT INTO orders (Order_ID, Customer_ID, Order_Amount, Order_Status, Transaction_ID, Address_ID,Game_ID) VALUES
(101, 'C001', 250, 1, 5001, 1,201),
(102, 'C002', 150, 0, 5002, 2,202),
(103, 'C003', 300, 1, 5003, 3,203),
(104, 'C004', 120, 1, 5004, 4,204),
(105, 'C005', 200, 0, 5005, 5,201),
(106, 'C006', 180, 1, 5006, 6,206), 
(107, 'C007', 220, 1, 5007, 7,201),
(108, 'C008', 175, 0, 5008, 8,208),
(109, 'C009', 260, 1, 5009, 9,201),
(110, 'C010', 140, 1, 5010, 10,210);

create index idx_orders_ordstat on orders(Order_Status);
create index idx_orders_customid on orders(Customer_ID);

INSERT INTO payment (Transaction_ID, Payment_Amount, Payment_Status) VALUES
(5001, 150, 1),
(5002, 200, 0),
(5003, 75, 1),
(5004, 300, 1),
(5005, 120, 0),
(5006, 250, 1),
(5007, 90, 1),
(5008, 180, 0),
(5009, 60, 1),
(5010, 500, 0);

create index idx_pay_transid on payment(Transaction_ID);
create index idx_pay_paystat on payment(Payment_Status);

INSERT INTO transaction (Trans_ID, Wallet_ID, Trans_Type, Trans_Date, Trans_Amount) VALUES
(5001, 401, 1, '2024-07-01', 1500),
(5002, 402, 2, '2024-07-02', 500),
(5003, 403, 1, '2024-07-03', 750),
(5004, 404, 3, '2024-07-04', 1200),
(5005, 405, 2, '2024-07-05', 300),
(5006, 406, 1, '2024-07-06', 600),
(5007, 407, 3, '2024-07-07', 1800),
(5008, 408, 2, '2024-07-08', 450),
(5009, 409, 1, '2024-07-09', 700),
(5010, 410, 3, '2024-07-10', 1300);

create index idx_trans_walletid on transaction(Wallet_ID);
create index idx_trans_date on transaction(Trans_date);

INSERT INTO wallet (Wallet_ID, Customer_ID, Balance) VALUES
(401, 'C001', 500),
(402, 'C002', 1500),
(403, 'C003', 200),
(404, 'C004', 750),
(405, 'C005', 300),
(406, 'C006', 1000),
(407, 'C007', 450),
(408, 'C008', 1200),
(409, 'C009', 600),
(410, 'C010', 900);
