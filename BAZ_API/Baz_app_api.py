from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

#Endpoint para obtener la infomación de un usuario por su ID
@app.route('/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
    #Establecer la comunicación a la BAse de datos
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM user WHERE id=?', (user_id,))
    user = cursor.fetchone()
    #Cerrar la conexión
    cursor.close()
    conn.close()

    if user is None:
        return jsonify({'message': 'Usuario no encontrado'}), 404

    #Convertir la información del usuario en un diccionario
    user_data = {'id':user[0],
                 'name': user[1],
                 'email': user[2]
                 }
    return jsonify(user_data)

#Endpoint para crear los datos de un usuario
@app.route('/users', methods=['POST'])
def create_user():
    #Obtener los datos del neuvo usuario desde el cuerpo(body) de la solicitud
    data = request.get_json()
    name = data['name']
    email = data['email']

    #Establecemos la conexión a la BD
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    #Insertar los datos del nuevo usuario en la base de datos
    cursor.execute('INSERT INTO user(name, email) VALUES (?,?)', (name, email))
    conn.commit()

    #Obtener el ID del nuevo usuario creado
    user_id = cursor.lastrowid

    #Cerrar la conexión con la base de datos
    cursor.close()
    conn.close()

    #Devolver una respuesta exitosa con el ID del uevo usuario creado
    return  jsonify({'message': 'Usuario creado exitosamente', 'id': user_id})

if __name__== '__main__':
    #Crear la tabla de usuarios en la base de datos(nota:solo para fines de prueba
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, email TEXT)')
    cursor.close()
    #Ejecutar la aplicación
    app.run()



