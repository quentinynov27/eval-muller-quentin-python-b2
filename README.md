## Pour l'installation 

py -3.12 -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt

## Pour le lancement du serveur

python -m uvicorn app.main:app --reload

## Pour les tests

python -m pytest -q

## Problèmes rencontrés

j'ai eu des problèmes comme pendant les cours avec python, j'ai du faire plusieurs manipulations moi même pour le coup mais j'ai finalement réussi à regler le problème des dépendences et de la version python entre msys64 et msys2.
