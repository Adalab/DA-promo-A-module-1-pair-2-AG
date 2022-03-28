USE northwind;

/*Ejercicio 1*/
SELECT MAX(unit_price) AS highestPrice, MIN(unit_price) AS lowestPrices
FROM products;

/*Ejercicio 2*/
SELECT AVG(unit_price) AS precio_medio, COUNT(product_id)
FROM products;

/*Ejercicio 3*/
SELECT MAX(freight) AS max_carga, MIN(freight) AS min_carga, ship_country
FROM orders
WHERE ship_country = "UK";

/*Ejercicio 4*/
SELECT ProductID, UnitPrice
FROM products
WHERE UnitPrice >= 28.87
ORDER BY UnitPrice DESC ;

/*Ejercicio5*/
SELECT SUM(Discontinued)
FROM products 
WHERE Discontinued = 1 ;

/*Ejercicio 6*/
SELECT ProductName, ProductID, Discontinued
FROM products
ORDER BY ProductID DESC
LIMIT 10 ;