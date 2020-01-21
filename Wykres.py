from flask import Flask, render_template, session, make_response
from datetime import date
import locale
import Cython
import base64, random
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy
import os
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


app = Flask(__name__)
locale.setlocale(locale.LC_TIME, 'pl_PL.UTF-8')


@app.route('/')
def home():
    return render_template('PROJEKT X.html')

@app.route('/plot.png')
def generuj():
    fig = plt.figure(figsize=(6,4), dpi=300)
    axis = fig.add_subplot(1, 1, 1)

    xs = numpy.arange(166)
    ys = numpy.loadtxt("dane.txt")
    axis.plot(xs, ys,color='purple')
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
app.run(debug=True, host='0.0.0.0', port=10114)
