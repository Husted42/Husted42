-- 1) What is the speed and storage capacity of PC's under 5000 DKK.
SELECT PC.model, PC.speed AS GHz, PC.storage AS GB FROM PC
WHERE PC.price < 5000; 

-- 2) Who manufactures mice?
SELECT DISTINCT Product.manufacturer FROM Product 
WHERE Product.model IN(
	SELECT Accessory.model FROM Accessory WHERE Accessory.type = 'mouse'
);

-- 3) Which laptops has more than 128 GB storage and how fast are they?
SELECT Product.manufacturer, Laptop.name, Laptop.speed FROM Laptop
LEFT JOIN Product 
ON Laptop.model = Product.model 
WHERE storage > 128;

-- 4) How much does the different keyboards cost?
SELECT Product.manufacturer, Keyboard.name, Accessory.price FROM Keyboard
LEFT JOIN Accessory ON Accessory.model = Keyboard.model
LEFT JOIN Product ON Keyboard.model = Product.model; 

-- 5) What is the average price of a Lenovo product?
SELECT AVG(a.price) FROM (
	SELECT Product.model, Laptop.price FROM Product 
	RIGHT JOIN Laptop ON Laptop.model = Product.model WHERE manufacturer = 'Lenovo'
	UNION
	SELECT Product.model, PC.price FROM Product 
	RIGHT JOIN PC ON PC.model = Product.model WHERE manufacturer = 'Lenovo'
	UNION
	SELECT Product.model, Accessory.price FROM Product
	RIGHT JOIN Accessory ON Product.model = Accessory.model WHERE manufacturer = 'Lenovo') a;

-- 6) Who manufatures PCs, but not Laptops?
SELECT DISTINCT Product.manufacturer FROM Product
WHERE Product.type = 'pc' 
AND Product.manufacturer NOT IN (
	SELECT Product.manufacturer FROM Product WHERE type = 'laptop');

-- 7) What is the cheapest wireless keyboard?


SELECT * FROM Product