from flask import Flask
import os
from flask import render_template
from flask import *
import json
from models import *


app = Flask(__name__, static_url_path='/static')
app.static_folder = 'static'




@app.route('/')
def index():
    # return '<html><body><h1>dsljgh World</h1></body></html>'

    return render_template("ui.html")

@app.route('/')
def ui():
   return render_template("ui.html")

@app.route("/helloin", methods=["POST"])
def helloin():

    k = request.form['click_val']
    val = update_count(k,1)
    return json.dumps({'status': val})

@app.route("/helloout", methods=["POST"])
def helloout():

    k = request.form['click_val']
    val = update_count(k,-1)
    return json.dumps({'status': val})

@app.route("/start", methods=["POST"])
def start():

    k = request.form['click_val']
    val = get_count(k)
    return json.dumps({'status': val})


@app.route("/capacity", methods=["POST"])
def capacity():
    k = request.form['click_val']
    val = get_capacity(k)
    return json.dumps({'status': val})



@app.route("/returnAll",methods=["GET"])
def dumpAll():
    return return_everything()

@app.route("/getNames",methods=["GET"])
def yield_names():
    return json.dumps([x.name for x in get_all_names()])






    # @app.route("/updateClick",methods=["POST"])
    # def hello():
    # 	data = json.loads(...)
    # 	x = models.doSomething(data)
    # 	if x:
    # 		return json.dumps({"success":1})
    # 	else:
    # return json.dumps({"success":0})




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
