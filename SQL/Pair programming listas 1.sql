USE Northwind;

/*Ejercicio 1*/
SELECT EmployeeID, LastName, FirstName
FROM Employees;

/*Ejercicio 2*/
SELECT * 
FROM Products
WHERE UnitPrice <= 5;

/*Ejercicio 3*/
SELECT *
FROM Products
WHERE UnitPrice >= 18 AND UnitPrice <= 20;

/*Ejercicio 4*/
SELECT *
FROM Products
WHERE UnitPrice >= 15 AND 50;

/*Ejercicio 5*/
SELECT *
FROM Products
WHERE UnitPrice IS NULL;

/*Ejercicio 6*/
SELECT *
FROM Products
WHERE ProductID < 10 AND UnitPrice < 15;

/*Ejercicio 7*/
SELECT *
FROM Products
WHERE NOT ProductID < 10 AND NOT UnitPrice < 15;

/*Ejercicio 8*/
SELECT ShipCity
FROM Orders;