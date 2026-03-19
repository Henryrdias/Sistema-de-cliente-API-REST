from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Henrylindo",
        database="sistema_clientes"
    )

@app.route('/clientes', methods=['POST'])
def criar_cliente():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)"
    values = (data['nome'], data['email'], data['telefone'])

    cursor.execute(sql, values)
    conn.commit()

    return jsonify({"msg": "Cliente criado com sucesso"}), 201

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    return jsonify(clientes)

@app.route('/clientes/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()

    sql = "UPDATE clientes SET nome=%s, email=%s, telefone=%s WHERE id=%s"
    values = (data['nome'], data['email'], data['telefone'], id)

    cursor.execute(sql, values)
    conn.commit()

    return jsonify({"msg": "Cliente atualizado"})

@app.route('/clientes/<int:id>', methods=['DELETE'])
def deletar_cliente(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM clientes WHERE id=%s", (id,))
    conn.commit()

    return jsonify({"msg": "Cliente deletado"})

if __name__ == '__main__':
    app.run(debug=True)
