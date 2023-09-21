from flask import Flask, jsonify, request, render_template
from flask_migrate import Migrate
from flask_cors import CORS
from models import db


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:pasword@ipserver/database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate()
db.init_app(app)
migrate.init_app(app, db)
CORS(app)

@app.route("/")
def root():
    return render_template('index.html')

@app.route('/api/test', methods = ['GET', 'POST'])
@app.route('/api/test/<int:id>', methods =['GET', 'PUT', 'DELETE'])
def test(id = None):
    if request.method == 'GET':
        return jsonify({"msg": "method GET"}), 200
    if request.method == 'POST':
        return jsonify({"msg": "method POST"}), 200
    if request.method == 'PUT':
        return jsonify({"msg": "method PUT"}), 200
    if request.method == 'DELETE':
        return jsonify({"msg": "method DELETE"}), 200
    
if __name__ == '__main__':
    app.run()     