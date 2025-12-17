from flask import Flask, render_template
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

FLASK_ENV = os.getenv("FLASK_ENV", "development")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv(
    "SUPABASE_ANON_KEY" if FLASK_ENV == "development" else "SUPABASE_SERVICE_KEY"
)

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError("Supabase credentials not set")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("FLASK_ENV:", FLASK_ENV)
print("SUPABASE CONNECTED:", bool(supabase))
 
@app.route("/")
def home():
    response = supabase.table("certificates").select("*").order("certid").execute()
    certificates = response.data
    return render_template("index.html", certificates=certificates)


@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
