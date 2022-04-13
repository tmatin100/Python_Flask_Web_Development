#import flask      https://flask.palletsprojects.com/en/2.1.x/
from flask import Flask

#create a new app by createing a variable traditinally called app and invoke the Flask class constructor 
app = Flask(__name__)

#fix for codepipleine
application = app 

#create a route
@app.route('/')
def index():                  #create a function for this route 
    return 'hello'

#set envrionment variables on your python vertiual environnment flask application
# export FLASK_APP=application.py 
# export FLASK_ENV=development 
# flask run 

@app.route('/api/testimonials')
def testimonials():
    return {'testimonial': ['great', 'its ok', 'fantastic','G-Unit']}