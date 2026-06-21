from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Homepage Route
@app.route('/')
def home():
    return render_template('home.html')

# Products Route
@app.route('/products')
def products():
    return render_template('products.html')

# Certifications Route
@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process contact form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(f"New Contact Form Submission:\nName: {name}\nEmail: {email}\nMessage: {message}")
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)