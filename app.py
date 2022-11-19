from flask import Flask
from flask import render_template
from flask import request

import pickle
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calc", methods=["POST"])
def calc():
    calc = request.form["calc"]
    with open("predict_population.pickle", mode="rb") as fp:
        model = pickle.load(fp)
    model.predict(np.array([int[calc]]))
    return render_template("calc.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
