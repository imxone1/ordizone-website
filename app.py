"""
Application Flask pour le site OrdiZone
Backend principal gérant les routes et la logique de l'application
"""

from flask import Flask, render_template, request, flash, redirect, url_for
import os
import re

# Initialisation de l'application Flask
app = Flask(__name__)

# Configuration
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24).hex())
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False') == 'True'


# ----------------------------
# HEADERS DE SECURITE
# ----------------------------
@app.after_request
def set_security_headers(response):

    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'

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


# ----------------------------
# DONNEES PRODUITS
# ----------------------------
PRODUCTS = [
    {
        'id': 1,
        'name': 'HP EliteBook 830 G7',
        'description': 'Core i5 10ème génération • SSD 512Go • RAM 16Go',
        'price': '200 000 FCFA',
        'image': 'hp-elitebook-830-g7.jpg'
    },
    {
        'id': 2,
        'name': 'HP EliteBook 830 G5',
        'description': 'Core i5 8ème génération • SSD 256Go • RAM 8Go',
        'price': '150 000 FCFA',
        'image': 'hp-elitebook-830-g5.jpg'
    },
    {
        'id': 3,
        'name': 'HP EliteBook X360 1030 G3',
        'description': 'Core i7 8ème génération • SSD 512Go • RAM 16Go',
        'price': '210 000 FCFA',
        'image': 'hp-x360-1030-g3.jpg'
    },
    {
        'id': 4,
        'name': 'Dell Latitude 5400',
        'description': 'Core i5 8ème génération • SSD 256Go • RAM 8Go',
        'price': '150 000 FCFA',
        'image': 'dell-latitude-5400.jpg'
    },
    {
        'id': 5,
        'name': 'Lenovo ThinkPad W540',
        'description': 'Core i7 4ème génération • HDD 1To • RAM 16Go',
        'price': '100 000 FCFA',
        'image': 'lenovo-w540.jpg'
    },
    {
        'id': 6,
        'name': 'Samsung Galaxy S20',
        'description': 'Stockage 256Go • RAM 8Go',
        'price': '255 000 FCFA',
        'image': 'samsung-s20.jpg'
    }
]


# ----------------------------
# DONNEES SERVICES
# ----------------------------
SERVICES = [
    {
        'id': 1,
        'name': "Vente d'ordinateurs",
        'description': "Ordinateurs portables et de bureau",
        'icon': '💻'
    },
    {
        'id': 2,
        'name': "Maintenance informatique",
        'description': "Réparation et dépannage",
        'icon': '🔧'
    },
    {
        'id': 3,
        'name': "Installation Windows",
        'description': "Installation OS et logiciels",
        'icon': '💿'
    },
    {
        'id': 4,
        'name': "Réseau informatique",
        'description': "Configuration réseau",
        'icon': '🌐'
    },
    {
        'id': 5,
        'name': "Community manager",
        'description': "Gestion réseaux sociaux",
        'icon': '📱'
    },
    {
        'id': 6,
        'name': "Assistance informatique",
        'description': "Conseils personnalisés",
        'icon': '💡'
    }
]


PHONE_NUMBER = "+22944277997"
WHATSAPP_LINK = f"https://wa.me/{PHONE_NUMBER}"


# ----------------------------
# ROUTES
# ----------------------------

@app.route('/')
def index():
    return render_template('index.html', services=SERVICES)


@app.route('/produits')
def produits():
    return render_template(
        'produits.html',
        products=PRODUCTS,
        whatsapp_link=WHATSAPP_LINK
    )


@app.route('/services')
def services():
    return render_template(
        'services.html',
        services=SERVICES,
        whatsapp_link=WHATSAPP_LINK
    )


@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':

        nom = request.form.get('nom', '').strip()
        telephone = request.form.get('telephone', '').strip()
        message = request.form.get('message', '').strip()

        if not nom or not telephone or not message:
            flash("Veuillez remplir tous les champs.", "error")

        elif len(nom) > 100:
            flash("Nom trop long.", "error")

        elif len(telephone) > 20:
            flash("Numéro invalide.", "error")

        elif len(message) > 1000:
            flash("Message trop long.", "error")

        else:

            phone_pattern = r'^[\d\s\+\-\(\)]+$'

            if not re.match(phone_pattern, telephone):
                flash("Format du numéro invalide.", "error")

            else:
                flash("Merci pour votre message.", "success")
                return redirect(url_for('contact'))

    return render_template(
        'contact.html',
        phone_number=PHONE_NUMBER,
        whatsapp_link=WHATSAPP_LINK
    )


# ----------------------------
# DEMARRAGE APPLICATION
# ----------------------------

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=app.config['DEBUG']
    )
