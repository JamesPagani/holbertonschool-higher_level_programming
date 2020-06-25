-- Create a new table called cities in the hbtn_0d_usa database.
-- Should one not exist, it will be created
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
