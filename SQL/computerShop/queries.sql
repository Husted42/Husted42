SELECT * FROM laptop;
SELECT * FROM pc;
SELECT * FROM printer;
SELECT * FROM product;

-- a) Find the model number, speed, and hard-disk size for all PCs whose price is under $1000 where
-- your rename the speed column to GHz and the hd column to GB.
SELECT pc.model, pc.speed AS GHz, pc.hd AS GB FROM pc
WHERE pc.price < 1000; 

-- b) Find the manufacturers of printers
SELECT DISTINCT product.maker FROM product 
WHERE product.model IN(
	SELECT printer.model FROM printer
);

-- c) Find the manufacturer and speed of laptops with a hard disk of at least thirty gigabytes.
SELECT laptop.model, product.maker, laptop.speed FROM laptop
LEFT JOIN product
ON laptop.model = product.model 
WHERE hd > 30;

-- d) Find the model number and price of all products (of any type) made by manufacturer B.
SELECT product.model, laptop.price FROM product 
RIGHT JOIN laptop ON laptop.model = product.model WHERE maker = 'B'
UNION
SELECT product.model, pc.price FROM product 
RIGHT JOIN pc ON pc.model = product.model WHERE maker = 'B'
UNION
SELECT product.model, printer.price FROM product 
RIGHT JOIN printer ON printer.model = product.model WHERE maker = 'B';

-- e) Find those manufacturers that sell Laptops, but not PCs 
SELECT DISTINCT product.maker, product.type
FROM product
WHERE product.type = 'laptop' 
AND product.maker NOT IN (SELECT maker FROM product WHERE type = 'pc')

-- f) Find the laptops whose speed is slower than that of any PC
SELECT * FROM laptop
WHERE laptop.speed < (
	SELECT MIN(speed) FROM PC
)

-- g) Find the maker of the color printer with the lowest price
SELECT product.maker FROM product WHERE product.model IN(
	SELECT printer.model FROM printer WHERE printer.price IN(
		SELECT MIN(printer.price) FROM printer WHERE printer.color = true))

-- h


-- i

-- j) Find the manufacturers that make at least three different models of PC
SELECT product.maker, COUNT(product.type)
FROM product WHERE product.type = 'pc'
GROUP BY product.maker
HAVING COUNT(product.type) > 2

-- k

-- l

	

