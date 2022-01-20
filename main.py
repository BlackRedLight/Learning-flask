from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('index.html')

@app.route('/works')
def works_page():
	return render_template('works.html')

@app.route('/about')
def about_page():
	return render_template('about.html')

@app.route('/contact')
def contact_page():
	return render_template('contact.html')

@app.route('/components')
def components_page():
	return render_template('components.html')

@app.route('/work')
def work_page():
	return render_template('components.html')