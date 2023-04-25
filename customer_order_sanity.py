from sqlglot.executor import execute
sql_str = """
SELECT
    o.order_id,
    o.order_date
FROM orders o
"""

tables = {
    "orders": [
        {"order_id": 1, "order_date": "2022-01-01", "customer_id": 1},
        {"order_id": 2, "order_date": "2022-02-01", "customer_id": 2},
        {"order_id": 3, "order_date": "2022-03-01", "customer_id": 1},
    ]
}
output = execute(sql_str,tables=tables)
print(output)