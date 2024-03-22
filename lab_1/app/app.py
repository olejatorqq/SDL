from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def execute_query(query):
    connection = psycopg2.connect(
        dbname="students",
        user="postgres",
        password="postgres",
        host="db"
    )
    cur = connection.cursor()
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    connection.close()
    return result

@app.route('/')
def index():
    query = "SELECT full_name FROM biso_01_19 WHERE id = 13"
    result = execute_query(query)
    full_name = result[0][0] if result else "Что за хрен?"
    return render_template('index.html', full_name=full_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
