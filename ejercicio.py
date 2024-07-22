class SistemaHCE:
    def __init__(self):
        self.usuarios = {
            "pacientes": [],
            "doctores": [],
            "administradores": []
        }

    def registrar_usuario(self, tipo, nombre):
        if tipo in self.usuarios:
            self.usuarios[tipo].append(nombre)
        else:
            print("Tipo de usuario no válido")

    def cantidad_usuarios(self, tipo):
        if tipo in self.usuarios:
            return len(self.usuarios[tipo])
        else:
            print("Tipo de usuario no válido")
            return 0

    def cantidad_total_usuarios(self):
        total = 0
        for tipo in self.usuarios:
            total += len(self.usuarios[tipo])
        return total

    def mostrar_usuarios(self):
        for tipo, lista_usuarios in self.usuarios.items():
            print(f"\n{tipo.capitalize()}:")
            for usuario in lista_usuarios:
                print(f" - {usuario}")

    def mostrar_menu(self):
        print("\nSistema de Gestión de Historia Clínica Electrónica (HCE)")
        print("1. Registrar Paciente")
        print("2. Registrar Doctor")
        print("3. Registrar Administrador de Hospital")
        print("4. Mostrar Cantidad de Usuarios")
        print("5. Mostrar Cantidad Total de Usuarios")
        print("6. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre = input("Ingrese el nombre del paciente: ")
                self.registrar_usuario("pacientes", nombre)
            elif opcion == '2':
                nombre = input("Ingrese el nombre del doctor: ")
                self.registrar_usuario("doctores", nombre)
            elif opcion == '3':
                nombre = input("Ingrese el nombre del administrador de hospital: ")
                self.registrar_usuario("administradores", nombre)
            elif opcion == '4':
                tipo = input("Ingrese el tipo de usuario (pacientes, doctores, administradores): ")
                print(f"Cantidad de {tipo}: {self.cantidad_usua1rio1s(tipo)}")
            elif opcion == '5':
                print(f"Cantidad total de usuarios: {self.cantidad_total_usuarios()}")
                self.mostrar_usuarios()
            elif opcion == '6':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida, por favor intente nuevamente.")

# Crear una instancia del sistema HCE y ejecutar el menú
sistema_hce = SistemaHCE()
sistema_hce.ejecutar()
