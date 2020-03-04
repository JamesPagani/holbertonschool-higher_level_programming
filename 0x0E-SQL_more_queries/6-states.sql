-- Creates a new database and a table inside it
-- DATABASE: hbtn_0d_usa
-- TABLE: states
-- COLUMNS: id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMERY KEY,
--          name VARCHAR(256)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       name VARCHAR(256)
);
