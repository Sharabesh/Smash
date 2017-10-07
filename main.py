from flask import Flask
from flask import render_template
app = Flask(__name__,static_url_path='/static')
 
@app.route('/')
def index():
   return '<html><body><h1>Hello World</h1></body></html>'
 
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
