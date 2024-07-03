select count(rating) from game where rating>=8.5; --Query1

select title from game order by rating desc;  --Query2

SELECT       --Query3
    c.firstname,
    c.lastname,
    c.Customer_ID,
    o.Game_ID
FROM 
    orders o
JOIN
    customer c ON o.Customer_ID = c.Customer_ID
WHERE 
    o.Game_ID = (
        SELECT 
            Game_ID
        FROM 
            orders
        GROUP BY 
            Game_ID
        ORDER BY 
            COUNT(Game_ID) DESC
        LIMIT 1
    );
    
select avg(rating) from game_review;   --Query4
    
    
