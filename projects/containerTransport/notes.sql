-- Find the estimated emmsion from each ship
SELECT vessels.vessel_id, env_name, env_class.emmision
FROM vessels
JOIN env_class
ON vessels.env_id = env_class.env_id;


