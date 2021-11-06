from flask import Flask, render_template
app = Flask(__name__)

@app.route('/mylist')
def mylist():
	vehicle=['Bicycle', 'Bike', 'Car', 'Jeep']
	return render_template('mylist.html', vehicle=vehicle)

@app.route('/mydict')
def mydict():
	dict1={'vehicle':'car', 'Brand':'Ford', 'Year':'1964'}
	return render_template('mydict.html', dict1=dict1)
	
if __name__ == '__main__':
    app.run(debug=True)
	
