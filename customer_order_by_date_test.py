from sqlglot.executor import execute
import sqlfluff
from sqlfluff.core import FluffConfig, Linter
import sqlglot
print(sqlglot.__version__)

def read_file(input_file):
  with open(input_file, "r") as f:
    return f.read()


sql_str = read_file('./customer_order_by_date.sql')
fluff_config = FluffConfig.from_path('./setup.cfg')
lint_result = sqlfluff.lint(sql_str, config_path='./setup.cfg', dialect="ansi")
print(lint_result)
print(sql_str)
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
output=  execute(sql_str,tables=tables)
print(output)