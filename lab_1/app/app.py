from flask import Flask, render_template
import psycopg2
import time

app = Flask(__name__)

def connect_to_db():
    max_retries = 10
    retry_delay = 5
    attempts = 0
    while attempts < max_retries:
        try:
            connection = psycopg2.connect(
                dbname="students",
                user="postgres",
                password="postgres",
                host="db"
            )
            return connection
        except psycopg2.OperationalError:
            print("Failed to connect to the database. Retrying...")
            attempts += 1
            time.sleep(retry_delay)
    raise Exception("Failed to connect to the database after several attempts.")

connection = connect_to_db()

def execute_query(query):
    cur = connection.cursor()
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    return result

@app.route('/')
def index():
    query = "SELECT full_name FROM biso_01_19 WHERE id = 13"
    result = execute_query(query)
    full_name = result[0][0] if result else "Что за хрен?"
    return render_template('index.html', full_name=full_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
