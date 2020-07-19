from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'dojo_survey_key'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show')
def show():
    return render_template("results.html")

@app.route('/createNinja', methods=['POST'])
def create_user():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/show')

if __name__=="__main__":
    app.run(debug=True)