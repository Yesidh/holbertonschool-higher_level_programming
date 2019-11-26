-- mysql -u root -p hbtn_0c_0 < /home/yesid/Downloads/temperatures.sql whit this command
-- import the table into my databse
-- Now I need a script that displays the average temperature by city ordered by temperature
-- descending
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
