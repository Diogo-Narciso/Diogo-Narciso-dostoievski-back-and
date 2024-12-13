from flask import Flask, request, jsonify, render_template
from flask_swagger_ui import get_swaggerui_blueprint
from config import Config
from models import db, User

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.from_object(Config)
db.init_app(app)

# Criar Banco de Dados
with app.app_context():
    db.create_all()

# Documentação Swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Cadastrar usuário
@app.route('/api/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({'error': 'Dados insuficientes!'}), 400

    try:
        user = User(name=data['name'], email=data['email'], password="123456")  # Senha padrão
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'Usuário cadastrado com sucesso!'}), 201
    except Exception as e:
        return jsonify({'error': 'Erro ao cadastrar usuário'}), 500

# Buscar usuários
@app.route('/api/buscar_usuarios', methods=['GET'])
def buscar_usuarios():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])

# Deletar usuário
@app.route('/api/deletar_usuario/<int:user_id>', methods=['DELETE'])
def deletar_usuario(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'Usuário não encontrado!'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'Usuário deletado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
