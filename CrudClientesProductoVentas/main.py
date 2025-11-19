#  \\pip install requests

from models.cliente import Cliente
from services.cliente_service import ClienteService

def menu():
    print("\n MENÚ CLIENTES")
    print("1. Listar Clientes")
    print("2. Crear Cliente")
    print("3. Buscar Cliente por ID")
    print("4. Actualizar Cliente")
    print("5. Eliminar Cliente")
    print("0. Salir del programa")


def main():
    
    service = ClienteService()

    while True:
       menu()
       opcion = input("Seleccion una opcion: ")
       
       if opcion == "1":        
           print("\n Listado de clientes: ")
           clientes = service.listar()
           if clientes:
               for c in clientes:
                   print(f"ID: {c['id_cliente']} | Nombre: {c['nombre']} | Correo: {c['correo']} | Teléfono: {c['telefono']} |")
           else:
               print("No hay Clientes registrados")
       elif opcion == "2":
           print("\n CREAR CLIENTE")

           nombre = input("Nombre: ")
           apellido = input("Apellido: ")
           correo = input("Correo: ")
           telefono = input("Teléfono: ")

           cliente = Cliente(None, nombre, apellido, correo, telefono)
           if service.crear(cliente):
               print("\nCliente creado correctamente.")
           else:
               print("\nX Error al crear cliente.")               
           
       elif opcion == "3":
           print("\n Buscar Cliente por ID")
           id_cliente = int(input("Ingrese ID: "))
           cliente = service.buscar_por_id(id_cliente)
           if cliente:
               telefono = int(cliente['telefono'])
               print(f"""ID: {cliente['id_cliente']} | {cliente['nombre']} {cliente['apellido']}| Correo: {cliente['correo']} | Teléfono : {telefono}|""")
           else:
               print("Cliente no encontrado.") 
       elif opcion == "4":
           print("\n ACTUALIZAR CLIENTE ")
           id_cliente = int(input("INGRESE ID DEL CLIENTE PARA ACTUALIZAR: "))
           existe = service.buscar_por_id(id_cliente)
           if not existe:
               print("Cliente no encontrado.")
               continue
           nombre = input(f"Nuevo nombre ({existe['nombre']}): ") or existe['nombre']
           apellido = input(f"Nuevo apellido ({existe['apellido']}): ") or existe['apellido']
           correo = input(f"Nuevo Correo ({existe['correo']}): ") or existe['correo']
           telefono = int(input(f"Nuevo Teléfono ({existe['telefono']}): ")) or existe['telefono']
           cliente = Cliente(id_cliente, nombre, apellido, correo, telefono)
           if service.actualizar(cliente):
               print("Cliente actualizado correctamente.")
           else:
               print("Error al actualizar cliente.")
        
       elif opcion == "5":
           print("\n Eliminar Cliente por ID")
           id_cliente = int(input("Ingrese ID: "))
           cliente = service.eliminar(id_cliente)
           if cliente:               
               print("Cliente Eliminado", id_cliente)
           else:
               print("Cliente no existe en la base de datos.") 
       elif opcion == "0":
           print("Saliendo del sistema... ")
           break        
       
if __name__ == "__main__":
    main()