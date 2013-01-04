from app import app
from flask import render_template
from flask import request

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/bubbles",methods=['POST'])
def bubbles():
    if request.form.get('sort',None)=='Bubble Sort Execute':
	    return render_template('bubble_sort.html')
    elif request.form.get('code',None)=='Bubble Sort Code':
        return show_code()

@app.route("/bubble_sort",methods=['POST'])
def bubble_Sort():
    if request.form.get('sort',None)=='Sort':
	array_string = request.form.get('array',None)
	array = array_string.split()#convert the string into list
        array = map(int,array)#convert the string-list to int-list
	from bubble_sort import sort_array
	array = sort_array(array)
	result = ' '.join(map(str,array))
	return result

def show_code():
    code = open("app/bubble_sort.py","r")
    data = code.read()
    code.close()
    return data

