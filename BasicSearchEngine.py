from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    query = ""

    if request.method == "POST":
        query = request.form["query"]

        try:
            response = requests.get(
                "https://search.sapti.me/search",
                params={
                    "q": query,
                    "format": "json"
                },
                timeout=10
            )

            data = response.json()
            results = data.get("results", [])

        except Exception as error:
            print("Error:", error)

    return render_template(
        "index.html",
        results=results,
        query=query
    )


if __name__ == "__main__":
    app.run(debug=True)
