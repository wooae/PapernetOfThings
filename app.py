from flask import Flask, render_template, request, redirect, url_for, abort
# from flaskext.mail import Mail, Message

app = Flask(__name__, template_folder='views')
# mail = Mail(app)

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
	
@app.route("/papernet/features")
def features():
	page = "features"
	return render_template("index.html", page = page)
	
@app.route("/papernet/contact", methods = ['GET', 'POST'])
def contact():
	page = "contact"
	message_sent = false
#	if request.method == 'POST':
#		sender_name = request.form['name']
#		sender_email = request.form['email']
#		content = request.form['message']
#		msg = Message("New message from the Papernet of Things website!", sender = (sender_name, sender_email), recipients = ["wooae@umich.edu"])
#		assert msg.sender == (sender_name + " <" + sender_email + ">")
#		msg.body = content
#		mail.send(msg)
#		message_sent = true 
	return render_template("index.html", page = page, message_sent = message_sent)

if __name__== '__main__':
	app.run(host = 'localhost', port = 3000, debug = True)