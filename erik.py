import requests  # Importa la libreria requests para hacer peticiones HTTP

def trivia_fetch(number):  # Define una funcion que recibe un numero
    url = f"http://numbersapi.com/{number}?json"  # Construye la URL para la API de Numbers con el n�mero dado
    response = requests.get(url)  # Realiza una peticion GET a la URL

    if response.status_code == 200:  # Si la respuesta es exitosa (codigo 200)
        data = response.json()  # Convierte la respuesta JSON en un diccionario de Python
        return data  # Devuelve el diccionario con la informacion
    else:
        return {"Error": "No se pudo obtener el dato."}  # Devuelve un mensaje de error si la petici�n falla

def main():  # Funci�n principal del programa
    try:
        numero = int(input("Escribe un número y te díra algo curioso sobre el: "))  # Pide al usuario un n�mero y lo convierte a entero
        trivia = trivia_fetch(numero)  # Llama a la funcion para obtener el dato curioso
        print(f"\nDato curioso: {trivia['text']}")  # Muestra el dato curioso en pantalla
    except ValueError:  # Si el usuario no escribe un numero valido
        print("Por favor, escribe un numero valido.")  # Muestra un mensaje de error

if __name__ == "__main__":  
    main()  # Llama a la función principal 
