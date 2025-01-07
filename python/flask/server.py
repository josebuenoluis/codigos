from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():
	print("DENTRO")
	return jsonify({"message": "Hello, World!"})

@app.route('/rpc',methods=['GET'])
def prueba():
	print("DENTRO")
	return jsonify({"message": "Hello, World!"})


@app.route("/rpc/Switch.Set",methods=['GET'])
def encendiendo():
    id = request.args.get('id', default=0, type=int) 
    on = request.args.get('on', default='false', type=str).lower() == 'true' 
	# Aquí puedes añadir la lógica para manejar la solicitud 
    # # Por ejemplo, podrías imprimir los valores recibidos 
    print(f"ID: {id}, On: {on}, Estado: {'encendido' if on else 'apagado'}") 
    return "",200

if __name__ == '__main__':
	app.run(port=80,host="0.0.0.0",debug=False)
