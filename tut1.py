from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/about")
def hitesh():
    name = 'Subham'
    return render_template('about.html',name=name)


@app.route("/bootstrap")
def boostrap():
    return render_template('boostrap.html')


app.run(debug=True)