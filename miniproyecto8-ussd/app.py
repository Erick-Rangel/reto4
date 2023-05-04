from flask import Flask, request, render_template
import africastalking
from flask_ussd import UssdRequest, UssdResponse, ussd

app = Flask(__name__)
ussd_service = ussd(app, __name__)

# Definir ruta para recibir mensajes USSD


@ussd_service.on_request
def handle_request(req: UssdRequest):
    # Obtener datos del mensaje USSD
    session_id = req.sessionId
    phone_number = req.phoneNumber
    service_code = req.serviceCode
    text = req.text

    # Procesar el mensaje USSD
    response_text = "Bienvenido al menú de ejemplo para USSD\n"
    if text == "":
        response_text += "Selecciona una opción del 1 al 3"
    elif text == "1":
        response_text += "Has seleccionado la opción 1"
    elif text == "2":
        response_text += "Has seleccionado la opción 2"
    elif text == "3":
        response_text += "Has seleccionado la opción 3"
    else:
        response_text += "Opción no válida. Selecciona una opción del 1 al 3"

    # Devolver respuesta a Africa's Talking
    response = UssdResponse(response_text, 1)
    return response.to_dict()


# Definir ruta para recibir mensajes SMS
@app.route('/sms', methods=['POST'])
def receive_sms():
    # Obtener los datos del mensaje SMS
    message = request.values.get('text', None)
    phone_number = request.values.get('from', None)
    response = "Hemos recibido tu mensaje: " + message

    # Enviar respuesta SMS a través de Africa's Talking
    sms = africastalking.SMS
    sms.send(response, [phone_number])

    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
