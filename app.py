from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "API Fusionnée Anatomie & Imagerie Médicale – EDN",
        "sources": ["MedPix", "Radiopaedia"]
    })

@app.route("/get_medical_image", methods=["GET"])
def get_medical_image():
    theme = request.args.get("theme", "").strip().lower()
    if not theme:
        return jsonify({"error": "Veuillez préciser un thème, ex: ?theme=pneumothorax"}), 400

    results = []

    # ---- 1️⃣ Recherche MedPix ----
    try:
        medpix_url = f"https://medpix.nlm.nih.gov/api/cases?query={theme}"
        r = requests.get(medpix_url, timeout=6)
        if r.status_code == 200 and "cases" in r.json():
            cases = r.json()["cases"]
            if len(cases) > 0:
                case = cases[0]
                results.append({
                    "source": "MedPix",
                    "title": case.get("title", "Cas MedPix"),
                    "description": case.get("diagnosis", "Cas médical"),
                    "image_url": case.get("image_url", ""),
                    "link": f"https://medpix.nlm.nih.gov/case/{case.get('id', '')}"
                })
    except Exception as e:
        print("Erreur MedPix :", e)

    # ---- 2️⃣ Recherche Radiopaedia ----
    try:
        radio_url = f"https://radiopaedia.org/search.json?q={theme}"
        r2 = requests.get(radio_url, timeout=6)
        if r2.status_code == 200 and "articles" in r2.json():
            articles = r2.json()["articles"]
            if len(articles) > 0:
                art = articles[0]
                results.append({
                    "source": "Radiopaedia",
                    "title": art.get("title", "Cas Radiopaedia"),
                    "description": art.get("summary", "Cas d'imagerie"),
                    "image_url": f"https://radiopaedia.org/cases/{art.get('slug','')}",
                    "link": f"https://radiopaedia.org/{art.get('slug','')}"
                })
    except Exception as e:
        print("Erreur Radiopaedia :", e)

    if not results:
        return jsonify({"error": "Aucun résultat trouvé pour ce thème"}), 404

    return jsonify({"theme": theme, "results": results})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
