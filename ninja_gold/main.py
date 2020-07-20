from flask import Flask, render_template, session, request, redirect
import random
from time import gmtime, strftime
app = Flask(__name__)

app.secret_key = 'ninja_gold_key'

@app.route('/')
def index():
    if 'gold' not in session or 'gold_display' not in session:
        session['gold'] = 0
        session['gold_display'] = []
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    if 'farm' in request.form['location']:
        gold = random.randint(10,20)
        session['gold'] += gold
        session['gold_display'].append(f"Earned {gold} golds from the Farm! ({strftime('%I:%M %p', gmtime())})")        
    if 'cave' in request.form['location']:
        gold = random.randint(5,10)
        session['gold'] += gold
        session['gold_display'].append(f"Earned {gold} golds from the Cave! ({strftime('%I:%M %p', gmtime())})")
    if 'house' in request.form['location']:
        gold = random.randint(2,5)
        session['gold'] += gold
        session['gold_display'].append(f"Earned {gold} golds from the House! ({strftime('%I:%M %p', gmtime())})")
    if 'casino' in request.form['location']:
        gold = random.randint(-50,50)
        session['gold'] += gold
        if gold < 0:
            session['gold_display'].append(f"Lost {gold} golds from the Casino! ({strftime('%I:%M %p', gmtime())})")
        if gold >= 0:
            session['gold_display'].append(f"Earned {gold} golds from the Casino! ({strftime('%I:%M %p', gmtime())})")

    return redirect('/')

@app.route('/reset_gold')
def resetGold():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)