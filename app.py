from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # return "Hello world"
    return "Hello world 2"

if __name__=="__main__":
    app.run()