SELECT
    o.order_id,
    o.order_date,
    c.customer_name,
    RANK() OVER (PARTITION BY c.customer_id 
        ORDER BY o.order_date DESC) as rank
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
ORDER BY c.customer_name, o.order_date DESC;