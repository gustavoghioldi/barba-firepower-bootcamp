# pip install requests (pypi)
import requests

class UserService:
    '''
    Obtine usuarios de un servidor publico
    servicio en: https://jsonplaceholder.typicode.com/users
    '''
    def get_all(self)->tuple:
        """_summary_

        Returns:
            tuple: _description_
        """
        r = requests.get("https://jsonplaceholder.typicode.com/users")
        return r.json(), r.status_code

    def get(self, id:int)->tuple:
        """trae usuarios por id

        Args:
            id (int): id del usuario

        Returns:
            tuple: tupla de losngitud 2 (0: trae dict, 1: status_code)
        """
        r = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
        return r.json(), r.status_code
    
us = UserService()
users_response = us.get_all()
if users_response[1] == 404:
    print("no existe la ruta del servicio")
else:
    print(users_response[0])

user_by_id = us.get(1)
print(user_by_id)
user_by_id = us.get(999999999)
print(user_by_id)

#los servicios rest se invocan por verbos. 
# GET -> traer informacion
# POST -> empuja imfpormacion al servidor
# PUT y PATCH -> Corrigen informacion en el servidor
# DELETE -> sirve para borrar informacion


