USE northwind ;

-- Ejercicio 1
SELECT COUNT(orders.order_id), customers.company_name, customers.country
FROM orders
INNER JOIN customers
WHERE country = 'UK' 
GROUP BY customers.company_name ;

-- Ejercicio 2
SELECT customers.company_name, customers.country, COUNT(orders.order_id) AS Suma_Pedidos,  YEAR(orders.order_date)
FROM orders 
INNER JOIN customers
WHERE country = 'UK'
GROUP BY company_name ;

-- Ejercicio 3
SELECT customers.company_name, SUM(products.unit_price), SUM(products.unit_price*0.85), customers.country, COUNT(orders.order_id) AS Suma_Pedidos,  YEAR(orders.order_date)
FROM orders, products
INNER JOIN customers
WHERE country = 'UK'
GROUP BY company_name ;

-- Ejercicio 4
SELECT customers.company_name, customers.country, orders.order_id, orders.order_date
FROM orders 
INNER JOIN customers
WHERE country = 'UK'
GROUP BY company_name ;
