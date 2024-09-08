<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tutoriel : Créer un Bot Python pour se Désinscrire des Newsletters</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        h2 {
            color: #2980b9;
        }
        p {
            margin-bottom: 10px;
        }
        code {
            background-color: #eaeaea;
            padding: 2px 5px;
            border-radius: 5px;
        }
        pre {
            background-color: #eaeaea;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        ul {
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <h1><strong>BONJOUUUR</strong> !</h1>
    
    <p>Voici les <strong>5 étapes à suivre</strong> pour créer votre propre bot (gratuitement) qui vous permettra de vous désinscrire automatiquement de tous les sites qui vous envoient des mails ennuyeux :</p>
    <p><em>(Pour Gmail, un autre tuto arrivera car c’est un peu plus compliqué)</em></p>
    <p>Ouvrez le lien sur PC pour une meilleure qualité d'image.</p>
    <p>Si d'autres personnes s'y connaissent en code, n’hésitez pas à me DM pour d’éventuelles améliorations.</p>
    
    <h2>Guide : Créer un bot Python pour se désinscrire des newsletters (Outlook, Yahoo)</h2>
    
    <h3>Objectif du bot :</h3>
    <ul>
        <li>Se connecter à une boîte email via IMAP (Outlook, Yahoo).</li>
        <li>Parcourir les emails pour détecter les newsletters.</li>
        <li>Suivre le lien de désabonnement pour tenter de se désabonner automatiquement.</li>
    </ul>
    
    <h3>Prérequis :</h3>
    <ul>
        <li>Python 3.x installé sur votre machine.</li>
        <li>Une adresse email Outlook ou Yahoo.</li>
    </ul>
    
    <h2>Étape 1 : Installer Python et les dépendances</h2>
    <p>Si vous n'avez pas encore Python, téléchargez-le et installez-le depuis <a href="https://www.python.org">python.org</a>.</p>
    <p>Ensuite, installez les bibliothèques Python nécessaires en ouvrant un terminal ou une invite de commandes et en exécutant la commande suivante :</p>
    <pre><code>pip install requests</code></pre>
    
    <h2>Étape 2 : Configurer les identifiants avec des variables d'environnement</h2>
    
    <h3>Sous Windows :</h3>
    <ul>
        <li>Ouvrez le menu Démarrer et tapez "Variables d'environnement".</li>
        <li>Cliquez sur <em>Modifier les variables d'environnement du système</em>.</li>
        <li>Dans la fenêtre Variables d'environnement, sous Variables utilisateur, cliquez sur <em>Nouveau</em>.</li>
        <li>Créez deux nouvelles variables :
            <ul>
                <li><code>EMAIL_USER</code> : votre adresse email (Outlook, Yahoo).</li>
                <li><code>EMAIL_PASS</code> : votre mot de passe email.</li>
            </ul>
        </li>
    </ul>
    
    <h3>Sous Mac/Linux :</h3>
    <ul>
        <li>Ouvrez un terminal.</li>
        <li>Ajoutez vos identifiants à la fin de votre fichier <code>.bashrc</code> ou <code>.zshrc</code>.</li>
    </ul>
    
    <h2>Étape 4 : Créer et configurer le script Python</h2>
    <p>Ouvrez un éditeur de texte (comme Visual Studio Code, Sublime Text, ou même Notepad) et créez un fichier <code>unsubscribe_bot.py</code>. Collez le code suivant dans ce fichier. Vous devrez ajuster la variable <code>service</code> en fonction du fournisseur de messagerie que vous utilisez (Outlook, Gmail, ou Yahoo).</p>
    
    <h3>CODE à copier :</h3>
    <p>Par défaut, le code est configuré avec <code>service = "outlook"</code>. C'est en bas du code, et vous devrez changer la valeur en fonction de votre service, donc mettre <code>service = "yahoo"</code> pour Yahoo, etc.</p>
    
    <p>Ensuite, enregistrez ce fichier sous le nom <code>site_bot.py</code>.</p>
    
    <h2>Étape 5 : Lancer le bot</h2>
    <ul>
        <li>Faites un clic droit sur le dossier contenant le fichier et sélectionnez "Ouvrir dans le terminal".</li>
        <li>Ensuite, tapez la commande suivante dans le terminal :
            <pre><code>python site_bot.py</code></pre>
        </li>
    </ul>
    
    <p>Appuyez sur Entrée et voilà, le bot est lancé !</p>
    
    <h3>Problèmes éventuels :</h3>
    <p>Si vous obtenez une erreur de connexion avec Outlook, suivez les étapes suivantes :</p>
    <ul>
        <li>Accédez à la sécurité de votre compte et activez l'authentification à deux facteurs.</li>
        <li>Créez un mot de passe d'application dans la section <em>Mot de passe d'application</em>.</li>
        <li>Utilisez ce mot de passe dans la variable d'environnement <code>EMAIL_PASS</code> (voir Étape 2).</li>
</code></pre>
</body>
</html>
