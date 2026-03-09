-- Total orders
SELECT COUNT(*) AS total_orders
FROM qudyan_orders;

-- Total revenue
SELECT SUM(order_amount) AS total_revenue
FROM qudyan_orders
WHERE order_status = 'delivered';

-- Average order value
SELECT AVG(order_amount) AS average_order_value
FROM qudyan_orders;

-- Order status distribution
SELECT order_status, COUNT(*) AS total_orders
FROM qudyan_orders
GROUP BY order_status
ORDER BY total_orders DESC;

-- Payment status distribution
SELECT payment_status, COUNT(*) AS total_orders
FROM qudyan_orders
GROUP BY payment_status
ORDER BY total_orders DESC;

-- Orders by type
SELECT order_type, COUNT(*) AS total_orders
FROM qudyan_orders
GROUP BY order_type
ORDER BY total_orders DESC;

-- Orders by day
SELECT delivery_date, COUNT(*) AS total_orders
FROM qudyan_orders
GROUP BY delivery_date
ORDER BY delivery_date;
