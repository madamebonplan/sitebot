# BONJOUUUR !

Voici les 5 étapes à suivre pour créer votre propre bot (gratuitement) qui vous permettra de vous désinscrire automatiquement de tous les sites qui vous envoient des mails chiants :

> **Note :** Pour Gmail, un autre tutoriel arrivera car c’est un peu plus compliqué.

Ouvrez le lien sur PC pour avoir une meilleure qualité d’image.  
Si d’autres personnes s’y connaissent en code, n’hésitez pas à me DM pour d’éventuelles améliorations.

## Guide : Créer un bot Python pour se désinscrire des newsletters (Outlook, Yahoo)

### Objectif du bot :
- Se connecter à une boîte email via IMAP (Outlook, Yahoo).
- Parcourir les emails pour détecter les newsletters.
- Suivre le lien de désabonnement pour tenter de se désabonner automatiquement.

### Prérequis :
- Python 3.x installé sur votre machine.
- Une adresse email Outlook ou Yahoo.

### Étape 1 : Installer Python et les dépendances
Si vous n'avez pas encore Python, téléchargez-le et installez-le depuis [python.org](https://www.python.org/downloads/).

Ensuite, installez les bibliothèques Python nécessaires en ouvrant un terminal ou une invite de commandes et en exécutant les commandes suivantes :

![Capture d’écran 2024-09-05 143052](https://github.com/user-attachments/assets/fc1b9b61-6012-4c3e-a696-38bb8ba549b9)

### Étape 2 : Configurer les identifiants avec des variables d'environnement

#### Sous Windows :
- Ouvrez le menu Démarrer et tapez "Variables d'environnement".
- Cliquez sur **Modifier les variables d'environnement du système**.
- Dans la fenêtre **Variables d'environnement**, sous **Variables utilisateur**, cliquez sur **Nouveau**.
- Créez deux nouvelles variables :
  - `EMAIL_USER` : votre adresse email (Outlook, Yahoo).
  - `EMAIL_PASS` : votre mot de passe email.

#### Sous Mac/Linux :
- Ouvrez un terminal.
- Ajoutez vos identifiants à la fin de votre fichier `.bashrc` ou `.zshrc` :
![Capture d’écran 2024-09-05 143137](https://github.com/user-attachments/assets/05ecb932-9c34-4e47-893f-44340aaf2916)


### Étape 4 : Créer et configurer le script Python
Ouvrez un éditeur de texte (comme Visual Studio Code, Sublime Text, ou même Notepad) et créez un fichier `unsubscribe_bot.py`. Collez le code suivant dans ce fichier. Vous devrez ajuster la variable `service` en fonction du fournisseur de messagerie que vous utilisez (Outlook, Gmail, ou Yahoo).

**Code à copier :**
> Là, le code est par défaut sur `service = "outlook"`.  
> C’est tout en bas du code et c’est cela que vous devrez changer en fonction de votre service (par exemple `service = "yahoo"` pour Yahoo).

![Capture d’écran 2024-09-05 144022](https://github.com/user-attachments/assets/c251226c-addc-4f71-8638-7f13b6a3d49a)

### Étape 5 : Lancer le bot
- Faites un clic droit sur le dossier et sélectionnez **Ouvrir dans le terminal**.
  
 ![IMG_2865](https://github.com/user-attachments/assets/6c1d66fb-15de-4b62-aa8c-f7304344db14)

- Puis écrire “python [nom du fichier]” donc pour moi c’est : “python site_bot.py” :
  
![Capture d’écran 2024-09-06 200152](https://github.com/user-attachments/assets/5dc51e67-103c-46d9-aa1c-34736eef3ed3)



Appuyez sur **Entrée**, et voilà, c'est lancé !

![Capture d’écran 2024-09-05 145201](https://github.com/user-attachments/assets/f04826a3-1bd7-4d9c-ba53-79bd21f40cd5)

> **Si message d’erreur pour Outlook (erreur de connexion) :**  
> Allez dans la sécurité de votre compte pour activer l’identification à 2 facteurs. Une fois activée, toujours sur la même page, descendez jusqu’à **Mot de passe d’application** puis cliquez sur **Créer un mot de passe d’application**.

>![Capture d’écran 2024-09-08 133010](https://github.com/user-attachments/assets/cb52b23d-6ef7-4825-aa01-87dcb70c9e8d)
![Capture d’écran 2024-09-08 133439](https://github.com/user-attachments/assets/2efc257a-c972-49fe-803e-aa6efb7409e6)

> Ce sera ce mot de passe que vous devrez mettre dans la variable d’environnement `EMAIL_PASS` (voir Étape 2).

