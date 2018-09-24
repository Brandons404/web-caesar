from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''<!DOCTYPE html>

<html>
    <head><p>HI</p>
		<style>
			form {{
				background-color: #eee;
				padding: 20px;
				margin: 0 auto;
				width: 540px;
				font: 16px sans-serif;
				border-radius: 10px;
			}}
			textarea {{
				margin: 10px 0;
				width: 540px;
				height: 120px;
			}}
		</style>

    </head>
    <body>
      <form action="/rotate" method="post">
	  <label for="rot">Rotate by:</label><br>
	  <input type="text" id="rot" name="rot" value="{0}" /><br>
	  <textarea id="text" name="text">{1}</textarea>
	  <input type="submit" value="sumbit" />
		
	  </form>
    </body>
</html>
'''

@app.route("/")
def index():
	return form.format("")

@app.route("/hello")
def hello():
	first_name = request.args.get("first_name")
	return '<h1>Hello, ' + first_name + '</h1>'

@app.route("/rotate", methods=["POST"])
def rotate():
	text = request.form["text"]
	rot = int(request.form["rot"])
	final = encrypt(text, rot)
	return form.format(rot, final)
	
	
app.run(port="8080")








