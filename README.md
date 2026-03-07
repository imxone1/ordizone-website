# OrdiZone - Site Web

Site web professionnel pour OrdiZone, une entreprise spécialisée dans la vente d'ordinateurs et les services informatiques au Bénin.

## Technologies utilisées

- **Backend**: Python 3.x + Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Design**: Responsive, mobile-first

## Installation

1. **Installer les dépendances Python**:
```bash
pip install -r requirements.txt
```

2. **Lancer l'application**:
```bash
python app.py
```

3. **Accéder au site**:
Ouvrez votre navigateur et allez sur `http://localhost:5000`

## Structure du projet

```
.
├── app.py                 # Application Flask principale
├── requirements.txt       # Dépendances Python
├── templates/            # Templates HTML (Jinja2)
│   ├── base.html         # Template de base
│   ├── index.html        # Page d'accueil
│   ├── produits.html     # Page des produits
│   ├── services.html     # Page des services
│   └── contact.html      # Page de contact
└── static/               # Fichiers statiques
    ├── css/
    │   └── style.css     # Styles CSS principaux
    └── js/
        ├── main.js       # Script JavaScript principal
        └── carousel.js   # Script pour le carousel
```

## Fonctionnalités

- ✅ Design responsive (mobile, tablette, desktop)
- ✅ Navigation avec menu mobile
- ✅ Carousel automatique des services
- ✅ Formulaire de contact
- ✅ Intégration WhatsApp
- ✅ Design moderne et professionnel

## Personnalisation

### Modifier les couleurs
Les couleurs principales sont définies dans `static/css/style.css` via les variables CSS (`:root`).

### Ajouter des produits
Modifiez la liste `PRODUCTS` dans `app.py`.

### Ajouter des services
Modifiez la liste `SERVICES` dans `app.py`.

### Modifier le numéro de téléphone
Modifiez la variable `PHONE_NUMBER` dans `app.py`.

## Déploiement en Production

Pour rendre votre site accessible à tous sur Internet, consultez le fichier [DEPLOYMENT.md](DEPLOYMENT.md) qui contient un guide complet de déploiement sur différentes plateformes (Render, Railway, PythonAnywhere, etc.).

**Solution rapide (GRATUIT) :**
1. Créez un compte sur https://render.com
2. Connectez votre repository GitHub
3. Déployez en quelques clics
4. Votre site sera accessible sur une URL publique !

## Gestion des Images

Le site utilise de vraies images pour les produits. Pour gérer les images :

1. **Copier les images initiales** :
   ```bash
   python copy_images.py
   ```

2. **Vérifier les images** :
   ```bash
   python manage_products.py --check
   ```

3. **Ajouter de nouvelles images** :
   - Placez l'image dans le dossier `images`
   - Exécutez `python copy_images.py`
   - Ajoutez le produit dans `app.py`

Consultez `GUIDE_IMAGES.md` pour la documentation complète.

## Notes

- Le formulaire de contact affiche actuellement un message de succès. Pour l'envoyer par email, vous devrez configurer SMTP dans Flask.
- Les images de produits doivent être copiées dans `static/images` pour être affichées.
- En production, le mode DEBUG est automatiquement désactivé pour la sécurité.

## Licence

© 2024 OrdiZone. Tous droits réservés.

