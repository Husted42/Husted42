-- Histogram of Tweets [Twitter SQL Interview Question]
WITH countTweets AS(
  SELECT user_id, COUNT(user_id) AS tweet_bucket FROM tweets
  WHERE EXTRACT(YEAR FROM tweet_date::DATE) = 2022
  GROUP BY user_id)

SELECT tweet_bucket, COUNT(tweet_bucket) AS user_num FROM countTweets
GROUP BY tweet_bucket
ORDER BY tweet_bucket;

-- Data Science Skills [LinkedIn SQL Interview Question]
WITH filtered_candidates AS(
  SELECT candidate_id, COUNT(candidate_id) AS countSkill FROM candidates
  WHERE skill IN ('Python', 'Tableau', 'PostgreSQL')
  GROUP BY candidate_id)

SELECT candidate_id FROM filtered_candidates
WHERE countSkill = 3;

--Page With No Likes [Facebook SQL Interview Question]
SELECT page_id FROM pages
WHERE page_id NOT IN(
  SELECT page_id FROM page_likes
);

-- Unfinished Parts [Tesla SQL Interview Question]
SELECT part, assembly_step FROM parts_assembly
WHERE finish_date IS NULL;

-- Laptop vs. Mobile Viewership [New York Times SQL Interview Question]
SELECT 
  COUNT(*) FILTER(WHERE device_type = 'laptop') AS laptop,
  COUNT(*) FILTER(WHERE device_type IN('tablet', 'phone')) AS mobile_views
FROM viewership;

-- Average Post Hiatus (Part 1) [Facebook SQL Interview Question]
SELECT user_id, (MAX(post_date::DATE) - MIN(post_date::DATE)) AS days_between FROM posts
WHERE EXTRACT(YEAR FROM post_date) = 2021
GROUP BY user_id
HAVING (MAX(post_date::DATE) - MIN(post_date::DATE)) != 0;

-- Teams Power Users [Microsoft SQL Interview Question]
SELECT sender_id, COUNT(sender_id) FROM messages
WHERE EXTRACT(YEAR FROM sent_date) = 2022 AND EXTRACT(MONTH FROM sent_date) = 8
GROUP BY sender_id
ORDER BY COUNT(sender_id) DESC
LIMIT 2;

-- Duplicate Job Listings [Linkedin SQL Interview Question]
WITH dublicateList AS(
SELECT company_id, COUNT(company_id) FROM job_listings
GROUP BY company_id
HAVING COUNT(company_id) > 1)

SELECT COUNT(company_id) AS duplicate_companies FROM dublicateList;

-- Cities With Completed Trades [Robinhood SQL Interview Question]
SELECT users.city, COUNT(users.city) AS total_orders FROM trades
LEFT JOIN users ON users.user_id = trades.user_id
WHERE trades.status = 'Completed' 
GROUP BY users.city
ORDER BY COUNT(users.city) DESC
LIMIT 3;

-- Average Review Ratings [Amazon SQL Interview Question]
SELECT 
  EXTRACT(MONTH FROM submit_date) AS mth,
  product_id AS product,
  ROUND(AVG(stars), 2) AS avg_stars
FROM reviews
GROUP BY mth, product_id
ORDER BY mth, product ASC;

-- App Click-through Rate (CTR) [Facebook SQL Interview Questions]
WITH counts AS(
  SELECT 
    app_id,
    COUNT(event_type) FILTER(WHERE event_type = 'click') AS clicks,
    COUNT(event_type) FILTER(WHERE event_type = 'impression') AS impre
  FROM events
  WHERE EXTRACT(YEAR FROM timestamp::DATE) = 2022
  GROUP BY app_id)
  
SELECT
  app_id,
  ROUND((100.0 * clicks / impre), 2) AS ctr
FROM counts;

-- Second Day Confirmation [TikTok SQL Interview Question]
WITH singup_info AS (
  SELECT 
    emails.user_id, 
    (texts.action_date::DATE - emails.signup_date::DATE) AS between_ 
  FROM emails
  RIGHT JOIN texts ON texts.email_id = emails.email_id
  WHERE texts.signup_action = 'Confirmed')

SELECT user_id FROM singup_info
WHERE between_ = 1;

-- Cards Issued Difference [JPMorgan Chase SQL Interview Question]
SELECT 
  card_name, 
  (MAX(issued_amount) - MIN(issued_amount)) AS diffrence 
FROM monthly_cards_issued
GROUP BY card_name
ORDER BY diffrence DESC;

-- Compressed Mean [Alibaba SQL Interview Question]
SELECT 
  ROUND(SUM(item_count * 1.0 * order_occurrences) / SUM(order_occurrences),1) AS mean
FROM items_per_order;

-- Pharmacy Analytics (Part 1) [CVS Health SQL Interview Question]
SELECT 
  drug, 
  ROUND((total_sales*1.0-cogs),2) AS total_profit FROM pharmacy_sales
ORDER BY total_profit DESC
LIMIT 3;

-- Pharmacy Analytics (Part 2) [CVS Health SQL Interview Question]
WITH loss_per_product AS (
  SELECT 
    manufacturer,  
    (cogs - total_sales) AS loss
  FROM pharmacy_sales)
  
SELECT 
  manufacturer, 
  COUNT(manufacturer) AS drug_cout,
  SUM(loss) AS total_loss
FROM loss_per_product
WHERE loss > 1
GROUP BY manufacturer
ORDER BY total_loss DESC;

-- Pharmacy Analytics (Part 3) [CVS Health SQL Interview Question]
SELECT 
  manufacturer,
  CONCAT('$',ROUND(SUM(total_sales) / 1000000), ' million') AS sale_mil
FROM pharmacy_sales
GROUP BY manufacturer
ORDER BY SUM(total_sales) DESC;

-- User's Third Transaction [Uber SQL Interview Question]
WITH rowfilter AS(
  SELECT 
    user_id,
    spend,
    transaction_date,
    ROW_NUMBER() OVER(
    PARTITION BY user_id ORDER BY transaction_date)
  FROM transactions)

SELECT user_id, spend, transaction_date
FROM rowfilter
WHERE row_number = 3;

-- Sending vs. Opening Snaps [Snapchat SQL Interview Question]
WITH time_spent AS (
  SELECT 
    age_bucket,
    SUM(time_spent) FILTER(WHERE activity_type = 'open') AS open_time,
    SUM(time_spent) FILTER(WHERE activity_type = 'send') AS send_time
  FROM activities
  LEFT JOIN age_breakdown ON age_breakdown.user_id = activities.user_id
  GROUP BY age_bucket
  ORDER BY age_bucket ASC)

SELECT 
  age_bucket,
  ROUND((100.0 * send_time / (send_time + open_time)), 2) AS send_perc,
  ROUND((100.0 * open_time / (send_time + open_time)), 2) AS open_perc
FROM time_spent;

-- Tweets' Rolling Averages [Twitter SQL Interview Question]
SELECT user_id, tweet_date,
  ROUND(
  AVG(tweet_count) OVER(
  PARTITION BY user_id
  ORDER BY tweet_date ASC
  ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2)
FROM tweets;

-- Highest-Grossing Items [Amazon SQL Interview Question]
SELECT category, product, total_spend FROM (
  SELECT
    category,
    product,
    SUM(spend) AS  total_spend,
    RANK() OVER(
    PARTITION BY category ORDER BY SUM(spend) DESC) as ranking
  FROM product_spend
  WHERE EXTRACT(YEAR FROM transaction_date) = 2022
  GROUP BY category, product) AS A
WHERE ranking < 3;

-- Age bucket [data]
DROP TABLE IF EXISTS users;
CREATE TABLE users(
	id SERIAL,
	name VARCHAR(16),
	age INT);
	
INSERT INTO users (name, age) VALUES 
('Jens', 23), ('Hanne', 21), ('Hajken', 24),
('Aage', 50), ('Morten', 55), ('Torben', 12),
('Helle', 20), ('Dennis', 0), ('Jannic', 67);

-- Age bucket [new column]

ALTER TABLE users
ADD age_bucket VARCHAR(16);

UPDATE users
SET age_bucket = CASE 
	WHEN (age BETWEEN 0 and 20) THEN '0-20'
	WHEN (age BETWEEN 21 and 35) THEN '21-35'
	WHEN (age BETWEEN 36 and 50) THEN '36-50'
	ELSE '50+'
END;

-- Age bucket [new table]
DROP TABLE IF EXISTS age_buckets; 
CREATE TABLE age_buckets(
	id INT,
	groups VARCHAR(16)
);

INSERT INTO age_buckets (id, groups)
SELECT id, 
CASE 
	WHEN (age BETWEEN 0 and 20) THEN '0-20'
	WHEN (age BETWEEN 21 and 35) THEN '21-35'
	WHEN (age BETWEEN 36 and 50) THEN '36-50'
	ELSE '50+'
END
FROM users;

-- Age bucket [Histogram]
SELECT groups, COUNT(groups) FROM age_buckets
GROUP BY groups
ORDER BY groups;

-- Age bucket [Max age with fucntion}
CREATE OR REPLACE FUNCTION fn_find_max_age()
RETURNS INT as
$$
SELECT MAX(age)
FROM users
$$
LANGUAGE SQL;

SELECT fn_find_max_age();
----- pgexercises.com -----
-- Update some existing data
UPDATE cd.facilities
SET initialoutlay = 10000
WHERE facid = 1;

 -- Update multiple rows and columns at the same time
UPDATE cd.facilities
SET guestcost = 30, membercost = 6
WHERE name LIKE '%Tennis%';

-- Update a row based on the contents of another row
UPDATE cd.facilities SET 
	membercost = (SELECT (membercost * 1.1) FROM cd.facilities WHERE facid = 0),
	guestcost = (SELECT (guestcost * 1.1) FROM cd.facilities WHERE facid = 0)
WHERE facid = 1;

-- Delete all bookings
TRUNCATE TABLE cd.bookings;

-- Delete a member from the cd.members table
DELETE FROM cd.members
WHERE memid = 37;

-- Delete based on a subquery
DELETE FROM cd.members
WHERE memid NOT IN(
  SELECT memid FROM cd.bookings);

-- 