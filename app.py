from flask import Flask, render_template
import os

# Initialize Flask application
# __name__ tells Flask where to find templates/static files
app = Flask(__name__)

# -------------------------
# ROUTES
# -------------------------

@app.route("/")
def home():
    # Renders the homepage
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


# Runs the app only when executed directly
# (not when imported by another file)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
