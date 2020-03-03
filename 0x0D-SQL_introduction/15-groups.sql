-- Displays each unique score in "second_table" and how many records have it
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score DESC;
