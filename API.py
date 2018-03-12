import requests

def send_simple_message(email):
	return requests.post(
		"https://api.mailgun.net/v3/sandboxf46d7247868b438c889599874ef47b2b.mailgun.org/messages",
		auth=("api","key-b18c3b77bc9891fa99558ac96dedf2e6"),
		data={"from": "Meissane" "<mailgun@sandboxf46d7247868b438c889599874ef47b2b.mailgun.org>",
			  "to" : [email],
			  "subject":"Hi",
		      "text":"Testing email !"})

send_simple_message()