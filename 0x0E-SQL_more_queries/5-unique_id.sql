-- Creates a table with a column only accepting unique values
-- TABLE: unique_id
-- COLUMNS: id INT DEFAULT 1 UNIQUE, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id(
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
