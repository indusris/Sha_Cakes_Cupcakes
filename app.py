from flask import Flask, render_template, request, redirect, url_for, session

# Create Flask app
app = Flask(__name__)

# Secret key for session handling
app.secret_key = "your_secret_key"

# Routes

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Products page
@app.route('/products')
def products():
    return render_template('products.html')

# Add to Cart functionality
@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    # Get product data from the form
    product_name = request.form.get('product_name')
    product_price = request.form.get('product_price')

    # Initialize the cart if it doesn't exist in the session
    if 'cart' not in session:
        session['cart'] = []

    # Add the product to the cart
    session['cart'].append({'name': product_name, 'price': float(product_price)})

    # Mark session as modified to save changes
    session.modified = True

    # Redirect back to the products page
    return redirect(url_for('products'))

# Cart page to display cart items
@app.route('/cart')
def cart():
    # Get cart items from the session
    cart_items = session.get('cart', [])
    # Calculate the total price
    total_price = sum(item['price'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
