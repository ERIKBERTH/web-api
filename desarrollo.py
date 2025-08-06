import requests  # Importa la librería requests para hacer peticiones HTTP

def trivia_fetch(number):  # Define una función que recibe un número
    url = f"http://numbersapi.com/%7Bnumber%7D?json"  # Construye la URL para la API de Numbers con el número dado
    response = requests.get(url)  # Realiza una petición GET a la URL

    if response.status_code == 200:  # Si la respuesta es exitosa (código 200)
        data = response.json()  # Convierte la respuesta JSON en un diccionario de Python
        return data  # Devuelve el diccionario con la información
    else:
        return {"Error": "No se pudo obtener el dato."}  # Devuelve un mensaje de error si la petición falla

def main():  # Función principal del programa
    try:
        numero = int(input("Escribe un número y te diré algo curioso sobre él: "))  # Pide al usuario un número y lo convierte a entero
        trivia = trivia_fetch(numero)  # Llama a la función para obtener el dato curioso
        print(f"\nDato curioso: {trivia['text']}")  # Muestra el dato curioso en pantalla
    except ValueError:  # Si el usuario no escribe un número válido
        print("Por favor, escribe un número válido.")  # Muestra un mensaje de error

if name == "main":  # Si el archivo se ejecuta directamente
    main()  # Llama a la función principal
