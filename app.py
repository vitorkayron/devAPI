from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
    "id": 0,
    "nome": "Vitor",
    "habilidades" : ["Python", "Flask", "Django", "HTML", "Java"]},
    {
    "id": 1,    
    "nome": "Esther",
     "habilidades": ["Vue", "HTML", "CSS", "JavaScript", "React", "SASS"]}
]

@app.route("/dev/<int:id>/", methods= ['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe'
            response = {'status': 'erro', 'mensagem':  mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return ({'status': 'sucesso', 'mensagem': 'Registro excluido!'})

@app.route("/dev/", methods=['GET', 'POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True) 