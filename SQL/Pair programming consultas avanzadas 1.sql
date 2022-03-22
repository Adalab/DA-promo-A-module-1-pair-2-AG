USE northwind;

/*Ejercicio 1*/
SELECT MIN(Unitprice) AS lowestPrice, MAX(Unitprice) AS highestPrice
FROM products ;

/*Ejercicio 2*/
SELECT SUM(ProductID), AVG(UnitPrice)
FROM products ;

/*Ejercicio 3*/
SELECT MAX(Freight), MIN(Freight)
FROM orders
WHERE ShipCountry = "UK" ; 

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