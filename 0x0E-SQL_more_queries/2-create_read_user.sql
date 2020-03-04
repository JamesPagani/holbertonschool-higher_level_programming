-- Creates a new database and user (with only SELECT privileges on that DB)
-- Database: hbtn_0d_2
-- New user/pass: user_0d_2@localhost/user_0d_2_pwd
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
