"""
Application Flask pour le site OrdiZone
"""

from flask import Flask, render_template, request, flash, redirect, url_for
import os
import re

# IMPORTANT : indiquer où sont les fichiers HTML
app = Flask(__name__, template_folder='.')

# Configuration
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24).hex())
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False') == 'True'


@app.after_request
def set_security_headers(response):

    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'

    return response


PRODUCTS = [
    {
        'id': 1,
        'name': 'HP EliteBook 830 G7',
        'description': 'Core i5 • SSD 512Go • RAM 16Go',
        'price': '200 000 FCFA',
        'image': 'hp elitebook 830 g7.jpg'
    }
]

SERVICES = [
    {
        'id': 1,
        'name': "Vente d'ordinateurs",
        'description': "Ordinateurs portables et de bureau",
        'icon': '💻'
    }
]

PHONE_NUMBER = "+22944277997"
WHATSAPP_LINK = f"https://wa.me/{PHONE_NUMBER}"


@app.route('/')
def index():
    return render_template('index.html', services=SERVICES)


@app.route('/produits')
def produits():
    return render_template('produits.html', products=PRODUCTS, whatsapp_link=WHATSAPP_LINK)


@app.route('/services')
def services():
    return render_template('services.html', services=SERVICES, whatsapp_link=WHATSAPP_LINK)


@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':

        nom = request.form.get('nom', '').strip()
        telephone = request.form.get('telephone', '').strip()
        message = request.form.get('message', '').strip()

        if not nom or not telephone or not message:
            flash("Veuillez remplir tous les champs.", "error")

        else:

            phone_pattern = r'^[\d\s\+\-\(\)]+$'

            if not re.match(phone_pattern, telephone):
                flash("Numéro invalide.", "error")
            else:
                flash("Merci pour votre message.", "success")
                return redirect(url_for('contact'))

    return render_template('contact.html',
                           phone_number=PHONE_NUMBER,
                           whatsapp_link=WHATSAPP_LINK)


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=app.config['DEBUG']
    )
