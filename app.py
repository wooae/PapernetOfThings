from flask import Flask, render_template, request, redirect, url_for, abort
app = Flask(__name__, template_folder='views')

@app.route("/papernet")
def index():
	page = "home"
	return render_template("index.html", page = page)
	
@app.route("/papernet/about")
def about():
	page = "about"
	return render_template("index.html", page = page)
	
@app.route("/papernet/market_research")
def market():
	page = "market"
	return render_template("index.html", page = page)

if __name__== '__main__':
	app.run(host = 'localhost', port = 3000, debug = True)