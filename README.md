<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Créer un Bot de Désinscription Automatique</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        h1 {
            color: #4CAF50;
            text-align: center;
        }
        h2 {
            color: #2196F3;
        }
        p {
            margin-bottom: 1em;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 4px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        ul {
            list-style-type: square;
            margin-left: 20px;
        }
        .note {
            background-color: #ffeb3b;
            padding: 10px;
            border-left: 5px solid #fbc02d;
            margin-bottom: 20px;
            border-radius: 4px;
        }
    </style>
</head>
<body>

    <h1>BONJOUUUR !</h1>

    <p>Voici les 5 étapes à suivre pour créer votre propre bot (gratuitement) qui vous permettra de vous désinscrire automatiquement de tous les sites qui vous envoient des mails chiants :</p>

    <div class="note">
        <strong>Note :</strong> Pour Gmail, un autre tutoriel arrivera car c'est un peu plus compliqué.
    </div>

    <p>Ouvrez le lien sur PC pour avoir une meilleure qualité d'image.</p>
    <p>Si d'autres personnes s'y connaissent en code, n'hésitez pas à me DM pour d'éventuelles améliorations.</p>

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

    <h3>Étape 1 : Installer Python et les dépendances</h3>
    <p>Si vous n'avez pas encore Python, téléchargez-le et installez-le depuis <a href="https://www.python.org/downloads/">python.org</a>.</p>
    <p>Ensuite, installez les bibliothèques Python nécessaires en ouvrant un terminal ou une invite de commandes et en exécutant les commandes suivantes :</p>
    <pre><code>pip install requests</code></pre>

    <h3>Étape 2 : Configurer les identifiants avec des variables d'environnement</h3>
    <h4>Sous Windows :</h4>
    <ul>
        <li>Ouvrez le menu Démarrer et tapez "Variables d'environnement".</li>
        <li>Cliquez sur <strong>Modifier les variables d'environnement du système</strong>.</li>
        <li>Dans la fenêtre <strong>Variables d'environnement</strong>, sous <strong>Variables utilisateur</strong>, cliquez sur <strong>Nouveau</strong>.</li>
        <li>Créez deux nouvelles variables :
            <ul>
                <li><code>EMAIL_USER</code> : votre adresse email (Outlook, Yahoo).</li>
                <li><code>EMAIL_PASS</code> : votre mot de passe email.</li>
            </ul>
        </li>
    </ul>

    <h4>Sous Mac/Linux :</h4>
    <p>Ouvrez un terminal et ajoutez vos identifiants à la fin de votre fichier <code>.bashrc</code> ou <code>.zshrc</code> :</p>
    <pre><code>export EMAIL_USER="votre_email"
export EMAIL_PASS="votre_mot_de_passe"</code></pre>

    <h3>Étape 4 : Créer et configurer le script Python</h3>
    <p>Ouvrez un éditeur de texte (comme Visual Studio Code, Sublime Text, ou même Notepad) et créez un fichier <code>unsubscribe_bot.py</code>. Collez le code suivant dans ce fichier. Vous devrez ajuster la variable <code>service</code> en fonction du fournisseur de messagerie que vous utilisez (Outlook, Gmail, ou Yahoo).</p>

    <div class="note">
        <strong>Code à copier :</strong><br>
        Là, le code est par défaut sur <code>service = "outlook"</code>.<br>
        C'est tout en bas du code, et c'est ce que vous devrez changer en fonction de votre service (par exemple, <code>service = "yahoo"</code> pour Yahoo).
    </div>

    <h3>Étape 5 : Lancer le bot</h3>
    <ul>
        <li>Faites clic droit sur le dossier et sélectionnez "Ouvrir dans le terminal".</li>
        <li>Puis tapez <code>python [nom du fichier]</code> (par exemple : <code>python site_bot.py</code>).</li>
    </ul>
    <p>Faites entrée, et voilà, c'est lancé !</p>

    <div class="note">
        <strong>Si message d'erreur pour Outlook (erreur de connexion) :</strong><br>
        Allez dans la sécurité de votre compte pour activer l'identification à 2 facteurs. Une fois activée, toujours sur la même page, descendez jusqu'à <strong>Mot de passe d'application</strong> puis cliquez sur <strong>Créer un mot de passe d'application</strong>.<br>
        Ce sera ce mot de passe que vous devrez mettre dans la variable d'environnement <code>EMAIL_PASS</code> (voir Étape 2).
    </div>

</body>
</html>
