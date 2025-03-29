import os
import requests
from datetime import datetime
from app.config import API_KEY, CAMERA_ID, SAVE_DIRECTORY, API_URL

def take_snapshot():
    try:
        # API-Aufruf
        response = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={"camera_id": CAMERA_ID}
        )
        response.raise_for_status()

        # Foto speichern
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"snapshot_{timestamp}.jpg"
        filepath = os.path.join(SAVE_DIRECTORY, filename)

        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"Foto gespeichert: {filepath}")
    except Exception as e:
        print(f"Fehler beim Aufnehmen des Fotos: {e}")