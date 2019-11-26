-- script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
--   states description:
--     id INT unique, auto generated, can’t be null and is a primary key
--     name VARCHAR(256) can’t be null
--   If the database hbtn_0d_usa already exists, your script should not fail
--   If the table states already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT AUTO_INCREMENT PRIMARY KEY UNIQUE NOT NULL,
name VARCHAR(256) NOT NULL);
