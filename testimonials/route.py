# we neet to import app for the routes to use it 
from testimonials import app 
from flask import render_template

@app.route('/')
def index():                  #create a function for this route 
    #return '<h1> hello world</h1>'
    return render_template('index.html')


@app.route('/api/testimonials')
def testimonials():
    return {'testimonial': ['great', 'its ok', 'fantastic']}