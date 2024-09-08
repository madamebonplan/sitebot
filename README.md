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


### Étape 4 : Créer et configurer le script Python
Ouvrez un éditeur de texte (comme Visual Studio Code, Sublime Text, ou même Notepad) et créez un fichier `unsubscribe_bot.py`. Collez le code suivant dans ce fichier. Vous devrez ajuster la variable `service` en fonction du fournisseur de messagerie que vous utilisez (Outlook, Gmail, ou Yahoo).

**Code à copier :**
> Là, le code est par défaut sur `service = "outlook"`.  
> C’est tout en bas du code et c’est cela que vous devrez changer en fonction de votre service (par exemple `service = "yahoo"` pour Yahoo).

### Étape 5 : Lancer le bot
- Faites un clic droit sur le dossier et sélectionnez **Ouvrir dans le terminal**.
- Ensuite, tapez la commande suivante :


Par exemple :


Appuyez sur **Entrée**, et voilà, c'est lancé !

> **Si message d’erreur pour Outlook (erreur de connexion) :**  
> Allez dans la sécurité de votre compte pour activer l’identification à 2 facteurs. Une fois activée, toujours sur la même page, descendez jusqu’à **Mot de passe d’application** puis cliquez sur **Créer un mot de passe d’application**.
>
> Ce sera ce mot de passe que vous devrez mettre dans la variable d’environnement `EMAIL_PASS` (voir Étape 2).

