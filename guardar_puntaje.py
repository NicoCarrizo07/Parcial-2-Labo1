import json

class GuardarPuntaje:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.lista_puntajes = []  # lista para almacenar puntajes
        self.cargar_puntajes()    # cargar puntajes al inicializar
    
    def cargar_puntajes(self):
        try:
            with open(self.nombre_archivo, "r") as file:
                self.lista_puntajes = json.load(file)  # cargar la lista completa de puntajes
            print("Cargando su puntaje...")
        except FileNotFoundError:
            print("El archivo no existe. Se creará uno nuevo para guardar los puntajes.")
        except Exception as e:
            print(f"Error al cargar los puntajes: {str(e)}")
    
    def finalizar_juego(self, puntaje):
        nombre = input("Ingresa tu nombre: ")
        puntaje_data = {"nombre": nombre, "puntaje": puntaje}
        self.lista_puntajes.append(puntaje_data)  # agrego el nuevo puntaje a la lista
        try:
            with open(self.nombre_archivo, "w") as file:
                json.dump(self.lista_puntajes, file, indent=4)  #guarda la lista completa 
            print("Puntaje guardado correctamente.")
        except Exception as e:
            print(f"Error al guardar el puntaje: {str(e)}") #{str(e)} muestra la exception como texto