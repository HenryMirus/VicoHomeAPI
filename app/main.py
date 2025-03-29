from app.config import SAVE_DIRECTORY
from app.api.actions import take_snapshot
import os
import time


def main():
    if not os.path.exists(SAVE_DIRECTORY):
        os.makedirs(SAVE_DIRECTORY)

    print("Starte Fotoaufnahme...")
    while True:
        take_snapshot()
        time.sleep(30)

if __name__ == "__main__":
    main()