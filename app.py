from flask import Flask, render_template, request, redirect, url_for, abort
app = Flask(__name__, template_folder='views')

@app.route("/")
def index():
	return render_template("index.html")

if __name__== '__main__':
	app.run(host = 'localhost', port = 3000, debug = True)