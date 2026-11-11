
import json
from pathlib import Path


def test_durees_incidents_strictement_positives():
    chemin = Path(__file__).resolve().parents[1] / "data" / "services.json"

    with open(chemin, encoding="utf-8") as fichier:
        donnees = json.load(fichier)

    for service in donnees["services"]:
        for duree in service["incidents"]:
            assert duree > 0, (
                f"Durée d'incident invalide pour {service['id']} : {duree}"
            )
