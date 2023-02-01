-- Rstudio data
SELECT lenght, env_id  FROM vessels
INTO OUTFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\filename.csv'
FIELDS TERMINATED BY '';

-- Find the average emmsion from each ship
SELECT vessels.vessel_id, env_class.emmision
FROM vessels
JOIN env_class
ON vessels.env_id = env_class.env_id;

-- Get tabel of vessel_id, routes.goods_amout, env_class.emmision
SELECT routes.vessel_id, routes.goods_amount, env_class.emmision
FROM routes
INNER JOIN env_class
ON routes.vessel_id = env_class.env_id;

-- Total emmision
-- Lenght
-- goodsamout
SELECT routes.vessel_id, env_class.emmision
FROM routes
INNER JOIN env_class
ON routes.vessel_id = env_class.env_id;
