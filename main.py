from flask import Flask, render_template
import os
import pathlib
from collections import OrderedDict 


app = Flask(__name__)
path = "C:/Users/jainy/Desktop/Docs/"
app.config['UPLOAD_FOLDER'] = path

@app.route('/')
def main():
	path = "C:/Users/jainy/Desktop/Docs/"
	files = os.listdir(path)
	html = {}
	for file in files:
		if (file.endswith(".html") == True):
			html[file[:-5]] = pathlib.Path(os.path.join(path, file)).as_uri()
			html_ordered = OrderedDict(sorted(html.items()))
	return render_template("index.html", files=html_ordered, length=len(html))

if __name__ == '__main__':
	app.run(debug=True)