from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle proxy requests
@app.route("/proxy", methods=["POST"])
def proxy():
    target_url = request.form.get("url")  # Get the target URL from the form
    try:
        response = requests.get(target_url)
        return response.content, response.status_code, response.headers.items()
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)
