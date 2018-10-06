import json, os
from datetime import datetime
from flask import Flask, request, Response
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

def db_conn():
  return psycopg2.connect(os.environ['DB_PATH'])

with db_conn() as conn:
  with conn.cursor() as cur:
    cur.execute("CREATE TABLE IF NOT EXISTS events (id SERIAL PRIMARY KEY, device VARCHAR(255), ratio FLOAT, concentation FLOAT, timestamp TIMESTAMP)")

@app.route('/store', methods=['POST'])
def store():
  with db_conn() as conn:
    with conn.cursor() as cur:
      data = request.get_json()
      cur.execute("INSERT INTO events (device, ratio, concentation, timestamp) VALUES (%s, %s, %s, %s)", (data.get("device"), data["data"].get("ratio"), data["data"].get("concentration"), datetime.now()))
  return "ok"

@app.route('/csv')
def csv():
  def generate():
    with db_conn() as conn:
      with conn.cursor() as cur:
        res = cur.execute("SELECT timestamp, device, ratio, concentation FROM events ORDER BY timestamp DESC")
        yield "timestamp,device,ratio,concentration\n"
        for rec in cur:
          yield "{},{},{},{}\n".format(*rec)

  return Response(generate(), mimetype='text/plain')
