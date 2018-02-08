from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/user/<int:id>")
def hello(id):
    return "<h1>hello id's %s</h1>" % id


@app.route("/")
def index():
    user_agent = request.headers.get("User-Agent")
    return "<h2>your brower is %s" % user_agent

if __name__ == "__main__":
    app.run(debug=True)

