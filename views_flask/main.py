from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    print("in hello function")
    return render_template("index.html")

@app.route("/<name>")
def hello_person(name):
    print("*"*80)
    print("in hello_person function")
    print(name)
    return f"Hello {name}!"

if __name__=="__main__":
    app.run(debug=True)