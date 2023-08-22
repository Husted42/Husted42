SELECT * FROM Laptop WHERE model IN(
	SELECT model FROM Product WHERE manufacturer = 'Acer');

SELECT * FROM Accessory;
SELECT * FROM Keyboard;