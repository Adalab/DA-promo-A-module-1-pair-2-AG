USE northwind;

/*ejercicio 1*/
SELECT ProductName, UnitPrice
FROM products
ORDER BY productID
LIMIT 10 ; 

/*Ejercicio 2*/
SELECT ProductName, UnitPrice
FROM products
ORDER BY productID DESC
LIMIT 10 ;

/*Ejercicio 3*/
SELECT DISTINcT OrderID
FROM orderdetails ; 

/*Ejercicio 4*/
SELECT *
FROM orderdetails
WHERE ProductID BETWEEN 1 AND 2
LIMIT 2 ;

/*Ejercicio 5*/
SELECT UnitPrice AS ImporteTotal, productID
FROM orderdetails
ORDER BY UnitPrice DESC
LIMIT 3 ;

/*Ejercicio 6*/
SELECT Unitprice
FROM orderdetails
WHERE UnitPrice BETWEEN 5 AND 10
ORDER BY OrderID DESC
LIMIT 5 ;

/*Ejercicio 7*/
SELECT ProductName AS NombreDeCategoria
FROM products
ORDER BY productID ; 

/*Ejercicio 8*/
SELECT ShippedDate, 
OrderDate, 
OrderID,
DATE_ADD(ShippedDate, INTERVAL 5 DAY) AS FechaRetrasada,
RequiredDate
FROM orders
LIMIT 15 ; 

/*Ejercicio 9*/
SELECT ProductID, UnitPrice
FROM orderdetails
WHERE UnitPrice BETWEEN 15 AND 50 ; 

/*Ejercicio 10*/
SELECT ProductID, UnitPrice
FROM orderdetails
WHERE UnitPrice IN (18, 19, 20) ;
