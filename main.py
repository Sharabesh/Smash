from flask import Flask
import os
from flask import render_template
app = Flask(__name__,static_url_path='/static')

from models import *
 
@app.route('/')
def index():
   return '<html><body><h1>dsljgh World</h1></body></html>'

   return render_template("index.html")



@app.route("/hello",methods=["GET"])
def hellpsdkgh():
	if method == "GET":
		return json.dumps({"success":1})

@app.route("/updateClick",methods=["POST"])
def hello():
	data = json.loads(...)
	x = models.doSomething(data)
	if x:
		return json.dumps({"success":1})
	else:
		return json.dumps({"success":0})

"""
$.ajax({
		type:"POST",
		url: "updateClick",
		"DATA": {
			"click":1
		}
	}).then(function(data) {
		if (data.success == 1) {
			doyourupdate(); 
		}

	})

 """
























if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
