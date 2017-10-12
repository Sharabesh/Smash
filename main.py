from __future__ import print_function # In python 2.7
import sys
from flask import Flask
import os
from flask import session
from flask import render_template
from flask import flash, redirect, request, abort
from flask import *
import json


from models import *



app = Flask(__name__, static_url_path='/static')
app.static_folder = 'static'




@app.route('/')
def index(fill=False):
    if not fill:
        return render_template('login.html')
    else:
        print('Hello world!', file=sys.stderr)
        return redirect(url_for('home'))

@app.route('/home')
def home():
    print("yikes")
    return render_template('ui.html')


@app.route("/login", methods = ["POST"])
def login():
    return index(True)



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
