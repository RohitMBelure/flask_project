from flask import Flask, render_template
app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
	return render_template('ifCS.html', user=name)

@app.route('/number')
def number():
	number=15
	return render_template('ifCS.html', y=number)
	
@app.route('/home')
def home():
	variable=[1, 10, 40, 54, 58, 89, 98, 143]
	return render_template('forCS.html', variable=variable)

@app.route('/base')
def base():
	list1=[125, 54, 487, 597, 998, 597, 451, 665, 71]
	list2=['rohit', 'Ram', 'shital', 'sneha', 'kartik', 'aarohi']
	list3=['ram', 457, 'True', 459, 257, 'False']
	return render_template('base.html', name='Laxmi', numbers=list1, list2=list2, list3=list3)

if __name__ == '__main__':
    app.run(debug=True)
		
