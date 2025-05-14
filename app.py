from flask import Flask, request, render_template, redirect
import pymysql
import os

app = Flask(__name__)

# Get DB config from environment variables
db_host = os.environ.get("DB_HOST")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_name = os.environ.get("DB_NAME")

def get_connection():
    return pymysql.connect(host=db_host,
                           user=db_user,
                           password=db_password,
                           database=db_name,
                           cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def index():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM todos")
        todos = cursor.fetchall()
    conn.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    item = request.form.get('item')
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO todos (item) VALUES (%s)", (item,))
        conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
