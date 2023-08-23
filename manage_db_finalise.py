import mysql.connector as mc

config = {
    'host': "localhost",
    'user': 'root',
    'password': 'mysql',
    'database': 'test_rest'
}
# table: client
# champs: [id_client(auto), nom_client, code_client, solde(0), etat(1)]
# fonction qui retourne la version de ma base de donnée
def getDBInfo(config):
    # requete sql
    req = "select version()"
    # Connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.execute(req)
            resultats = c.fetchone()
            return {'resultats': resultats[0]}
    return {'resultats': ""}

# fonction qui retourne tous les clients
def getAllClients(config):
    # requete sql
    req = "SELECT code_client, nom_client \
        FROM client"
    # Connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.execute(req)
            resultats = c.fetchall()
            return {'resultats': resultats}
    return {'resultats': ""}

# fonction qui permet de rechercher en fonction du nom du client
def findClientByName(config, name):
    # requete sql
    req = "SELECT code_client, nom_client \
        FROM client \
        WHERE lower(nom_client) like %s"
    params = (name.lower(), )
    # Connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.execute(req, params)
            resultats = c.fetchall()
            return {'resultats': resultats}
    return {'resultats': ""}

# fonction qui permet de rechercher en fonction du nom du client
def addNewClient(config, data):# data = {"nom_client":"pierrot", "code_client":"CL768", "solde":0.0, "etat":1}
    # requete sql
    req = "INSERT INTO client(code_client, nom_client, solde, etat) \
        VALUES (%s, %s, %s, %s)"
    params = [
        (data["code_client"], data["nom_client"], data["solde"], data["etat"])
        ]
    # Connexion et execution de la requete
    with mc.connect(**config) as db:
        with db.cursor() as c:
            c.executemany(req, params)
            db.commit() # pour persister les nouvelles données en BD
            return {'nb_ligne': c.rowcount}
    return {'nb_ligne': 0}

#Fonction pour fermer un compte client
def fermer_compte_client(config, numero_compte):
   
    try:
        connection = connect_to_database(config)
        req = f"UPDATE clients SET etat = '0' WHERE numero_compte = '{numero_compte}'"
        execute_query(connection, query)
        close_connection(connection)
        return {"message": f"Le compte {numero_compte} a été fermé avec succès."}
    except Exception as e:
        return {"message": f"Échec lors de la fermeture du compte {numero_compte}. Erreur : {str(e)}"}
    

#Fonction pour modifier les informations d'un client
def modifier_informations_client(config, numero_compte, champ_a_modifier, nouvelle_valeur):
    
    try:
        connection = connect_to_database(config)
        req = f"UPDATE clients SET {champ_a_modifier} = '{nouvelle_valeur}' WHERE numero_compte = '{numero_compte}'"
        execute_query(connection, query)
        close_connection(connection)
        return {"message": f"Le champ {champ_a_modifier} du compte {numero_compte} a été modifié avec succès."}
    except Exception as e:
        return {"message": f"Échec lors de la modification du champ {champ_a_modifier} pour le compte {numero_compte}. Erreur : {str(e)}"}

#Fonction pour ajouter de l'argent à un compte existant
def ajouter_argent_compte(config, numero_compte, montant):
    
    try:
        connection = connect_to_database(config)
        req = f"UPDATE clients SET solde = solde + {montant} WHERE numero_compte = '{numero_compte}'"
        execute_query(connection, query)
        close_connection(connection)
        return {"message": f"Le montant de {montant} a été ajouté au compte {numero_compte} avec succès."}
    except Exception as e:
        return {"message": f"Échec lors de l'ajout du montant au compte {numero_compte}. Erreur : {str(e)}"}


#Fonction pour ramener le solde à zéro
def ramener_solde_zero(config, numero_compte):
    
    try:
        connection = connect_to_database(config)
        req = f"UPDATE clients SET solde = 0 WHERE numero_compte = '{numero_compte}'"
        execute_query(connection, query)
        close_connection(connection)
        return {"message": f"Le solde du compte {numero_compte} a été ramené à zéro avec succès."}
    except Exception as e:
        return {"message": f"Échec lors de la mise à zéro du solde pour le compte {numero_compte}. Erreur : {str(e)}"}

