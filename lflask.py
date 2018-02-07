from flask import Flask

app = Flask(__name__)


@app.route("/user/<int:id>")
def hello(id):
    return "<h1>hello id's %s</h1>" % id

if __name__ == "__main__":
    app.run(debug=True)

