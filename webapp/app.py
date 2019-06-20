from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

#App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
        zone = TextField('Zone:', validators=[validators.required()])
        time = TextField('Time:', validators=[validators.required()])


	@app.route("/", methods=['GET', 'POST'])
	def hello():
		form = ReusableForm(request.form)

		print form.errors
		if request.method == 'POST':
			zone = request.form['zone']
			time = request.form['time']
			print zone + ' - ' + time

		if form.validate():
			print 'form validated'
			flash('Watering zone '+ zone + ' for ' + time + ' minutes.')
		else:
			print 'form not validated'
			flash('All form fields are required')

		return render_template('hello.html', form=form)

if __name__ == "__main__":
	app.run('0.0.0.0')
