from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello, World!"

if __name__ == '__main__':
  port = int(os.environ.get('FLASK_PORT', 5000))
  app.run(port=port, debug=True)
