#!/bin/sh
set -e

# Clean cache
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

# Auto format
echo "running auto format" && yapf . --recursive --in-place --style='{based_on_style: pep8, indent_width: 4, COLUMN_LIMIT: 100}'

# Linting
echo "running pylint" && find . -type f -name "*.py" | xargs pylint

# Running Static type check
echo "running mypy static type checker" && mypy . --disallow-untyped-defs

# Unit tests
echo "running tests" && coverage run -m unittest discover . --pattern="*_test.py"

# Coverage report
echo "generating coverage report" && coverage report -m --omit=*_test.py
