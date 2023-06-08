import os
from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# set your own database
#db = "dbname='bank' user='postgres' host='127.0.0.1' password = 'UIS'"
db = "dbname='bank23010' user='postgres' host='127.0.0.1' password = 'password'"
conn = psycopg2.connect(db)

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route("/brewers")
def brew():
    return render_template('brew.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/test")
def test():
    cur = conn.cursor()
    cur.execute('SELECT * FROM Customers;')
    Customers = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('test.html', Customers = Customers)


if __name__ == "__main__":
    app.run(debug=True)