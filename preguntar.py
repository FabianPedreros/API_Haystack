import requests

# URL de tu servicio FastAPI
url = "http://localhost:8000/responder"

# Pregunta que deseas enviar
pregunta = "¿La universidad es publica?"

# Realizar la solicitud POST
response = requests.post(url, json={"pregunta": pregunta})

# Obtener la respuesta del servidor
respuesta = response.json()["respuesta"]

# Imprimir la respuesta
print(respuesta)
