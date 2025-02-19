from flask import Flask, render_template, request, flash, redirect, session
from flask_bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "supersecretkey"  # Required for session tracking

# Store messages in a simple list (Resets when the app restarts)
messages = []

@app.route('/', methods=['GET', 'POST'])
def home():
    session['visits'] = session.get('visits', 0) + 1  # Track user visits

    # Handle dark mode toggle
    if request.args.get("dark_mode") == "toggle":
        session['dark_mode'] = not session.get('dark_mode', False)

    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')

        if name and message:
            messages.append({'name': name, 'message': message, 'time': datetime.now().strftime("%Y-%m-%d %H:%M")})
            flash(f"Thank you, {name}! Your message has been received.", "success")
        else:
            flash("Please fill out both fields.", "danger")

    return render_template('home.html', messages=messages, visits=session['visits'], dark_mode=session.get('dark_mode', False))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
