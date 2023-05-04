from flask import Flask, render_template, request

app = Flask(__name__)

UNIDADES = {
    0: 'cero', 1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro', 5: 'cinco', 6: 'seis', 7: 'siete', 8: 'ocho', 9: 'nueve'
}
DECENAS = {
    10: 'diez', 11: 'once', 12: 'doce', 13: 'trece', 14: 'catorce', 15: 'quince', 20: 'veinte', 30: 'treinta',
    40: 'cuarenta', 50: 'cincuenta', 60: 'sesenta', 70: 'setenta', 80: 'ochenta', 90: 'noventa'
}
CENTENAS = {
    100: 'cien', 200: 'doscientos', 300: 'trescientos', 400: 'cuatrocientos', 500: 'quinientos',
    600: 'seiscientos', 700: 'setecientos', 800: 'ochocientos', 900: 'novecientos'
}

def convertir_numero_a_palabras(numero):
    if numero < 10:
        return UNIDADES[numero]
    elif numero < 20:
        return DECENAS[numero]
    elif numero < 100:
        decena = numero // 10 * 10
        unidad = numero % 10
        if unidad == 0:
            return DECENAS[decena]
        else:
            return DECENAS[decena] + ' y ' + UNIDADES[unidad]
    elif numero == 100:
        return CENTENAS[100]
    elif numero < 1000:
        centena = numero // 100 * 100
        resto = numero % 100
        if resto == 0:
            return CENTENAS[centena]
        else:
            return CENTENAS[centena] + ' ' + convertir_numero_a_palabras(resto)
    else:
        return 'Número fuera de rango'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        numero = int(request.form['number'])
        resultado = convertir_numero_a_palabras(numero)
        return render_template('index.html', words=resultado)
    
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
