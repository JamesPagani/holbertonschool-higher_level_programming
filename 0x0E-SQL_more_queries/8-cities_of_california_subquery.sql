-- Select all cities from the California state
-- In the database, California has an id of 1.
SELECT id, name FROM cities WHERE state_id=1 ORDER BY cities.id ASC;
