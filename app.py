from flask import Flask, render_template, url_for
from counting.integrals import IntegralMethods

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/integral/<a>/<b>")
def integral(a, b):
    i = IntegralMethods()
    r1 = i.parabola(int(a), int(b))
    r2 = i.trapeze(int(a), int(b))
    return render_template("integral.html", res1=r1, res2=r2)


# if __name__ == "__main__":
#     app.run(debug=True)