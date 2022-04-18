#import flask      https://flask.palletsprojects.com/en/2.1.x/patterns/packages/
from flask import Flask

#create a new app by createing a variable traditinally called app and invoke the Flask class constructor 
app = Flask(__name__)
application = app 

#import the routes from the route file 
import testimonials.route