from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
        return "Hello CDA5570!"

    if __name__ == "__main__":
            app.run()
