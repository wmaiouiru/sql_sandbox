from sqlglot.executor import execute
sql_str = """
SELECT
    o.order_id,
    o.order_date,
    c.customer_name,
  RANK() OVER (
    PARTITION BY c.customer_id
    ORDER BY
      o.order_date DESC
  ) as rank
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
ORDER BY c.customer_name, o.order_date DESC;
"""

tables = {
    "orders": [
        {"order_id": 1, "order_date": "2022-01-01", "customer_id": 1},
        {"order_id": 2, "order_date": "2022-02-01", "customer_id": 2},
        {"order_id": 3, "order_date": "2022-03-01", "customer_id": 1},
    ],
    "customers": [
        {"customer_name": "name 1", "customer_id": 1},
        {"customer_name": "name 2", "customer_id": 2},
    ],
}
output = execute(sql_str,tables=tables)
print(output)