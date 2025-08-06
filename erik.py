import requests  # Importa la librer�a requests para hacer peticiones HTTP

def trivia_fetch(number):  # Define una funci�n que recibe un n�mero
    url = f"http://numbersapi.com/{number}?json"  # Construye la URL para la API de Numbers con el n�mero dado
    response = requests.get(url)  # Realiza una petici�n GET a la URL

    if response.status_code == 200:  # Si la respuesta es exitosa (c�digo 200)
        data = response.json()  # Convierte la respuesta JSON en un diccionario de Python
        return data  # Devuelve el diccionario con la informaci�n
    else:
        return {"Error": "No se pudo obtener el dato."}  # Devuelve un mensaje de error si la petici�n falla

def main():  # Funci�n principal del programa
    try:
        numero = int(input("Escribe un n�mero y te dir� algo curioso sobre �l: "))  # Pide al usuario un n�mero y lo convierte a entero
        trivia = trivia_fetch(numero)  # Llama a la funci�n para obtener el dato curioso
        print(f"\nDato curioso: {trivia['text']}")  # Muestra el dato curioso en pantalla
    except ValueError:  # Si el usuario no escribe un n�mero v�lido
        print("Por favor, escribe un n�mero v�lido.")  # Muestra un mensaje de error

if name == "main":  # Si el archivo se ejecuta directamente
    main()  # Llama a la funci�n principal
