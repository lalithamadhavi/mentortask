from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for simplicity (can be replaced with a database)
submissions = []

#redirects to home.html
@app.route('/')
def home():
    return render_template('home.html')

#Action performed when submit button is clicked.
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    submissions.append({'name': name, 'email': email})
    return redirect(url_for('view_submissions'))

#Redirects to submissions.html
@app.route('/submissions')
def view_submissions():
    return render_template('submissions.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)

