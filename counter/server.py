from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)

app.secret_key = 'counter_key'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
        
    return render_template("index.html")

@app.route('/destroy_session')
def resetSession():
    session.clear()
    # session.pop('key_name')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)