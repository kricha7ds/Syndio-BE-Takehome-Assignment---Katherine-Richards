from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
import sqlite3
from contextlib import contextmanager

import statsmodels.api as sm
import pandas as pd

load_dotenv()

app = Flask(__name__)

@contextmanager
def db_connection():
  connection = sqlite3.connect('employees.db')
  connection.row_factory = sqlite3.Row
  try:
    yield connection
  finally:
    connection.close()

@app.route("/")
def hello():
  return "Hello, World!"

def calculate_mlr(department: str):
  with db_connection() as conn:
    try:
      sql = """
        SELECT tenure, performance, protected_class, compensation
        FROM employees
        WHERE department = ?
          AND tenure IS NOT NULL
          AND performance IS NOT NULL
          AND protected_class IS NOT NULL
          AND compensation IS NOT NULL
      """
      df = pd.read_sql_query(sql, conn, params=(department,))

      y = df.compensation
      df = pd.get_dummies(df, columns=['protected_class'], drop_first=True, dtype=int)
      X = df.drop(columns=["compensation"]).assign(const=1)

      model = sm.OLS(y, X).fit()
      pvalues = model.pvalues

      return pvalues.get('protected_class_reference', pvalues.get('protected_class_comparison'))
    except sqlite3.Error:
      return None

@app.route("/pvalue")
def pvalue():
  department = request.args.get('department', '').capitalize()

  result = calculate_mlr(department)

  if result:
    pvalue = round(result, 3)
    return jsonify({"pvalue": pvalue})
  else:
    return jsonify({"status": 404, "message": "Not Found"}), 404

if __name__ == "__main__":
  port = int(os.environ.get("FLASK_PORT", 5000))
  app.run(port=port, debug=True)
