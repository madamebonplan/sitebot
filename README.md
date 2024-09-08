BONJOUUUR ! 

Voici les 5 étapes à suivre pour créer votre propre bot (gratuitement) qui vous permettra de vous désinscrire automatiquement de tous les sites qui vous envoient des mails chiants : 

(Pour Gmail un autre tuto arrivera car c’est un peu plus compliqué) 

Guide : Créer un bot Python pour se désinscrire des newsletters (Outlook, Yahoo)
Objectif du bot :
Se connecter à une boîte email via IMAP (Outlook, Yahoo).
Parcourir les emails pour détecter les newsletters.
Suivre le lien de désabonnement pour tenter de se désabonner automatiquement.
Prérequis :
Python 3.x installé sur votre machine.
Une adresse email Outlook, Yahoo.
Étape 1 : Installer Python et les dépendances
Si vous n'avez pas encore Python, téléchargez-le et installez-le depuis python.org.
Ensuite, installez les bibliothèques Python nécessaires en ouvrant un terminal ou une invite de commandes et en exécutant les commandes suivantes :


« pip install requests »
Étape 2 : Configurer les identifiants avec des variables d'environnement
Sous Windows :
Ouvrez le menu Démarrer et tapez "Variables d'environnement".
Cliquez sur Modifier les variables d'environnement du système.
Dans la fenêtre Variables d'environnement, sous Variables utilisateur, cliquez sur Nouveau.
Créez deux nouvelles variables :
EMAIL_USER : votre adresse email (Outlook, Yahoo).
EMAIL_PASS : votre mot de passe email.
Sous Mac/Linux :
Ouvrez un terminal.
Ajoutez vos identifiants à la fin de votre fichier .bashrc ou .zshrc :

Étape 4 : Créer et configurer le script Python
Ouvrez un éditeur de texte (comme Visual Studio Code, Sublime Text, ou même Notepad) et créez un fichier unsubscribe_bot.py. Collez le code suivant dans ce fichier. Vous devrez ajuster la variable service en fonction du fournisseur de messagerie que vous utilisez (Outlook, Gmail, ou Yahoo).
CODE à copier :
Là le code est par défaut sur service = “outlook”
C’est tout en bas du code et c’est ça que vous devrez changer en fonction de votre service donc mettre service = « yahoo » si c’est pour Yahoo etc



Donc copiez coller sur Block note ou autre et nommez votre fichier comme par exemple site_bot.py

Vous aurez donc un dossier comme ça : 


Créez un dossier pour le mettre comme ceci : 


Étape 5 : Lancer le bot
Faites clique droit sur le dossier et “ouvrir dans le terminal”


Puis écrire “python [nom du fichier]” donc pour moi c’est : “python site_bot.py”


Faites entrée et voilà c’est lancé : 
# sitebot
