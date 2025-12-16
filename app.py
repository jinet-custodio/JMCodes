from flask import Flask, render_template
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv()  # Load .env file
print(os.environ.get("SUPABASE_DB_URL_DEV"))
print("FLASK_ENV:", os.getenv("FLASK_ENV"))

app = Flask(__name__)

# Determine which DB to use
FLASK_ENV = os.getenv("FLASK_ENV", "development")
DB_URL = os.getenv("SUPABASE_DB_URL_DEV" if FLASK_ENV=="development" else "SUPABASE_DB_URL_PROD")

def get_db_connection():
    conn = psycopg2.connect(DB_URL, cursor_factory=RealDictCursor)
    return conn


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


# Runs the app only when executed directly
# (not when imported by another file)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
