# Guide de Déploiement - OrdiZone

Ce guide explique comment déployer votre site OrdiZone pour le rendre accessible à tous sur Internet.

## Option 1 : Render (Recommandé - GRATUIT) ⭐

Render offre un plan gratuit avec une URL personnalisée.

### Étapes :

1. **Créer un compte sur Render**
   - Allez sur https://render.com
   - Créez un compte gratuit (avec GitHub, GitLab ou email)

2. **Préparer votre code sur GitHub/GitLab**
   - Créez un compte GitHub si vous n'en avez pas (https://github.com)
   - Créez un nouveau repository
   - Uploadez tous vos fichiers du projet

3. **Déployer sur Render**
   - Dans Render, cliquez sur "New +" → "Web Service"
   - Connectez votre repository GitHub/GitLab
   - Configurez le service :
     - **Name**: ordizone (ou un nom de votre choix)
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
   - Cliquez sur "Create Web Service"

4. **Accéder à votre site**
   - Render vous donnera une URL comme : `https://ordizone.onrender.com`
   - Votre site sera accessible partout dans le monde !

### Avantages Render :
- ✅ Gratuit (avec limitations)
- ✅ URL HTTPS automatique
- ✅ Déploiement automatique depuis GitHub
- ✅ Facile à utiliser

---

## Option 2 : Railway

Railway est une autre excellente option gratuite.

### Étapes :

1. Allez sur https://railway.app
2. Créez un compte (avec GitHub)
3. Cliquez sur "New Project" → "Deploy from GitHub repo"
4. Sélectionnez votre repository
5. Railway détecte automatiquement Flask et déploie
6. Votre site sera accessible sur une URL Railway

---

## Option 3 : PythonAnywhere

Spécialement conçu pour les applications Python.

### Étapes :

1. Créez un compte gratuit sur https://www.pythonanywhere.com
2. Allez dans "Web" → "Add a new web app"
3. Choisissez "Flask" et Python 3.x
4. Uploadez vos fichiers
5. Configurez le WSGI file pour pointer vers app.py
6. Reload l'application

---

## Option 4 : VPS (Serveur Privé Virtuel)

Pour un contrôle total (payant, ~5-10€/mois).

### Hébergeurs populaires :
- DigitalOcean
- Linode
- Vultr
- OVH (Français)

### Configuration basique :

1. Achetez un VPS
2. Installez Python, pip, et nginx
3. Configurez gunicorn comme serveur WSGI
4. Configurez nginx comme reverse proxy
5. Installez un certificat SSL (Let's Encrypt gratuit)

---

## Configuration pour Production

⚠️ **Important** : Avant de déployer, assurez-vous que :

1. Le mode DEBUG est désactivé (déjà configuré dans app.py) ✅
2. Vous avez un fichier `requirements.txt` à jour ✅
3. Vous utilisez gunicorn en production ✅
4. **Définissez SECRET_KEY dans les variables d'environnement Render** ⚠️

### Sécurité

Votre site inclut déjà plusieurs mesures de sécurité :
- ✅ Headers de sécurité HTTP (protection XSS, clickjacking, etc.)
- ✅ Validation des formulaires
- ✅ HTTPS automatique sur Render
- ✅ Mode DEBUG désactivé en production

**Consultez le fichier [SECURITY.md](SECURITY.md) pour plus de détails sur la sécurité.**

---

## Domaine Personnalisé (Optionnel)

Si vous avez un nom de domaine (ex: ordizone.bj) :

1. Dans Render/Railway, allez dans les paramètres
2. Ajoutez votre domaine personnalisé
3. Configurez les DNS de votre domaine pour pointer vers Render/Railway
4. Le certificat SSL sera généré automatiquement

---

## Support

Pour toute question sur le déploiement, consultez la documentation officielle de la plateforme choisie.

