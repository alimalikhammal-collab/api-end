API Fusionnée Anatomie & Imagerie Médicale – EDN

Cette API permet de rechercher des images anatomiques et radiologiques en interrogeant automatiquement **MedPix (NIH)** et **Radiopaedia**.

## 🚀 Utilisation locale

```bash
pip install -r requirements.txt
python app.py
```

Ouvrir dans le navigateur :
```
http://127.0.0.1:5000/get_medical_image?theme=pneumothorax
```

## 🌍 Déploiement sur Render

1. Créer un compte sur https://render.com
2. Créer un nouveau service "Web Service"
3. Importer ce projet (ou le zip)
4. Runtime : Python 3
5. Commande de démarrage : `python app.py`
6. Port : 5000

#L’API sera ensuite disponible à une URL du type :  
`https://api-edn-imagerie.onrender.com/get_medical_image?theme=coeur`

## 🧠 Connexion à GPT Builder

Ajouter dans ton GPT une *Action* avec ce schéma OpenAPI :

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "API Fusionnée Anatomie & Imagerie Médicale",
    "version": "1.0.0"
  },
  "servers": [
    { "url": "https://api-edn-imagerie.onrender.com" }
  ],
  "paths": {
    "/get_medical_image": {
      "get": {
        "description": "Recherche une image médicale (anatomie ou imagerie) par mot-clé.",
        "parameters": [
          {
            "name": "theme",
            "in": "query",
            "description": "Thème à rechercher (ex: coeur, cerveau, pneumothorax)",
            "required": true,
            "schema": { "type": "string" }
          }
        ]
      }
    }
  }
}
```
