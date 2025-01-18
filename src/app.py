from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/my-route', methods=['GET'])
def hello_world():
    return '<h1>Hello!</h1>'

@app.route('/todos', methods=['GET, POST'])
def todos():
    response_body = {}

    if request.method == 'GET':
        response_body['message'] = 'Listado de todos los TODOS'
        response_body['results'] = todos_list 
        return response_body, 200
    
    if request.method == 'POST':
        data = request.json
        todos_list.append(data)

        response_body['message'] = 'TODO agregado con éxito'
        response_body['results'] = todos_list

        return response_body, 201

@app.route('/todos/<int:position>', methods=['GET', 'PUT', 'DELETE'])
def todo(position):
    response_body = {}

    print('This is the position to delete: ', position)

    if request.method == 'GET':
        response_body['message'] = f'TODO en posición: {str(position)}'
        response_body['results'] = todos_list[position]
        return response_body, 200
    
    if request.method == 'PUT':
        data = request.json
        todos_list[position] = data

        response_body['message'] = f'TODO en posición "{str(position)}" modificado correctamente'
        response_body['results'] = todos_list[position]
        return response_body, 200
    
    if request.method == 'DELETE':
        del todos_list[position]

        response_body['message'] = f'TODO en posición "{str(position)}" eliminado correctamente'
        response_body['results'] = todos_list
        return response_body, 200

todos_list = [{ "label": "My first task", "done": False },
         { "label": "My second task", "done": False }]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)