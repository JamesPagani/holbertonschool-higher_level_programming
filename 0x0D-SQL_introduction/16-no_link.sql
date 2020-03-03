-- Shows all records in "second_table" with non-NULL name values
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
