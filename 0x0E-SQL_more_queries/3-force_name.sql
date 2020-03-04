-- Creates a new table with a NOT NULL column
-- TABLE: force_name
-- COLUMNS: id INT, name NOT NULL VARCHAR(256)
CREATE TABLE IF NOT EXISTS force_name(
       id INT,
       name VARCHAR(256) NOT NULL
);
