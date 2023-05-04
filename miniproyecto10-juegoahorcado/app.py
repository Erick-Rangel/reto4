import random
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'clave_secreta'

palabras = ["python", "javascript", "ruby", "html", "css", "java", "php", "csharp", "swift", "kotlin"]

@app.route('/')
def index():
    session['vidas'] = 6
    session['palabra'] = random.choice(palabras)
    session['letras_adivinadas'] = ['_'] * len(session['palabra'])
    return render_template('index.html', letras=session['letras_adivinadas'], vidas=session['vidas'])

@app.route('/', methods=['POST'])
def juego():
    letra = request.form['letra']
    if letra in session['palabra']:
        for i in range(len(session['palabra'])):
            if letra == session['palabra'][i]:
                session['letras_adivinadas'][i] = letra
        if '_' not in session['letras_adivinadas']:
            return render_template('ganaste.html')
    else:
        session['vidas'] -= 1
        if session['vidas'] == 0:
            return render_template('perdiste.html')
    return render_template('index.html', letras=session['letras_adivinadas'], vidas=session['vidas'])

if __name__ == '__main__':
    app.run(debug=True)
