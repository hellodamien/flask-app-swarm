from flask import Flask  
import os
import pymysql
app = Flask(__name__)  

# Function to check database connection
def check_db_connection():
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_user = os.environ.get('DB_USER', 'root')
    db_password = os.environ.get('DB_PASSWORD', '')
    db_name = os.environ.get('DB_NAME', 'test')

    try:
        connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        connection.close()
        return True
    except Exception as e:
        print("Failed to connect to database:", str(e))
        return False

@app.route('/')  
def home():  
    return "Hello, Docker Swarm! (v2)"

@app.route("/pinggy")
def pinggy():
    return "Pinggy is an Ngrok alternative https://pinggy.io/"

@app.route("/check-db")
def check_db():
    check_db_connection()
    if check_db_connection():
        return "Database connection status: OK"
    else:
        return "Database connection status: KO"

if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=5000)  
