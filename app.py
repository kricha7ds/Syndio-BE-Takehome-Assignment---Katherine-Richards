from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
import sqlite3
from contextlib import contextmanager

load_dotenv()

app = Flask(__name__)
VALID_DEPARTMENTS=[]

@contextmanager
def db_connection():
  connection = sqlite3.connect('employees.db')
  connection.row_factory = sqlite3.Row # give access to row results
  try:
    yield connection
  finally:
    connection.close()

@app.route("/")
def hello():
  return "Hello, World!"

def calculate_mlr(department): # Multiple linear regression
  return

@app.route("/pvalue")
def pvalue():
  department = request.args.get('department', '').capitalize()

  results = calculate_mlr(department)

  # return jsonify({"pvalue": results})
  return jsonify({"success": "success"})

if __name__ == '__main__':
  port = int(os.environ.get('FLASK_PORT', 5000))
  app.run(port=port, debug=True)
