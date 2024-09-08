import imaplib
import email
from email.header import decode_header
import os
import re
import requests
from requests.exceptions import RequestException

# Récupérer les identifiants depuis les variables d'environnement
username = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASS")

if username is None or password is None:
    print("Erreur : les variables d'environnement ne sont pas définies.")
else:
    print("Les variables d'environnement sont correctement récupérées.")

# Connexion à la boîte email en fonction du service
def connect_to_email(service):
    if service == "outlook":
        imap_server = "imap-mail.outlook.com"
    elif service == "gmail":
        imap_server = "imap.gmail.com"
    elif service == "yahoo":
        imap_server = "imap.mail.yahoo.com"
    else:
        raise ValueError("Service non pris en charge. Utilisez 'outlook', 'gmail', ou 'yahoo'.")

    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(username, password)
        print(f"Connexion réussie au service {service}")
        return mail
    except imaplib.IMAP4.error as e:
        print(f"Erreur lors de la connexion au service {service} : {str(e)}")
        return None

# Récupération des emails
def fetch_emails(mail):
    try:
        mail.select("inbox")
        status, messages = mail.search(None, "ALL")
        if status == 'OK':
            email_ids = messages[0].split()
            return email_ids
        else:
            print("Erreur lors de la recherche des emails.")
            return []
    except Exception as e:
        print(f"Erreur lors de la récupération des emails : {str(e)}")
        return []

# Vérifie si un email est une newsletter
def is_newsletter(email_message):
    try:
        for part in email_message.walk():
            if part.get_content_type() == "text/html":
                charset = part.get_content_charset() or "utf-8"
                try:
                    body = part.get_payload(decode=True).decode(charset)
                except UnicodeDecodeError:
                    print(f"Erreur de décodage avec {charset}, tentative avec 'ISO-8859-1'.")
                    body = part.get_payload(decode=True).decode('ISO-8859-1')

                if "unsubscribe" in body.lower() or "se désinscrire" in body.lower() or "désabonnement" in body.lower():
                    return True
        return False
    except Exception as e:
        print(f"Erreur lors de la vérification de la newsletter : {str(e)}")
        return False

# Trouver le lien de désabonnement
def find_unsubscribe_link(email_message):
    try:
        for part in email_message.walk():
            if part.get_content_type() == "text/html":
                charset = part.get_content_charset() or "utf-8"
                try:
                    body = part.get_payload(decode=True).decode(charset)
                except UnicodeDecodeError:
                    print(f"Erreur de décodage avec {charset}, tentative avec 'ISO-8859-1'.")
                    body = part.get_payload(decode=True).decode('ISO-8859-1')

                match = re.search(r'href=["\'](https?://[^"\']*(unsubscribe|se.désinscrire)[^"\']*)["\']', body, re.IGNORECASE)
                if match:
                    return match.group(1)
        return None
    except Exception as e:
        print(f"Erreur lors de la recherche du lien de désabonnement : {str(e)}")
        return None

# Valider le lien avant de le suivre
def validate_link(link):
    try:
        if link and link.startswith("https://"):
            return True
        print("Lien de désabonnement non sécurisé ou incorrect.")
        return False
    except Exception as e:
        print(f"Erreur lors de la validation du lien : {str(e)}")
        return False

# Suivre le lien de désabonnement
def unsubscribe(link):
    if validate_link(link):
        try:
            response = requests.get(link, timeout=10)
            if response.status_code == 200:
                print("Désabonnement réussi.")
            else:
                print(f"Échec du désabonnement. Code de statut : {response.status_code}")
        except RequestException as e:
            print(f"Erreur lors de la requête de désabonnement : {str(e)}")
    else:
        print("Lien de désabonnement non valide ou non sécurisé.")

# Traiter les emails
def process_newsletters(mail):
    email_ids = fetch_emails(mail)
    for email_id in email_ids:
        try:
            status, data = mail.fetch(email_id, "(RFC822)")
            if status == 'OK':
                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])

                        if is_newsletter(msg):
                            unsubscribe_link = find_unsubscribe_link(msg)
                            if unsubscribe_link:
                                print(f"Lien de désabonnement trouvé : {unsubscribe_link}")
                                unsubscribe(unsubscribe_link)
                            else:
                                print("Aucun lien de désabonnement trouvé.")
        except Exception as e:
            print(f"Erreur lors du traitement de l'email {email_id} : {str(e)}")

# Connexion au service email et traitement
if __name__ == "__main__":
    # Définissez votre service de messagerie : "outlook", "gmail", ou "yahoo"
    service = "outlook"  # Par exemple, remplacez par "gmail" ou "yahoo"
    
    if username and password:
        mail = connect_to_email(service)
        if mail:
            process_newsletters(mail)
        else:
            print("Impossible de traiter les emails. La connexion a échoué.")
    else:
        print("Impossible de se connecter à l'email car les identifiants ne sont pas définis.")
