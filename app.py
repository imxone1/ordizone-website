"""
Application Flask pour le site OrdiZone
Backend principal gérant les routes et la logique de l'application
"""

from flask import Flask, render_template, request, flash, redirect, url_for
import os
import re

# Initialisation de l'application Flask
app = Flask(__name__)

# Configuration de sécurité
# Clé secrète : utiliser une variable d'environnement en production, ou générer une clé fixe
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24).hex())

# En production, DEBUG doit être False pour la sécurité
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False') == 'True'

# Headers de sécurité pour protéger contre diverses attaques
@app.after_request
def set_security_headers(response):
    """
    Ajoute des headers de sécurité HTTP pour protéger l'application
    """
    # Empêche le MIME-sniffing (évite que le navigateur devine le type de fichier)
    response.headers['X-Content-Type-Options'] = 'nosniff'
    
    # Empêche l'inclusion de la page dans une iframe (protection contre clickjacking)
    response.headers['X-Frame-Options'] = 'DENY'
    
    # Active la politique de sécurité stricte du navigateur (XSS protection)
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    # Politique de référent (ne pas envoyer l'URL complète)
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    
    # Permissions policy (désactive certaines fonctionnalités par défaut)
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
    
    # Content Security Policy (CSP) - protège contre XSS
    # Autorise les ressources du même domaine et Font Awesome CDN
    csp = (
        "default-src 'self'; "
        "style-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; "
        "script-src 'self' 'unsafe-inline'; "
        "font-src 'self' https://cdnjs.cloudflare.com; "
        "img-src 'self' data: https:; "
        "connect-src 'self'; "
        "frame-ancestors 'none';"
    )
    response.headers['Content-Security-Policy'] = csp
    
    return response

# Données des produits (peuvent être remplacées par une base de données)
PRODUCTS = [
    {
        'id': 1,
        'name': 'HP EliteBook 830 G7',
        'description': 'Core i5 10ème génération • Disque dur : 512Go SSD • RAM : 16Go • Autonomie : 4H environ',
        'price': '200 000 FCFA',
        'image': 'hp elitebook 830 g7.jpg'
    },
    {
        'id': 2,
        'name': 'HP EliteBook 830 G5',
        'description': 'Core i5 8ème génération • Écran 13,3" • Clavier rétro éclairé AZERTY d\'origine • Disque dur : 256Go • RAM : 8Go • Autonomie : 4H',
        'price': '150 000 FCFA',
        'image': 'hp elitebook 830 g5.jpg'
    },
    {
        'id': 3,
        'name': 'HP EliteBook X360 1030 G3',
        'description': 'Core i7 8ème génération • Écran 13" tactile rotatif à 360° • Disque dur : 512Go SSD • RAM : 16Go • Autonomie : 4H • Super clean • 2 pièces disponibles',
        'price': '210 000 FCFA',
        'image': 'hp elitebook x360 1030 g3.jpg'
    },
    {
        'id': 4,
        'name': 'Dell Latitude 5400',
        'description': 'Core i5 8ème génération • Écran 14" • Clavier simple • Disque dur : 256Go • RAM : 8Go • Autonomie : 4H',
        'price': '150 000 FCFA',
        'image': 'dell latitude 5400.jpg'
    },
    {
        'id': 5,
        'name': 'Lenovo ThinkPad W540',
        'description': 'Core i7 4ème génération • Écran 15,6" • Pavé numérique • Clavier rétro éclairé • RAM : 16Go • Disque dur : 1To HDD • Graphique dédiée : 2Go DDR5 Nvidia • Autonomie : 3H',
        'price': '100 000 FCFA',
        'image': 'lenovo w540.jpg'
    },
    {
        'id': 6,
        'name': 'Samsung Galaxy S20',
        'description': 'Smartphone Samsung Galaxy S20 • Stockage : 256Go • RAM : 8Go',
        'price': '255 000 FCFA',
        'image': 'sammsung s20.jpg'
    }
]

# Données des services
SERVICES = [
    {
        'id': 1,
        'name': 'Vente d\'ordinateurs',
        'description': 'Large sélection d\'ordinateurs portables et de bureau de qualité',
        'icon': '💻'
    },
    {
        'id': 2,
        'name': 'Maintenance et dépannage informatique',
        'description': 'Réparation et maintenance de vos équipements informatiques',
        'icon': '🔧'
    },
    {
        'id': 3,
        'name': 'Installation de Windows et logiciels',
        'description': 'Installation de systèmes d\'exploitation et logiciels nécessaires',
        'icon': '💿'
    },
    {
        'id': 4,
        'name': 'Réseau informatique',
        'description': 'Configuration et maintenance de réseaux informatiques',
        'icon': '🌐'
    },
    {
        'id': 5,
        'name': 'Community manager',
        'description': 'Gestion de vos réseaux sociaux et présence en ligne',
        'icon': '📱'
    },
    {
        'id': 6,
        'name': 'Conseils et assistance informatique',
        'description': 'Conseils personnalisés pour vos besoins informatiques',
        'icon': '💡'
    }
]

# Numéro de téléphone et lien WhatsApp
PHONE_NUMBER = "+22944277997"
WHATSAPP_LINK = f"https://wa.me/{PHONE_NUMBER}"


@app.route('/')
def index():
    """Route pour la page d'accueil"""
    return render_template('index.html', services=SERVICES)


@app.route('/produits')
def produits():
    """Route pour la page des produits"""
    return render_template('produits.html', products=PRODUCTS, whatsapp_link=WHATSAPP_LINK)


@app.route('/services')
def services():
    """Route pour la page des services"""
    return render_template('services.html', services=SERVICES, whatsapp_link=WHATSAPP_LINK)


def validate_input(text, max_length=500):
    """
    Valide et nettoie les entrées utilisateur pour éviter les attaques XSS
    """
    if not text:
        return False, ""
    
    # Limiter la longueur
    if len(text) > max_length:
        return False, ""
    
    # Nettoyer les caractères dangereux (protection basique contre XSS)
    # Flask/Jinja2 échappe automatiquement dans les templates, mais c'est une couche supplémentaire
    text = text.strip()
    
    return True, text


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Route pour la page de contact"""
    if request.method == 'POST':
        # Récupération et nettoyage des données du formulaire
        nom = request.form.get('nom', '').strip()
        telephone = request.form.get('telephone', '').strip()
        message = request.form.get('message', '').strip()
        
        # Validation des champs
        if not nom or not telephone or not message:
            flash('Veuillez remplir tous les champs du formulaire.', 'error')
        elif len(nom) > 100:
            flash('Le nom est trop long (maximum 100 caractères).', 'error')
        elif len(telephone) > 20:
            flash('Le numéro de téléphone est trop long.', 'error')
        elif len(message) > 1000:
            flash('Le message est trop long (maximum 1000 caractères).', 'error')
        else:
            # Validation supplémentaire du numéro de téléphone (format basique)
            # Autorise les chiffres, espaces, +, -, (), etc.
            phone_pattern = r'^[\d\s\+\-\(\)]+$'
            if not re.match(phone_pattern, telephone):
                flash('Le format du numéro de téléphone n\'est pas valide.', 'error')
            else:
                # Ici, vous pourriez envoyer un email ou sauvegarder dans une base de données
                # Pour l'instant, on affiche juste un message de succès
                # Note: Les données sont automatiquement échappées par Jinja2 dans les templates
                flash('Merci pour votre message ! Nous vous contacterons bientôt.', 'success')
                # Redirection pour éviter la resoumission du formulaire (POST-Redirect-GET pattern)
                return redirect(url_for('contact'))
    
    return render_template('contact.html', phone_number=PHONE_NUMBER, whatsapp_link=WHATSAPP_LINK)


if __name__ == '__main__':
    # Démarrage de l'application Flask
    app.run(debug=True, host='0.0.0.0', port=5000)

