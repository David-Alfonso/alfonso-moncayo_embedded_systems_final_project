import requests
import time

api_key = 'FAYJ0B0X2E5ZWZO9'
url = f'https://api.thingspeak.com/update?api_key={api_key}'

def enviar_a_thingspeak(field, date, data):
    try:
        data = {
            'create_at': date,
            field: data
        }
        response = requests.post(url, data=data)
        time.sleep(16)
    except Exception as e:
        print(f"Error al enviar datos a ThingSpeak: {str(e)}")

def procesar_archivo(archivo_path):
    try:
        # Abrir el archivo en modo lectura y escritura
        with open(archivo_path, 'r+') as archivo:
            # Leer todas las líneas del archivo
            lineas = archivo.readlines()

            # Procesar cada línea
            for linea in lineas:
                # Separar los datos por coma
                datos = linea.strip().split(',')

                if archivo_path == 'humidity.txt': # poner ruta completa
                    enviar_a_thingspeak('field3',datos[0],datos[1])

                elif archivo_path == 'temperature.txt':
                    enviar_a_thingspeak('field2',datos[0],datos[1])

                elif archivo_path == 'photo.txt':
                    enviar_a_thingspeak('field1',datos[0],datos[1])

                # Imprimir los datos
                #print("Datos:", datos)

            # Truncar el archivo para dejarlo en blanco
            archivo.truncate(0)

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print(f"Error: {e}")

# Llamar a la función para procesar el archivo
procesar_archivo('temperature.txt')
procesar_archivo('humidity.txt')
procesar_archivo('photo.txt')
