import os
from flask import Flask, jsonify
import pymysql
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.environ["DB_HOST"],
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=5
    )

@app.route("/")
def home():
    return """
    <h1>AWS 3-Tier Website</h1>
    <p>Flask Backend is running!</p>
    <p><a href="/visitors">View visitors from RDS database</a></p>
    """

@app.route("/visitors")
def visitors():
    connection = None
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, name, message, created_at "
                "FROM visitors ORDER BY id"
            )
            rows = cursor.fetchall()

        for row in rows:
            if row["created_at"]:
                row["created_at"] = row["created_at"].isoformat(sep=" ")

        return jsonify(rows)
    except Exception:
        app.logger.exception("Database request failed")
        return jsonify({"error": "Could not retrieve visitor records"}), 500
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
