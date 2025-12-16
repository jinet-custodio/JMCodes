from flask import Flask, render_template
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv()

app = Flask(__name__)

# Environment
FLASK_ENV = os.getenv("FLASK_ENV", "development")

DB_URL = os.getenv(
    "DATABASE_URL_DEV" if FLASK_ENV == "development" else "DATABASE_URL_PROD"
)

if not DB_URL:
    raise RuntimeError("Database URL not set. Check your .env file.")

def get_db_connection():
    return psycopg2.connect(DB_URL, cursor_factory=RealDictCursor)

@app.route("/")
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM certificates ORDER BY id;")
    certificates = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", certificates=certificates)

@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
