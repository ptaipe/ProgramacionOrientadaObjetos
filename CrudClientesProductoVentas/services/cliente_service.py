import requests
from models.cliente import Cliente

API_URL = "http://127.0.0.1:5000/clientes"

class ClienteService:

    def listar(self):
        response = requests.get(API_URL)
        return response.json()
    
    def crear(self, cliente: Cliente):
        data = {
            "nombre":cliente.nombre,
            "apellido":cliente.apellido,
            "correo":cliente.correo,
            "telefono":cliente.telefono
        }
        response = requests.post(API_URL, json=data)
        return response.status_code == 200
    
    def buscar_por_id(self, id_cliente):
        response = requests.get(f"{API_URL}/{id_cliente}")
        if response.status_code == 200:
            return response.json()
        return None
    
    def actualizar(self, cliente: Cliente):
        data = {
            "nombre":cliente.nombre,
            "apellido":cliente.apellido,
            "correo":cliente.correo,
            "telefono":cliente.telefono
        }
        response = requests.put(f"{API_URL}/{cliente.id_cliente}", json=data)
        return response.status_code == 200
    
    def eliminar(self, id_cliente):
        response = requests.delete(f"{API_URL}/{id_cliente}")
        return response.status_code == 200