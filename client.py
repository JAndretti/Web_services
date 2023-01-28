#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jan 13 2023
@author: Jules Andretti
"""
import requests
import json

uri = 'https://www.gaalactic.fr/~andrettj_SEV5204E/ws/messages'

print('Veuillez entrer la méthode entre GET et POST: ')
method = input()
if method == "GET":
    print('Entrez votre login et mdp sous la forme login:mdp')
    loginPwd = input()
    loginPwd = 'Mary:Passiflore812'
    print("Veuillez entrer l'ID de l'étudiant: ")
    student = input()
    print("Veuillez entrer l'ID de l'exam: ")
    exam = input()
    print("Veuillez entrer l'ID du sensor: ")
    sensor = input()
    params = {'student': student,'exam':exam,'sensor':sensor}
    customHeaders = {'Accept': 'application/json', 'X-Auth' : loginPwd,'User-agent': 'my_client_agent/v0.0.1'}
    httpReturn = requests.get(uri, headers=customHeaders, params=params)
elif method == "POST":
    print('Entrez votre login et mdp sous la forme login:mdp')
    loginPwd = input()
    loginPwd = 'Mary:Passiflore812'
    print("Veuillez entrer l'ID de l'étudiant: ")
    student = input()
    print("Veuillez entrer l'ID de l'exam: ")
    exam = input()
    print("Veuillez entrer l'ID du sensor: ")
    sensor = input()
    print("Veuillez entrer la date et l'heure d'acquisition sous la forme YYYY-MM-DD HH:mm:ss : ")
    time = input()
    time = "2018-06-13 13:04:12"
    print("Veuillez entrer la valeur mesurée: ")
    measure = input()
    params = {'student': student,'exam':exam,'sensor':sensor,'time':time,'measure':measure}
    customHeaders = {'Accept': 'application/json', 'X-Auth': loginPwd, 'Content-type' : 'application/x-www-form-urlencoded'}
    httpReturn = requests.post(uri, headers=customHeaders, params=params)
else:
    print("Mauvaise méthode")


#

print('\nContenu de l\'en-tête de la réponse http :')
print(httpReturn.headers)
print('\nCode de retour de la réponse http :')
print(httpReturn.status_code)
if httpReturn.status_code == 200:
    print("Successful request")
    # Extraction du contenu du corps de la réponse (httpReturn.text)
    # Dans le cas présent celui-ci correspond au contenu de la collection au format json
    # puisque la valeur de l'en-tête " Accept " de la requête était " application/json "
    representationContent = httpReturn.text
    structuredRepresentationContent = json.loads(representationContent)
    # L'objet ainsi obtenu correspond un dictionnaire
    print('\nType de la structure contenant les données de la collection :')
    print(type(structuredRepresentationContent))
    print('\nContenu du corps de la réponse http :')
    print(representationContent)
    # Désérialisation de la chaîne json et créer un objet qui contient
    # les données sous une forme structurée

    print('\nContenu structuré de la collection :')
    print('CODE:',structuredRepresentationContent['code'],'\n')
    if method == "GET":
        
        try:
            len=len(structuredRepresentationContent['data'])
            for i in range(len):
                print(f"Valeur du capteur {sensor}:",structuredRepresentationContent['data'][i]['Measurement_value'],"Date Time:",structuredRepresentationContent['data'][i]['Acquisition_time'])
            print(structuredRepresentationContent['text'])
        except:
            print(structuredRepresentationContent['text'])
        
    elif method == "POST":
        print('Return:',structuredRepresentationContent['text'])
        print('Data added:',structuredRepresentationContent['data'])


elif httpReturn.status_code == 400:
    print("Bad Request, Check the parameters of your request")
elif httpReturn.status_code == 401:
    print("Unauthorized access, check your credentials")
elif httpReturn.status_code == 403:
    print("Forbidden, you don't have access to this resource")
elif httpReturn.status_code == 404:
    print("Resource not found")
elif httpReturn.status_code == 500:
    print("Internal server error, please try again later")
else:
    print("Request failed with status code :", httpReturn.status_code)

