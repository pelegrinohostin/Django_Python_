import requests

respuesta = requests.get("https://api.github.com", timeout=5)

print(respuesta.status_code)
print(respuesta.headers["content-type"])
