from flask import Flask, request
import africastalking

# Configuración de las credenciales de Africa's Talking
username = "sandbox"
api_key = "84f299d4e6b0108e5568e2f50c7ee4bca18ffb5acd61c31708e3c98dbcade257"
africastalking.initialize(username, api_key)

app = Flask(__name__)

@app.route('/ussd', methods=['POST'])
def ussd_callback():
    # Obtener datos de la solicitud USSD
    session_id = request.values.get("sessionId", None)
    phone_number = request.values.get("phoneNumber", None)
    service_code = request.values.get("serviceCode", None)
    text = request.values.get("text", "")

    # Procesar la solicitud USSD
    if text == "":
        # Menú principal
        response = "CON Bienvenido al menú de mi aplicación USSD.\n"
        response += "Seleccione una opción:\n"
        response += "1. Saldo de mi cuenta\n"
        response += "2. Recargar mi cuenta\n"
        response += "3. Salir"
    elif text == "1":
        # Consultar saldo
        response = "END Su saldo actual es de $50"
    elif text == "2":
        # Solicitar monto de recarga
        response = "CON Ingrese el monto a recargar:"
    elif text.isdigit():
        # Procesar recarga
        amount = int(text)
        new_balance = 50 + amount
        response = "END Recarga exitosa de ${}. Su nuevo saldo es de ${}".format(amount, new_balance)
    elif text == "3":
        # Salir
        response = "END Gracias por usar nuestra aplicación USSD. ¡Hasta luego!"
    else:
        # Opción no válida
        response = "END Opción no válida. Inténtelo de nuevo."

    return response

if __name__ == '__main__':
    app.run(debug=True)