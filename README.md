## Pour l'installation 

py -3.12 -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt

## Pour le lancement du serveur

python -m uvicorn app.main:app --reload

## Pour les tests

python -m pytest -q