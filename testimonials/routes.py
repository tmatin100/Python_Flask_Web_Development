# we neet to import app for the routes to use it 
from testimonials import app 
from flask import render_template

testimonials = [ 
    { 
        'id': 10, 
        'name': 'Tamzidul', 
        'message': 'Your course helped me land a new job!'
        
    },

    { 
        'id': 35, 
        'name': 'Aakash', 
        'message': 'Never have I understood OOP until now'
        
    },

    { 
        'id': 40, 
        'name': 'Maitn', 
        'message': 'I watched all 200 hrs staright!'
        
    }

]

@app.route('/')
def index():                  #create a function for this route 
    #return '<h1> hello world</h1>'
    return render_template('index.html', testimonials = testimonials)

@app.route('/<id>')
def show_testimonial(id): 

    for testimonial in testimonials:
        if testimonial.get('id') == int(id):
            return render_template('testimonial.html', testimonial = testimonial)

#@app.route('/api/testimonials')
#def testimonials():
   # return {'testimonial': ['great', 'its ok', 'fantastic']}