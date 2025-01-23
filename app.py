from flask import Flask, render_template
# import Flask and render template. render_template  function allows you to use HTML files (templates) stored in the templates folder. keeping the structure clean.

# creating flask app. app: This creates an instance of the Flask class. __name__: This is a special Python variable that represents the name of the current module.
app = Flask(__name__)

# defining routes. @app.route: This is a decorator in Flask that maps a URL (web address) to a Python function. '/': Represents the root URL of your website. For example, http://127.0.0.1:5000/ corresponds to this route.
@app.route('/')
def home():
    return render_template('home.html')

# about page
@app.route('/about')
def about():
    return render_template('about.html')

# contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# product page
@app.route('/products')
def products():
    return render_template('products.html')


#running the flask app. if __name__ == '__main__': - This ensures that the app runs only when the script is executed directly. app.run(debug=True): Starts the Flask development server.
if __name__ == '__main__':
    app.run(debug=True)
