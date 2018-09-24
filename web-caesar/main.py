from flask import Flask, request


app = Flask(__name__)
app.config['DEBUG'] = True

form = '''<!DOCTYPE html>

<html>
    <head>
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

def alphabet_position(letter):
    up_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low_alpha = 'abcdefghijklmnopqrstuvwxyz'
    if letter.isupper():
        return up_alpha.index(letter)
    elif letter.islower():
        return low_alpha.index(letter)



def rotate_character(char, rot):
    new_char =''
    up_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low_alpha = 'abcdefghijklmnopqrstuvwxyz'
    if char.isalpha():
      if char.isupper():
        index = alphabet_position(char)
        new_char = up_alpha[(index+rot) % 26]
        return new_char
      if char.islower():
        index = alphabet_position(char)
        new_char = low_alpha[(index+rot) % 26]
        return new_char
    else:
        new_char = char
        return char

		
def encrypt(text, rot):
    new_text = ''
    for c in text:
        new_text += rotate_character(c,rot)
    return new_text
	

@app.route("/")
def index():
	return form.format(0, "")

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








