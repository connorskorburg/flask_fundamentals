from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:rows>')
def checkerRow(rows):
    return render_template("index.html", rows=rows, columns=1)

@app.route('/<int:rows>/<int:columns>')
def checkerRowColumn(rows, columns):
    return render_template("index.html", rows=rows, columns=columns)

@app.route('/<int:rows>/<int:columns>/<color1>')
def checkerColorOne(rows, columns, color1):
    return render_template("index.html", rows=rows, columns=columns, color1=color1)

@app.route('/<int:rows>/<int:columns>/<color1>/<color2>')
def checkerColorTwo(rows, columns, color1, color2):
    return render_template("index.html", rows=rows, columns=columns, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)