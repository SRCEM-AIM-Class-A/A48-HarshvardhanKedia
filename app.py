from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "supersecretkey"  # Required for flash messages

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')

        if name and message:
            flash(f"Thank you, {name}! Your message has been received.", "success")
        else:
            flash("Please fill out both fields.", "danger")

    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
