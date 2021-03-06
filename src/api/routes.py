"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Valla, Client, Owner, Order
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend"
    }

    return jsonify(response_body), 200

@api.route("/person", methods=['POST', 'GET']) # aquí especificamos que estos endpoints aceptan solicitudes POST y GET.
def handle_person():
  if request.method == 'POST': # podemos entender qué tipo de request estamos manejando usando un condicional
    return "Se recibió un POST"
  else:
    return "Se recibió un GET"
##########################################################################################################
# Get all users 

@api.route("/user/", methods=["GET"])  
def get_all_users():

        all_users = User.query.all()  
        all_users = list(map(lambda x: x.serialize(), all_users)) #Returns a list of dictionaries
        return jsonify(all_users), 200  # list object has no attribute 'serialize'

# Handle single user:    
    
@api.route("/user/<int:id>", methods=["GET", "PUT"])  
def get_single_user(id):

    if request.method == "GET":
        single_user = User.query.get(id)  
        return jsonify(single_user.serialize()), 200

    if request.method == "PUT":
        user= User.query.get(id)
        user.name= request.json["name"]
        user.email= request.json["email"]
        user.is_active= request.json["is_active"]
        user.created= request.json["created"]
        user.role_id= request.json["role_id"]
        db.session.commit()
        return jsonify(user.serialize()), 200

# Get all vallas:

@api.route("/valla/", methods=["GET"])   
def get_vallas():

    all_vallas = Valla.query.all()
    all_vallas = list(map(lambda x: x.serialize(), all_vallas)) 
    return jsonify(all_vallas), 200

# Handle single valla:

@api.route("/valla/<int:id>", methods=["GET", "PUT"])  
def get_single_valla(id):

    if request.method == 'GET':                                           
        single_valla = Valla.query.get(id)
        return jsonify(single_valla.serialize()), 200
    
    if request.method == 'PUT':   
        valla = Valla.query.get(id)
        valla.code = request.json['code'] 
        valla.name = request.json['name']  
        valla.format = request.json['format'] 
        valla.ligth = request.json['ligth']
        valla.price_low = request.json['price_low']
        valla.price_high = request.json['price_high']
        valla.view = request.json['view']
        valla.route = request.json['route']
        valla.created = request.json['created']
        valla.comment = request.json['comment']
        valla.owner_id = request.json['owner_id']   
        db.session.commit()
        return jsonify(valla.serialize()), 200

# Get all owners:

@api.route("/owner/", methods=["GET"])   
def get_all_owners():

    all_owners = Owner.query.all()
    all_owners = list(map(lambda x: x.serialize(), all_owners)) 
    return jsonify(all_owners), 200

# Handle single owner:

@api.route("/owner/<int:id>", methods=["GET", "PUT"])  
def get_single_owner(id):

    if request.method == 'GET':                                           
        single_owner = Owner.query.get(id)
        return jsonify(single_owner.serialize()), 200
    
    if request.method == 'PUT':   
        owner = Owner.query.get(id)
        owner.name = request.json['owner_name']  
        owner.code = request.json['owner_code'] 
        owner.created = request.json['created']
        owner.phone = request.json['owner_phone']
        owner.email = request.json['owner_email'] 
        owner.company = request.json['owner_company']
        db.session.commit()
        return jsonify(owner.serialize()), 200

        
# Get all clients:

@api.route("/client/", methods=["GET"])   
def get_all_clients():

    all_clients = Owner.query.all()
    all_clients = list(map(lambda x: x.serialize(), all_clients)) 
    return jsonify(all_clients), 200

# Handle single owner:

@api.route("/client/<int:id>", methods=["GET", "PUT"])  
def get_single_client(id):

    if request.method == 'GET':                                           
        single_client = Client.query.get(id)
        return jsonify(single_client.serialize()), 200
    
    if request.method == 'PUT':   
        client = Owner.query.get(id)
        client.name = request.json['client_name']  
        client.code = request.json['client_code'] 
        client.created = request.json['created']
        client.phone = request.json['client_phone']
        client.email = request.json['client_email'] 
        client.company = request.json['client_company']
        db.session.commit()
        return jsonify(client.serialize()), 200





   
   