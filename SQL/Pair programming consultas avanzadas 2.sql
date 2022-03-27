USE northwind;
-- ejercicio 1
SELECT COUNT(order_id), MAX(freight), employee_id
FROM orders
GROUP BY employee_id ; 

-- ejercicio 2
SELECT COUNT(order_id), MAX(freight), employee_id, order_date
FROM orders
WHERE orderDate IS NOT NULL
GROUP BY orderID 
ORDER BY employeeID ;

-- ejercicio 3
SELECT DAY(order_date), MONTH(order_date), YEAR(order_date), COUNT(order_id)
FROM orders
GROUP BY order_date ;

-- ejercicio 4
SELECT MONTH(order_date), YEAR(order_date), COUNT(order_id)
FROM orders
GROUP BY MONTH(order_date), YEAR(order_date) ;

-- ejercicio 5
SELECT COUNT(DISTINCT employee_id) AS EmpleadosCiudad, city
FROM employees
GROUP BY city
HAVING COUNT(DISTINCT employee_id)>=4 ;

-- ejercicio 6
SELECT order_id, unit_price,
CASE 
     WHEN unit_price >2000 THEN 'Alto' 
     ELSE 'Bajo' 
     END AS Precio
FROM orderdetails ;