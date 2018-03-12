from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask("MyApp")

def send_simple_message(email):
	return requests.post(
		"https://api.mailgun.net/v3/sandboxf46d7247868b438c889599874ef47b2b.mailgun.org/messages",
		auth=("api","key-b18c3b77bc9891fa99558ac96dedf2e6"),
		data={"from": "Meissane" "<mailgun@sandboxf46d7247868b438c889599874ef47b2b.mailgun.org>",
			  "to" : [email],
			  "subject":"Hi",
		      "text":"Testing email !"})


@app.route("/") 
def hello():
	return "Hello World yet again" 

@app.route("/<name>") 
def hello_someone(name):
	return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
	form_data = request.form
	send_simple_message(form_data["email"])
	return "Check your emails"


app.run(debug=True)

"""@app.route("/age_check", methods=["POST"])
def age_check():
	form_data = request.form
	bdatetime = form_data["bdaytime"]
	the_format = "%Y-%m-%dT%H:%M"
	parsed_time = datetime.strptime(bdatetime, the_format)
	the_age_in_days = datetime.now()-parsed_time
	the_age_in_days = the_age_in_days.days
	legal_age = 18*365
	if the_age_in_days < legal_age:
		return "You are allowed to buy booze in {0} days".format(
			legal_age - the_age_in_days)
	else:
		return "Take a trip to the booze store"
		"""
