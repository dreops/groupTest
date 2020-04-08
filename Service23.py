from application import app
from flask import request, Response
from random import randit

@app.route(/random/color, methods = ['GET'])
def random_color():
    colors = ['red', 'yellow', 'green', 'orange']
    color = colors[randit(0,30)]
    return Response(color,mimetype='test/plain')


@app.route(/random/number, methods = ['GET'])
def random_number():
    return Response(randit(1,8), mimetype='test/plain')

~                                                                 
