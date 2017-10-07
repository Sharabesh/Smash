from flask import Flask
from flask import render_template
app = Flask(__name__,static_url_path='/static')
 
@app.route('/')
def index():
   return '<html><body><h1>Hello World</h1></body></html>'
 
if __name__ == "__main__":
    app.run()