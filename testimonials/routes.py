# we neet to import app for the routes to use it 
from testimonials import app 
from flask import render_template, abort, url_for

testimonials = [ 
    { 
        'id': 10, 
        'name': 'Tamzidul', 
        'message': 'Your course helped me land a new job!'
        
    },

    { 
        'id': 20, 
        'name': 'Aakash', 
        'message': 'Never have I understood OOP until now'
        
    },

    { 
        'id': 30, 
        'name': 'Maitn', 
        'message': 'I watched all 200 hrs staright!'
        
    }

]

@app.route('/')
@app.route('/testimonials')
def show_testimonial():                  #create a function for this route 
    #return '<h1> hello world</h1>'
    return render_template('index.html', testimonials = testimonials)

@app.route('/get/testimonials/<id>')
def show_testimonial(id):

    for testimonial in testimonials:
        if testimonial.get('id') == int(id):
            return render_template('testimonial.html', testimonial=testimonial)
    abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e, title="Page Not Found"), 404



#@app.route('/api/testimonials')
#def testimonials():
   # return {'testimonial': ['great', 'its ok', 'fantastic']}