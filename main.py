from src import apprun
from flask import render_template as render
from src.heart.heartSistem import *
app = apprun()
@app.route('/')
def index():  
    return render('index.html')

@app.errorhandler(404)
def notfound(error):
    return render('errors/error404.html',error = error)

@app.errorhandler(500)
def internalserveererror(error):
    return render('errors/error500.html')


if __name__ == '__main__':
    app.run(debug=True)