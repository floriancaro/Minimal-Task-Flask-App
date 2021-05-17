from flask import Flask

app = Flask(__name__)

# define a route decorator for the root directory of the web app
@app.route("/")
@app.route("/index")
def index(): # tell the app what to do when this path is accessed 
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
