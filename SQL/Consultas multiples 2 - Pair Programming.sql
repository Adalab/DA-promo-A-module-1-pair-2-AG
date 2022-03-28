USE Northwind;

-- 1
SELECT orders.order_id, orders.order_date, customers.company_name
FROM orders
LEFT JOIN customers
ON orders.customer_id = customers.customer_id;

-- 2
SELECT COUNT(orders.order_id), customers.country, customers.company_name
FROM orders
RIGHT JOIN customers
ON orders.customer_id = customers.customer_id
WHERE country = "UK"
GROUP BY company_name;

-- 3
SELECT orders.order_id, orders.order_date, customers.country, customers.company_name, customers.contact_name
FROM orders
RIGHT JOIN customers
ON orders.customer_id = customers.customer_id
WHERE country = "UK";

-- 4
SELECT A.last_name AS nombre_em, A.first_name AS apellido_em, A.country AS pais_em, A.title AS titulo_em, B.last_name AS nombre_su, B.first_name AS apellido_su, B.country AS pais_su, B.title AS titulo_su
FROM employees A, employees B
WHERE A.title <> B.title
AND A.country = B.country ;

