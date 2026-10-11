import tkinter as Ventana
from datetime import datetime


class RegistroVehiculos:
    # se inicia el constructor
    def __init__(self):
        self.colorAzul = "blue"
        self.colorAmarillo = "yellow"
        self.formulario = " "
        self.entryPlaca = " "
        self.entryMarca = " "
        self.entryColor = " "
        self.entryTipo = " "
        self.labelValidacion = " "
        self.labelRegistro = " "

        # array donde se guardan los vehiculos (cada uno es un diccionario)
        self.vehiculos_registrados = []

        # lambda SIN parametros: siempre hace lo mismo, se llama con ()
        self.hora_ingreso = lambda: datetime.now().strftime("%H:%M:%S")

        # lambda CON parametros: depende del dato que se le envie
        self.campo_vacio = lambda texto: texto.strip() == ""

    def iniciar_ventana(self):
        self.formulario = Ventana.Tk()
        self.formulario.title("Registro de Vehiculos")
        self.formulario.geometry("600x750")
        self.formulario.configure(bg=self.colorAzul)
        return self.formulario

    def crear_campo(self, texto):
        # metodo para no repetir el codigo de cada label y entry
        label = Ventana.Label(self.formulario, text=texto)
        label.configure(bg=self.colorAmarillo, font=("Arial", 12, "bold"), width=25)
        label.pack(pady=5)

        entry = Ventana.Entry(self.formulario)
        entry.configure(font=("Arial", 12), width=30)
        entry.pack()

        # lambda sin parametros que llama un metodo enviandole el entry
        botonLimpiar = Ventana.Button(self.formulario, text="Limpiar campo",
                                      command=lambda: self.limpiar_campo(entry))
        botonLimpiar.pack(pady=3)
        return entry

    def iniciar_preguntas(self):
        self.entryPlaca = self.crear_campo("Placa (ABC-123):")
        self.entryMarca = self.crear_campo("Marca:")
        self.entryColor = self.crear_campo("Color:")
        self.entryTipo = self.crear_campo("Tipo (Residente/Visitante):")

        # boton sin lambda: se pasa el metodo sin parentesis
        botonGuardar = Ventana.Button(self.formulario, text="Guardar", width=20,
                                      font=("Arial", 12, "bold"), command=self.guardar_vehiculo)
        botonGuardar.pack(pady=10)

        # boton con lambda sin parametros
        botonMostrar = Ventana.Button(self.formulario, text="Mostrar registro", width=20,
                                      font=("Arial", 12, "bold"), command=lambda: self.mostrar_registro())
        botonMostrar.pack()

        self.labelValidacion = Ventana.Label(self.formulario, text="", bg=self.colorAzul,
                                             fg=self.colorAmarillo, font=("Arial", 11, "bold"))
        self.labelValidacion.pack(pady=10)

        self.labelRegistro = Ventana.Label(self.formulario, text="", bg="white", justify="left")
        self.labelRegistro.pack(pady=5)

    def tomar_datos(self):
        vehiculo = {
            "placa": self.entryPlaca.get().upper(),
            "marca": self.entryMarca.get(),
            "color": self.entryColor.get(),
            "tipo": self.entryTipo.get()
        }
        return vehiculo

    def validar_campos(self, vehiculo):
        vacios = ""
        for campo in vehiculo:
            if self.campo_vacio(vehiculo[campo]):
                vacios = vacios + campo + " "

        if vacios == "":
            return True
        else:
            self.labelValidacion.configure(text="Campos vacios: " + vacios)
            return False

    def guardar_vehiculo(self):
        # funcion general que llama los otros metodos
        vehiculo = self.tomar_datos()
        if self.validar_campos(vehiculo):
            vehiculo["hora"] = self.hora_ingreso()
            self.vehiculos_registrados.append(vehiculo)
            self.labelValidacion.configure(text="Vehiculo " + vehiculo["placa"] + " guardado")
            self.limpiar_campo(self.entryPlaca)
            self.limpiar_campo(self.entryMarca)
            self.limpiar_campo(self.entryColor)
            self.limpiar_campo(self.entryTipo)

    def mostrar_registro(self):
        texto = ""
        contador = 1
        for vehiculo in self.vehiculos_registrados:
            texto = texto + str(contador) + ". " + vehiculo["placa"] + " - " + vehiculo["marca"]
            texto = texto + " - " + vehiculo["color"] + " - " + vehiculo["tipo"]
            texto = texto + " - " + vehiculo["hora"] + "\n"
            contador = contador + 1

        if texto == "":
            texto = "No hay vehiculos registrados"

        print(texto)                                   # por consola
        self.labelRegistro.configure(text=texto)       # por interfaz

    def limpiar_campo(self, entry):
        entry.delete(0, 'end')
        print("campo borrado...")
