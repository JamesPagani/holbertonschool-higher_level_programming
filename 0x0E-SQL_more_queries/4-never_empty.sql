-- Creates a new table with a default value for a column
-- TABLE: id_not_null
-- COLUMNS: id INT DEFAULT 1, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS id_not_null(
       id INT DEFAULT 1,
       name VARCHAR(256)
);
