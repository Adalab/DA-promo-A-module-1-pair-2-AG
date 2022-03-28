USE Northwind;

/*ejercicio 1*/
SELECT product_name, unit_price
FROM products
ORDER BY product_id
LIMIT 10 ; 

/*Ejercicio 2*/
SELECT product_name, unit_price
FROM products
ORDER BY product_id DESC
LIMIT 10 ;

/*Ejercicio 3*/
SELECT DISTINcT order_id
FROM orderdetails ; 

/*Ejercicio 4*/
SELECT *
FROM orderdetails
WHERE product_id BETWEEN 1 AND 2
LIMIT 2 ;

/*Ejercicio 5*/
SELECT unit_price AS importeTotal, product_id
FROM orderdetails
ORDER BY unit_price DESC
LIMIT 3 ;

/*Ejercicio 6*/
SELECT unit_price
FROM orderdetails
WHERE unit_price BETWEEN 5 AND 10
ORDER BY order_id DESC
LIMIT 5 ;

/*Ejercicio 7*/
SELECT product_name AS NombreDeCategoria
FROM products
ORDER BY product_id ; 

/*Ejercicio 8*/
SELECT shipped_date, 
order_date, 
order_id,
DATE_ADD(shipped_date, INTERVAL 5 DAY) AS FechaRetrasada,
required_date
FROM orders
LIMIT 15 ; 

/*Ejercicio 9*/
SELECT product_id, unit_price
FROM orderdetails
WHERE unit_price BETWEEN 15 AND 50 ; 

/*Ejercicio 10*/
SELECT product_id, unit_price
FROM orderdetails
WHERE unit_price IN (18, 19, 20) ;
