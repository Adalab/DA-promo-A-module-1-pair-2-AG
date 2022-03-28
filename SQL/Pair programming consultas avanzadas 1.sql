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
SELECT AVG(unit_price)
FROM products;

SELECT product_id, unit_price
FROM products
WHERE unit_price >= 28.87
ORDER BY unit_price DESC;

/*Ejercicio 5*/
SELECT discontinued, product_id
FROM products 
GROUP BY product_id;

/*Ejercicio 6*/
SELECT product_name, product_id, discontinued
FROM products
WHERE discontinued = 0
ORDER BY product_id DESC
LIMIT 10 ;