-- script that lists all records score >= 10 of the table second_table of the database hbtn_0c_0
-- in Mysql server, results should be ordered by score(top) first
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
