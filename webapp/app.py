from flask import Flask, render_template, flash, request, redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import thread
import sys
sys.path.append('../app')
import runsprinkler 

#App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
        zone = TextField('Zone:', validators=[validators.required()])
        time = TextField('Time:', validators=[validators.required()])


	@app.route("/", methods=['GET', 'POST'])
	def manualRun():
		form = ReusableForm(request.form)

		print form.errors
		if request.method == 'POST':
			zone = request.form['zone']
			time = request.form['time']
			print zone + ' - ' + time

		if form.validate():
			print 'form validated'
			flash('Watering zone '+ zone + ' for ' + time + ' minutes.')
                        thread.start_new_thread(runsprinkler.startWatering, (int(zone) - 1,int(time)))
		        return redirect('/showLogs')
		else:
			print 'form not validated'
			flash('All form fields are required')

		return render_template('manual.html', form=form)

	@app.route("/showLogs", methods=['GET', 'POST'])
        def showLogs():
            return render_template('showLogs.html')

	@app.route("/logs", methods=['GET', 'POST'])
	def stream():
	    def generate():
		 with open('../sprinkler.log') as f:
		    while True:
			yield f.read()
			sleep(1)

	    return app.response_class(generate(), mimetype='text/plain')

if __name__ == "__main__":
	app.run('0.0.0.0')
