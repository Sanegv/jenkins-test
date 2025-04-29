from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)

@app.route('/')
def home():
    return "API is running!"


def get_db_connection():
    try:
        cnx = mysql.connector.connect(user='admin', password='admin',
                              host='127.0.0.1',
                              database='testdb')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        return cnx
    return None

@app.route('/data')
def get_data():
    conn = get_db_connection()
    if conn is None:
        return "Connection error."
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route('/echo', methods=['GET'])
def echo():
    args = request.args
    result = ' '.join([args.get(arg) for arg in args])
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)