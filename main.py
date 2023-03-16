from flask import Flask, render_template, request

app = Flask('app')


@app.route('/')
def home():
	username = request.headers['X-Replit-User-Name']

	if username != "" and username != None:
		image = request.headers['X-Replit-User-Profile-Image']
		bio = request.headers['X-Replit-User-Bio']
		roles = request.headers['X-Replit-User-Roles']

		return render_template('success.html',
		                       username=username,
		                       image=image,
		                       bio=bio,
		                       roles=roles)
	return render_template('home.html')


app.run(host='0.0.0.0', port=8080)