import concurrent.futures
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=["GET"])
def hello_world():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)

    app.run(debug=True)
