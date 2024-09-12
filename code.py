# Hippolyte "NH35" 12/09/2024

# Changements:
# Ajout d'un input dans la console plutot qu'en variable d'environnement.
# Passage de tout les if en "Guards" (négation + retours). Cette forme permet de garder une linéarité dans le code et pas indenté à l'infini.
# Passage de SUPPORTED_MAIL_SERVICES comme disctionnaire en constante. Tu peux ajouter d'autres serveurs imap au besoin.
# Passage des mots clés en une liste KEYWORDS. Tu peux en rajouter si besoin.
# get_service utilise la distance de lvenshtein pour prévenir des faute de frappes. le nombre de faute de frappe est définissable dans MAX_TYPO
# Suppression de validate_link(). starwith renvoie déjà un booleen.
# Deplacement de la fonction process dans le __main__ (pourquoi faire une focntion ici ? avec un try except ?)
# Rennomage de mail en mailbox pour plus de compréssion.

# Rappel de code:
# Try catch permet de gérer des "Exception" qui sotn des comportements particulier du code. Il vaut mieux dire "except Exception as e" plutot que préciser le type d'exception. Car il peut y en avoir d'autres d'un autre type. "Exception" est hierarchiquement superieur (héritage) et englobe toutes les sortes.
# Il est recommandé que les fonctions ne fasse qu'une seule et unique chose. Et que le résultat attendu soit retourné. Et les résultats inatendus gérés par try catch.
# Il est recommandé de typé ces paramètres en entrée et en sortie de focntion. def fonction(param:type)->type. J'ai ajouté le type Optional[] dans les cas ou une valeur est attendue ou None. Mais de manière générale il vaut mieux éviter None.

import imaplib
import email
from email.header import decode_header
import os
import re
import requests
from requests.exceptions import RequestException
from typing import Optional
import getpass #Librairie pour input un mdp

SUPPORTED_MAIL_SERVICES = {
    'outlook': 'imap-mail.outlook.com',
    'gmail': 'imap.gmail.com',
    'yahoo': 'imap.mail.yahoo.com'
}
KEYWORDS = ['desabonnement', 'unsubscribe','se desinscrire']
MAX_TYPO = 3
MAX_TRY_SERVICE = 3 


def get_credential()-> str,str:
    """Demande l'identifiant et le mot de passe dans la console."""
    username = input("Entrez votre identifiant : ")
    password = getpass.getpass("Entrez votre mot de passe : ")
    return username, password


def levenshtein_distance(str1:str, str2:str)->int:
    """Mesure la différence entre 2 chaines de caractères"""
    n, m = len(str1), len(str2)
    if n == 0: return m
    if m == 0: return n
    dp = [[i + j if i * j == 0 else 0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
    return dp[n][m]


def get_service()->str:
    """Demande le type de messagerie à l'utilisateur"""

    cnt_loop = 0
    input_mail_service = "____"
    while input_mail_service != "" and cnt_loop <= MAX_TRY_SERVICE:
        cnt_loop += 1

        print(f"Services mail supportés : {SUPPORTED_MAIL_SERVICES.items()}")
        input_mail_service = input("Entrez votre service mail : ")

        for (mail_service, imap_server) in enumerate(SUPPORTED_MAIL_SERVICES):

            dist = levenshtein_distance(input_mail_service,mail_service)
            if dist <= MAX_TYPO:
                return mail_service

        print(f"le service mail, n'est pas reconnu ou supporté. Ré-essayez. {cnt_loop}/{MAX_TRY_SERVICE}")

    print(f"Apprends à écrire, frérot. T'abuses là.")
    exit()


def fetch_emails(mailbox) -> list:
    """Récupération des emails"""

    # Essaie de la fonction risqué
    try:
        mailbox.select("inbox")
        status, messages = mailbox.search(None, "ALL")

    # Elle plante, Retour.
    except Exception as e:
        print(f"Erreur lors de la récupération des emails : {str(e)}")
        return [] # exit() est aussi valide car le programme n'aura de toute facon rien à itérer.

    if status != 'OK':
        print("Le code de status de la recherche n'est pas OK.")
        return []

    email_ids = messages[0].split()
    return email_ids


def get_body(part) -> Optional[str]: # Je déduis que body est un str car on lui applique un .lower() qui est une méthode pour les string uniquement.
    """Transforme le body à partir du payload"""
    # Avec ce pattern, tu peux enchainer les try et des que l'un réussi, tu retourne le résultat.
    patterns = [part.get_content_charset(), "utf-8", 'ISO-8859-1'] # Note que j'ai pas vérifié si part.get_content_retournait bien un string... A rollback si ca plante.
    for pattern in patterns:
        try:
            body = part.get_payload(decode=True).decode(pattern)
            return body
        except:
            pass # Pass ne fait rien.

    return None


def is_newsletter(email_message) -> bool:
    """Vérifie si un email est une newsletter"""
    # Note : Il y a une répétition de procedure entre is_newsletter et find_unsubscribe_link. Met je connais pas assez IMAP4 pour risqué de recoder la fonction sans pouvoir la tester.

    # On garde le try englobant, car je ne connais pas le comportement de walk()
    try:
        for part in email_message.walk():
            
            # Si le content n'est pas html, on passe au suivant
            if part.get_content_type() != "text/html":
                continue
            
            body = get_body(part)

            # Si le body est None, on passe au suivant
            if body is None:
                continue

            # Si le body contient l'un des mots clés, alors c'est une newsletter
            if body.lower() in KEYWORDS:
                return True

        return False

    except Exception as e:
        print(f"Erreur lors de la vérification de la newsletter : {str(e)}")
        return False

# Trouver le lien de désabonnement
def find_unsubscribe_link(email_message) -> str: 
    try:
        for part in email_message.walk():
            
            # Si le content n'est pas html, on passe au suivant
            if part.get_content_type() != "text/html":
                continue

            body = get_body(part)

            # Si le body est None, on passe au suivant
            if body is None:
                continue

            # Cherche le premier lien ayant l'un des mots clés.
            keywords_pattern = '|'.join(re.escape(keyword) for keyword in keywords)
            match = re.search(r'href=["\'](https?://[^"\']*({keywords_pattern})[^"\']*)["\']', body, re.IGNORECASE)
            if match i not None:
                return match.group(1)

        return ""

    except Exception as e:
        print(f"Erreur lors de la recherche du lien de désabonnement : {str(e)}")
        return ""


# Suivre le lien de désabonnement
def unsubscribe(link: str)-> bool:
    # Il y a-t-il un lien ? Non, retour.
    if link is None or link == ""
        print("Aucun lien de désabonnement.")
        return False

    # Le lien est est il sécurisé https ? Non, retour.
    if link.startswith("https://"):
        print("Lien de désabonnement n'est pas sécurisé.")
        return False

    # On essaye la focntion risqué. Si ca plante, retour.
    try:
        response = requests.get(link, timeout=10)
    except Exception as e:
        print(f"Erreur lors de la requête de désabonnement : {e}")
        return False
    
    # La réponse est elle valide (code 2XX) ? Non, retour.
    if response.status_code < 200 or response.status_code >= 300:
        print(f"Échec du désabonnement. Code de statut : {response.status_code}")
        return False

    print("Désabonnement réussi.")
    return True
        




if __name__ == "__main__":
    """CODE PRINCIPALE ET POINT D'ENTRER DU PROGRAMME"""
    
    # récupère le service de l'utilsateur 
    service = get_service()
    # récupère le serveur imap associé
    imap_server = SUPPORTED_MAIL_SERVICES[service]
    # récupère les identifiants de l'utilisateur
    username, password = get_credential()

    try:
        mailbox = imaplib.IMAP4_SSL(imap_server)
        mailbox.login(username, password)
        print(f"Connexion réussie au service {service}")

    except Exception as e:
        print(f"Erreur lors de la connexion au service {service} : {str(e)}")
        exit()

    email_ids = fetch_emails(mailbox) # Pas de try, car les exceptions sont déjà traités en interne.

    total_emails = len(email_ids)
    total_success = 0

    for email_id in email_ids:

        try:
            status, data = mail.fetch(email_id, "(RFC822)")
        except Exception as e:
            print(f"Erreur lors de la récupération de l'email {email_id} : {str(e)}")
            continue

        # Si le status n'est pas OK, on passe à la boucle suivante.
        if status != 'OK':
            continue

        for response_part in data:

            # Si ce n'est pas une instance, on passe a la boucle suivante.
            if not isinstance(response_part, tuple):
                continue

            try:
                msg = email.message_from_bytes(response_part[1])
            except Exception as e:
                print(f"Erreur lors du décodage de l'email {email_id} : {str(e)}")
                # Contrairement à continue (qui passe à la boucle suivante), 
                # break stop la boucle et poursuit comee si elle etait terminé.
                break 

            if not is_newsletter(msg):
                continue

            unsubscribe_link = find_unsubscribe_link(msg)
            if unsubscribe_link is None or unsubscribe_link == "":
                print("Aucun lien de désabonnement trouvé.")    
                continue

            # Si on a échappé à tout les controles, on procède à l'objectif principal.
            print(f"Lien de désabonnement trouvé : {unsubscribe_link}")
            res = unsubscribe(unsubscribe_link)
            if res:
                total_success += 1

    print(f"Processus Terminé !")
    print(f"Nombre Desinscription : {total_success}/{total_emails}")
    exit()


