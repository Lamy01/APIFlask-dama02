# import des bibliothèques flask
from flask import Flask, request, json, jsonify

from manage_db import *
from manage_lib import *

# création de l'application rest
app = Flask(__name__)

# route ou endpoint
@app.route("/api/bonjour")
def bonjour():
    msg = direBonjour()
    return msg
    
# route qui permet de dire bonjour avec un prénom
@app.route("/api/bonjourPrenom", methods=['GET'])
def bonjourPrenom():
    data_prenom = request.args.get("prenom", default="", type=str)
    data_nom = request.args.get("nom", default="", type=str)
    msg = direBonjourPrenom(prenom=data_prenom, nom=data_nom)
    return msg

# route pour info DB
@app.route("/api/infoDB", methods=['GET'])
def infoDB():
    val = getDBInfo(config=config)
    return jsonify(val)

# route pour tous les clients
@app.route("/api/getAllClient", methods=['GET'])
def getAllClient():
    val = getAllClients(config=config)
    return jsonify(val)

# route pour rechercher un client par nom
@app.route("/api/searchByName", methods=['GET'])
def searchByName():
    name = request.args.get("name", default="", type=str)
    val = findClientByName(config=config, name=name)
    return jsonify(val)

# route pour ajouter un nouveau client
@app.route("/api/addClient", methods=['POST'])
def addClient():
    donnees = json.loads(request.data)
    val = addNewClient(config=config, data=donnees)
    return jsonify(val)

# Nouveau endpoint : Fermer un compte
@app.route("/api/fermerCompte", methods=['POST'])
def fermerCompte():
    numero_compte = request.json.get("numero_compte")
    val = fermer_compte_client(config=config, numero_compte=numero_compte)
    return jsonify(val)

# Nouveau endpoint : Modifier les informations d'un client
@app.route("/api/modifierClient", methods=['POST'])
def modifierClient():
    donnees = request.json
    val = modifier_informations_client(config=config, donnees=donnees)
    return jsonify(val)

# Nouveau endpoint : Ajouter de l'argent sur le compte
@app.route("/api/ajouterArgent", methods=['POST'])
def ajouterArgent():
    numero_compte = request.json.get("numero_compte")
    montant = request.json.get("montant")
    val = ajouter_argent_compte(config=config, numero_compte=numero_compte, montant=montant)
    return jsonify(val)

# Nouveau endpoint : Ramener le solde du client à 0
@app.route("/api/ramenerSoldeAZero", methods=['POST'])
def ramenerSoldeAZero():
    numero_compte = request.json.get("numero_compte")
    val = ramener_solde_zero(config=config, numero_compte=numero_compte)
    return jsonify(val)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3003, debug=True)
