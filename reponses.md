Exercice 1 : 

1. Pour créer une station, on utilise le verbe POST et on utilise le code HTTP 201

2. Pour une station inexistante on va renvoyer le code HTTP 404 avec une réponse en json qui va permettre d'expliquer concrètement l'erreur.

3. Le code HTTP 401 présente un client non authentifié tandis que le code HTTP 403 présente un client authentifié mais qui n'a pas les droits pour accéder à la ressource.

Exercice 3.4 :
Après redemarrage du serveur, avec une vérification sur une station existante, on obtient le code HTTP 200 et la station est bien présente dans la base de données.

Exercice 4.3 :
Après deux lancements de suite de la commande python -m pytest -q, j'obtiens le même résultat les deux fois qui est le suivant : 8 passed, 1 warning in 0.12s
avec également le lien suivant : -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html