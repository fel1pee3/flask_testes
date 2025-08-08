from estudo import app
from flask import render_template, url_for

@app.route('/')
def home():
    usuario = 'José Felipe Fernandes Maia'
    idade = 19
    context = {
        'usuario' : usuario,
        'idade' : idade
    }
    return render_template('index.html', context=context)

@app.route('/outrarota/')
def rotadois():
    return 'Outra Rota'