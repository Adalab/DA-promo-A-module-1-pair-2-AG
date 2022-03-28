USE Northwind;

/*Ejercicio 1*/
SELECT employee_id, last_name, first_name
FROM employees;

/*Ejercicio 2*/
SELECT * 
FROM products
WHERE unit_price <= 5;

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
FROM products
WHERE product_id < 10 AND unit_price < 15;

/*Ejercicio 7*/
SELECT *
FROM products
WHERE NOT product_id < 10 AND NOT unit_price < 15;

/*Ejercicio 8*/
SELECT ship_city
FROM orders;